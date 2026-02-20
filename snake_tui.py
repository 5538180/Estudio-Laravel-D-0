"""
Snake TUI para Debian (terminal Linux).

Objetivos didácticos cubiertos:
- Captura de teclado sin bloqueo con hilo secundario (flechas, q, p, +, -).
- Diseño modular: funciones separadas por responsabilidad (entrada, render, lógica, persistencia).
- Mínimo uso de variables globales de escritura (solo estado compartido del hilo de teclado).
- Persistencia de puntuaciones con pickle y top 10 al finalizar.

Controles:
- Flechas: mover serpiente
- p: pausar/reanudar
- + / -: aumentar o reducir velocidad
- q: salir

Si el terminal queda en estado raro tras una interrupción durante pruebas:
    reset
"""

from __future__ import annotations

import os
import pickle
import random
import shutil
import sys
import termios
import threading
import time
import tty
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# CÓDIGOS ANSI (estilo visual)
# ---------------------------------------------------------------------------
CURSOR_HIDE = "\033[?25l"
CURSOR_SHOW = "\033[?25h"
CLEAR_SCREEN = "\033[2J\033[H"
R_L = "\033[2K"
S_R = "\033[0m"
S_B = "\033[1m"

C_TITLE = "\033[97m"
C_ACCENT = "\033[38;5;153m"
C_BORDER = "\033[38;5;250m"
C_TEXT = "\033[37m"
C_SNAKE_BODY = "\033[38;5;84m"
C_SNAKE_HEAD = "\033[38;5;120m"
C_SNAKE_EAT = "\033[38;5;159m"
C_SNAKE_HIT = "\033[38;5;196m"
C_TOP = "\033[38;5;39m"
C_BAR_BG = "\033[48;5;16m"


@dataclass(frozen=True)
class GameConfig:
    """Configuración estática del juego (solo lectura)."""

    lines: int = 17
    columns: int = 62
    margin_left: int = 5
    margin_top: int = 2
    initial_length: int = 6

    # Velocidad: se trabaja con delay (segundos/tick).
    base_delay: float = 0.11
    speed_step: float = 0.01
    min_delay: float = 0.04
    max_delay: float = 0.22
    vertical_slow_factor: float = 1.10

    # Apariencia
    title: str = "PYTHON SNAKE"
    title_right: str = "DAW 2025"
    border_char: str = "█"
    body_horizontal: str = "■"
    body_vertical: str = "█"
    body_turn: str = "▮"
    fruit_char: str = "●"
    fruit_colors: Tuple[str, ...] = (
        "\033[38;5;99m",   # violeta
        "\033[38;5;39m",   # azul
        "\033[38;5;171m",  # magenta
        "\033[38;5;226m",  # amarillo
        "\033[38;5;51m",   # cian
    )

    # Persistencia
    score_file: str = "scores.pkl"


@dataclass
class GameState:
    """Estado mutable de una partida."""

    snake: List[Tuple[int, int]]
    direction: str
    fruit: Tuple[int, int]
    fruit_color: str
    score: int = 0
    paused: bool = False
    running: bool = True
    delay: float = GameConfig().base_delay
    head_color: str = C_SNAKE_HEAD
    head_flash_ticks: int = 0
    limits: Dict[str, int] = field(default_factory=dict)
    hud_line: int = 0
    map_bottom: int = 0
    player: str = "ANON"
    initial_length: int = 6


# ---------------------------------------------------------------------------
# VARIABLES GLOBALES COMPARTIDAS CON EL HILO DE TECLADO
# (escritura limitada a esta zona y al bucle principal)
# ---------------------------------------------------------------------------
lock = threading.Lock()
key_pressed: str = "R"  # última tecla detectada
speed_delay: float = GameConfig().base_delay

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


# ---------------------------------------------------------------------------
# UTILIDADES DE TERMINAL
# ---------------------------------------------------------------------------
def write(text: str) -> None:
    """Escribe texto sin salto de línea."""
    print(text, end="")


def move_cursor(line: int, column: int) -> None:
    """Mueve cursor a coordenadas 1-based."""
    write(f"\033[{line};{column}H")


