"""Lanzador simple para ejecutar Snake TUI en Debian."""

from snake_tui import normalize_name, start_game


if __name__ == "__main__":
    try:
        player = normalize_name(input("Introduce tu nombre (ENTER para anonimo): "))
    except (EOFError, KeyboardInterrupt):
        player = "ANON"
    start_game(player)

