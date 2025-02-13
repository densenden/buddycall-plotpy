import asciimatics
from asciimatics.screen import Screen
import importlib

def draw_dashboard(screen):
    screen.clear()

    # ASCII Header mit US-Farben
    screen.print_at("********** TRUMP NEWS **********", 2, 2, Screen.COLOUR_RED)
    screen.print_at("********** MUSK TRENDS *********", 40, 2, Screen.COLOUR_BLUE)

    # Trump Visualisierung
    try:
        trump_module = importlib.import_module("trump")
        trump_module.show_trump_visual(screen)
    except ModuleNotFoundError:
        screen.print_at("[Trump Visual nicht implementiert]", 5, 10, Screen.COLOUR_WHITE)

    # Musk Visualisierung
    try:
        musk_module = importlib.import_module("musk")
        musk_module.show_musk_visual(screen)
    except ModuleNotFoundError:
        screen.print_at("[Musk Visual nicht implementiert]", 50, 10, Screen.COLOUR_WHITE)

    screen.refresh()

def main(screen):
    draw_dashboard(screen)
    while True:
        event = screen.get_key()
        if event in (ord("q"), ord("Q")):
            return

Screen.wrapper(main)