def flush() -> None:
    """Fuerza volcado en pantalla para que la TUI responda al instante."""
    sys.stdout.flush()


def clear_screen() -> None:
    """Limpia pantalla y oculta cursor."""
    write(CLEAR_SCREEN + CURSOR_HIDE)
    flush()


def restore_terminal() -> None:
    """Restaura configuración TTY y vuelve a mostrar cursor."""
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    finally:
        write(S_R + CURSOR_SHOW)
        flush()


def beep(freq: int = 880, duration: int = 60) -> None:
    """
    Reproduce un sonido breve usando `beep` si está instalado.
    Si no existe, usa campana ASCII.
    """
    cmd = shutil.which("beep")
    if cmd:
        os.system(f"{cmd} -f {freq} -l {duration} >/dev/null 2>&1")
    else:
        write("\a")
        flush()


# ---------------------------------------------------------------------------
# TECLADO (captura no bloqueante en hilo secundario)
# ---------------------------------------------------------------------------
def start_keyboard(cfg: GameConfig) -> threading.Thread:
    """
    Hilo de lectura de teclado.

    Teclas:
    - Flechas: U, D, L, R
    - q: salir
    - p: pausar/reanudar
    - +/-: ajustar velocidad global compartida
    """

    def read_keyboard() -> None:
        global key_pressed, speed_delay
        try:
            tty.setcbreak(fd)
            while True:
                ch1 = sys.stdin.read(1)

                # Secuencias ANSI de flechas: ESC [ A/B/C/D
                if ch1 == "\x1b":
                    ch2 = sys.stdin.read(1)
                    ch3 = sys.stdin.read(1)
                    seq = ch1 + ch2 + ch3
                    mapping = {
                        "\x1b[A": "U",
                        "\x1b[B": "D",
                        "\x1b[C": "R",
                        "\x1b[D": "L",
                    }
                    key = mapping.get(seq, "")
                    if key:
                        with lock:
                            key_pressed = key
                elif ch1 in ("q", "Q"):
                    with lock:
                        key_pressed = "Q"
                    break
                elif ch1 in ("p", "P"):
                    with lock:
                        key_pressed = "P"
                elif ch1 == "+":
                    with lock:
                        speed_delay = max(cfg.min_delay, speed_delay - cfg.speed_step)
                elif ch1 == "-":
                    with lock:
                        speed_delay = min(cfg.max_delay, speed_delay + cfg.speed_step)
        finally:
            # Cierre defensivo por si el programa termina dentro del hilo.
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    th = threading.Thread(target=read_keyboard, daemon=True)
    th.start()
    return th


# ---------------------------------------------------------------------------
# RENDER DE UI
# ---------------------------------------------------------------------------
def draw_header(cfg: GameConfig) -> None:
    """Dibuja cabecera superior con título y etiqueta derecha."""
    total_width = cfg.columns + 2
    line = cfg.margin_top
    left = cfg.margin_left

    move_cursor(line, left)
    write(C_BAR_BG + " " * total_width + S_R)

    # Texto espaciado para aproximar el estilo visual de la referencia.
    stylized_title = " ".join("PYTHON") + "   " + " ".join("SNAKE")
    move_cursor(line, left + 2)
    write(C_BAR_BG + C_TITLE + S_B + stylized_title + S_R)

    right_col = left + total_width - len(cfg.title_right) - 2
    move_cursor(line, right_col)
    write(C_BAR_BG + C_ACCENT + S_B + cfg.title_right + S_R)
    flush()


def draw_map(cfg: GameConfig) -> Dict[str, int]:
    """
    Dibuja el marco del área de juego.

    Devuelve límites internos (zona por donde se mueve la serpiente):
      U: límite superior, D: inferior, L: izquierdo, R: derecho
    """
    top = cfg.margin_top + 1
    left = cfg.margin_left
    width = cfg.columns + 2
    b = cfg.border_char

    move_cursor(top, left)
    write(C_BORDER + b * width + S_R)

    for i in range(cfg.lines):
        move_cursor(top + 1 + i, left)
        write(C_BORDER + b + S_R + " " * cfg.columns + C_BORDER + b + S_R)

    move_cursor(top + cfg.lines + 1, left)
    write(C_BORDER + b * width + S_R)
    flush()

    return {
        "U": top + 1,
        "D": top + cfg.lines,
        "L": left + 1,
        "R": left + cfg.columns,
    }


