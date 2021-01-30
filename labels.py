import pygame as pg


def show_text(screen, text_input, lst=(0, 0), color=(255, 255, 255), font_type="src/fnts/nasalization-rg.ttf", size=20):
    _font = pg.font.Font(font_type, size)
    _text = _font.render(text_input, True, color)
    screen.blit(_text, lst)
