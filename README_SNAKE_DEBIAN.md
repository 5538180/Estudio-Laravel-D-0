# Snake TUI (Debian)

Juego Snake en modo texto para terminal Linux (Debian/Ubuntu), hecho en Python.

## Requisitos

- Python 3.10+ (normalmente ya instalado)
- Terminal compatible ANSI (GNOME Terminal, Konsole, xterm, etc.)
- Opcional: `beep` para sonidos de eventos

Instalar `beep` (opcional):

```bash
sudo apt update
sudo apt install beep
```

## Ejecutar

Desde la carpeta del proyecto:

```bash
python3 snake.py
```

Alternativa directa:

```bash
python3 snake_tui.py
```

## Controles

- Flechas: mover serpiente
- `p`: pausar/reanudar
- `+`: aumentar velocidad
- `-`: reducir velocidad
- `q`: salir

## Funcionalidades incluidas

- Mapa TUI con cabecera estilo `PYTHON SNAKE`
- Serpiente con caracteres distintos en horizontal, vertical y giros
- Frutas de color aleatorio
- Puntuación y velocidad en HUD
- Evita giro de 180 grados
- Persistencia de scores en `scores.pkl`
- Top 10 al terminar la partida

## Si el terminal se queda raro al interrumpir pruebas

Ejecuta:

```bash
reset
```