def draw_layout(cfg: GameConfig) -> Tuple[Dict[str, int], int, int]:
    """Dibuja cabecera + mapa y devuelve (limits, map_bottom, hud_line)."""
    draw_header(cfg)
    limits = draw_map(cfg)
    map_bottom = limits["D"] + 1
    hud_line = map_bottom + 1
    return limits, map_bottom, hud_line


# ---------------------------------------------------------------------------
# LÓGICA DE SERPIENTE
# ---------------------------------------------------------------------------
def initial_snake(cfg: GameConfig, limits: Dict[str, int]) -> List[Tuple[int, int]]:
    """Crea serpiente inicial horizontal en la zona media-derecha."""
    center_line = (limits["U"] + limits["D"]) // 2
    head_col = limits["L"] + int(cfg.columns * 0.65)
    return [(center_line, head_col - i) for i in range(cfg.initial_length)]


def head_char_for_direction(direction: str) -> str:
    """Devuelve un carácter distinto para la cabeza según dirección."""
    return {
        "R": "▌",
        "L": "▐",
        "U": "▀",
        "D": "▄",
    }.get(direction, "▌")


def segment_char(
    cfg: GameConfig,
    prev_: Tuple[int, int] | None,
    curr: Tuple[int, int],
    next_: Tuple[int, int] | None,
) -> str:
    """
    Devuelve el símbolo del segmento según orientación.
    - Horizontal: body_horizontal
    - Vertical: body_vertical
    - Giro: body_turn
    """
    if prev_ is None or next_ is None:
        neighbor = next_ or prev_
        if neighbor and neighbor[0] == curr[0]:
            return cfg.body_horizontal
        return cfg.body_vertical

    if prev_[0] == next_[0]:
        return cfg.body_horizontal
    if prev_[1] == next_[1]:
        return cfg.body_vertical
    return cfg.body_turn


def draw_snake(cfg: GameConfig, state: GameState) -> None:
    """Dibuja la serpiente completa en pantalla."""
    for idx, cell in enumerate(state.snake):
        prev_ = state.snake[idx - 1] if idx > 0 else None
        next_ = state.snake[idx + 1] if idx < len(state.snake) - 1 else None
        move_cursor(*cell)
        if idx == 0:
            char = head_char_for_direction(state.direction)
            write(state.head_color + char + S_R)
        else:
            char = segment_char(cfg, prev_, cell, next_)
            write(C_SNAKE_BODY + char + S_R)
    flush()


def move_snake(state: GameState) -> Tuple[int, int]:
    """
    Avanza la serpiente una celda en `state.direction`.
    Devuelve la cola retirada (para borrar o recuperar si come fruta).
    """
    head_line, head_col = state.snake[0]
    delta = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}[state.direction]
    new_head = (head_line + delta[0], head_col + delta[1])
    state.snake.insert(0, new_head)
    return state.snake.pop()


def check_collision(state: GameState) -> bool:
    """Comprueba choque contra borde o cuerpo."""
    head = state.snake[0]
    l = state.limits
    hit_wall = head[0] < l["U"] or head[0] > l["D"] or head[1] < l["L"] or head[1] > l["R"]
    hit_body = head in state.snake[1:]
    return hit_wall or hit_body


# ---------------------------------------------------------------------------
# FRUTAS Y PUNTOS
# ---------------------------------------------------------------------------
def random_free_cell(state: GameState) -> Tuple[int, int]:
    """Busca una celda libre dentro del mapa que no esté ocupada por la serpiente."""
    while True:
        pos = (
            random.randint(state.limits["U"], state.limits["D"]),
            random.randint(state.limits["L"], state.limits["R"]),
        )
        if pos not in state.snake:
            return pos


def draw_fruit_at(cfg: GameConfig, pos: Tuple[int, int], color: str) -> None:
    """Dibuja fruta en una posición concreta."""
    move_cursor(*pos)
    write(color + cfg.fruit_char + S_R)
    flush()


def initial_fruit_cell(state: GameState) -> Tuple[int, int]:
    """
    Genera fruta inicial cerca de la izquierda para una salida visual
    parecida a la referencia.
    """
    l = state.limits
    center = (l["U"] + l["D"]) // 2
    min_line = max(l["U"], center - 4)
    max_line = min(l["D"], center + 4)
    min_col = l["L"] + 2
    max_col = min(l["R"], l["L"] + 10)

    for _ in range(100):
        pos = (random.randint(min_line, max_line), random.randint(min_col, max_col))
        if pos not in state.snake:
            return pos
    return random_free_cell(state)


def draw_fruit(cfg: GameConfig, state: GameState) -> Tuple[Tuple[int, int], str]:
    """Genera y dibuja una fruta en posición libre con color aleatorio."""
    pos = random_free_cell(state)
    color = random.choice(cfg.fruit_colors)
    draw_fruit_at(cfg, pos, color)
    return pos, color


def check_eat(cfg: GameConfig, state: GameState, removed_tail: Tuple[int, int]) -> bool:
    """
    Si la cabeza coincide con fruta:
    - vuelve a añadir la cola retirada para crecer
    - suma puntos
    - genera fruta nueva
    """
    if state.snake[0] != state.fruit:
        return False

    state.snake.append(removed_tail)
    state.score = len(state.snake) - state.initial_length
    state.head_flash_ticks = 2
    state.head_color = C_SNAKE_EAT

    beep(1200, 65)
    state.fruit, state.fruit_color = draw_fruit(cfg, state)
    return True


# ---------------------------------------------------------------------------
# HUD
# ---------------------------------------------------------------------------
def delay_to_speed_value(cfg: GameConfig, delay: float) -> int:
    """Convierte delay a valor de velocidad visible (1 = lenta, 10 = rápida)."""
    span = cfg.max_delay - cfg.min_delay
    if span <= 0:
        return 1
    normalized = (cfg.max_delay - delay) / span
    return max(1, min(10, int(round(1 + normalized * 9))))


def draw_hud(cfg: GameConfig, state: GameState) -> None:
    """Muestra marcador inferior (score, speed, player, pausa)."""
    speed_num = delay_to_speed_value(cfg, state.delay)
    pause_txt = "  [PAUSA]" if state.paused else ""

    # Barra negra inferior con tres bloques (izquierda, centro, derecha).
    bar_width = cfg.columns + 2
    move_cursor(state.hud_line, cfg.margin_left)
    write(C_BAR_BG + " " * bar_width + S_R)

    left_text = f"🐍 SCORE: {state.score:<3}"
    center_text = f"🚀 SPEED: {speed_num:<2}"
    right_text = f"🤖 {state.player}{pause_txt}"

    left_col = cfg.margin_left + 1
    center_col = cfg.margin_left + (bar_width // 2) - 6
    right_col = cfg.margin_left + bar_width - len(right_text) - 2

    move_cursor(state.hud_line, left_col)
    write(C_BAR_BG + C_TEXT + left_text + S_R)
    move_cursor(state.hud_line, center_col)
    write(C_BAR_BG + C_TEXT + center_text + S_R)
    move_cursor(state.hud_line, right_col)
    write(C_BAR_BG + C_TEXT + right_text + S_R)
    flush()


# ---------------------------------------------------------------------------
# SCORES (pickle)
# ---------------------------------------------------------------------------
def load_scores(cfg: GameConfig) -> List[Tuple[str, int]]:
    """Carga histórico de puntuaciones de disco."""
    if not os.path.exists(cfg.score_file):
        return []
    try:
        with open(cfg.score_file, "rb") as fh:
            data = pickle.load(fh)
            if isinstance(data, list):
                return data
    except Exception:
        return []
    return []


def save_scores(cfg: GameConfig, scores: List[Tuple[str, int]]) -> None:
    """Guarda histórico de puntuaciones en disco."""
    with open(cfg.score_file, "wb") as fh:
        pickle.dump(scores, fh)


def update_scores(cfg: GameConfig, player: str, score: int) -> List[Tuple[str, int]]:
    """Inserta partida actual y devuelve histórico ordenado descendentemente."""
    scores = load_scores(cfg)
    scores.append((player, score))
    scores.sort(key=lambda item: item[1], reverse=True)
    save_scores(cfg, scores)
    return scores


def print_top_scores(scores: List[Tuple[str, int]], player: str, current_score: int) -> None:
    """Imprime top 10 y resalta la entrada del jugador actual."""
    print("\nTOP 10 SCORES")
    for idx, (name, points) in enumerate(scores[:10], start=1):
        is_current = name == player and points == current_score
        color = C_TOP if is_current else C_TEXT
        print(f"{color}{idx:>2}. {name:<12} {points:>4}{S_R}")


# ---------------------------------------------------------------------------
# BUCLE PRINCIPAL
# ---------------------------------------------------------------------------
def start_game(player_name: str) -> None:
    """Inicializa y ejecuta una partida completa."""
    cfg = GameConfig()
    global key_pressed, speed_delay

    clear_screen()
    limits, map_bottom, hud_line = draw_layout(cfg)

    snake = initial_snake(cfg, limits)
    state = GameState(
        snake=snake,
        direction="R",
        fruit=(0, 0),
        fruit_color=cfg.fruit_colors[0],
        limits=limits,
        hud_line=hud_line,
        map_bottom=map_bottom,
        player=player_name,
        initial_length=cfg.initial_length,
        delay=cfg.base_delay,
    )

    # Fruta y HUD iniciales
    state.fruit = initial_fruit_cell(state)
    state.fruit_color = random.choice(cfg.fruit_colors)
    draw_fruit_at(cfg, state.fruit, state.fruit_color)
    draw_snake(cfg, state)
    draw_hud(cfg, state)

    # Estado compartido para el hilo de teclado
    key_pressed = "R"
    speed_delay = cfg.base_delay
    start_keyboard(cfg)

    opposite = {"U": "D", "D": "U", "L": "R", "R": "L"}

    try:
        while state.running:
            with lock:
                action = key_pressed
                key_pressed = ""
                state.delay = speed_delay

            # Salida voluntaria
            if action == "Q":
                break

            # Pausa
            if action == "P":
                state.paused = not state.paused
                draw_hud(cfg, state)
                continue

            # Cambio de dirección evitando giro de 180º.
            if action in ("U", "D", "L", "R") and action != opposite[state.direction]:
                state.direction = action
                state.paused = False

            if state.paused:
                time.sleep(0.05)
                continue

            # En vertical la serpiente se mueve un poco más lento.
            delay = state.delay
            if state.direction in ("U", "D"):
                delay *= cfg.vertical_slow_factor
            time.sleep(delay)

            removed_tail = move_snake(state)

            # Si choca, se marca la cabeza en rojo y termina.
            if check_collision(state):
                move_cursor(*removed_tail)
                write(" ")
                state.head_color = C_SNAKE_HIT
                draw_snake(cfg, state)
                beep(200, 120)
                break

            ate = check_eat(cfg, state, removed_tail)
            if not ate:
                move_cursor(*removed_tail)
                write(" ")

            # Destello breve tras comer fruta.
            if state.head_flash_ticks > 0:
                state.head_color = C_SNAKE_EAT
                state.head_flash_ticks -= 1
            else:
                state.head_color = C_SNAKE_HEAD

            draw_snake(cfg, state)
            draw_hud(cfg, state)
    finally:
        restore_terminal()
        print(f"\nGAME OVER - {state.player}: {state.score}")
        scores = update_scores(cfg, state.player, state.score)
        print_top_scores(scores, state.player, state.score)


def normalize_name(raw_name: str) -> str:
    """Normaliza nombre de jugador para HUD y top."""
    name = raw_name.strip().upper()
    if not name:
        return "ANON"
    return name[:12]


if __name__ == "__main__":
    try:
        player = normalize_name(input("Introduce tu nombre (ENTER para anonimo): "))
    except (EOFError, KeyboardInterrupt):
        player = "ANON"
    start_game(player)
