import pygame as pg
from texts import show_text


def start_screen(screen):
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("src/snd/menu.mp3")
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.4)
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                    pg.mixer.music.stop()
                    pg.mixer.music.unload()
                    return 0
            if event.type == pg.MOUSEBUTTONDOWN:
                click = pg.mouse.get_pos()
                if 200 <= click[0] <= 400:
                    if 350 <= click[1] <= 450:
                        pg.mixer.music.stop()
                        pg.mixer.music.unload()
                        return 0

        screen.fill((194, 245, 66))
        show_text(screen, "Snake Game", (30, 100), size=80)
        pg.draw.rect(screen, (131, 171, 31), (200, 350, 200, 100))
        show_text(screen, "Play!", (240, 400 - 30), (255, 255, 255), size=50)
        pg.display.flip()


def end_screen(screen, score):
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("src/snd/game-over.ogg")
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.7)
    recorde = 10
    text_score = f"Score: {score}"
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYUP:
                if event.key == pg.K_q:
                    pg.quit()
                    quit()
                if event.key == pg.K_r:
                    pg.mixer.music.stop()
                    pg.mixer.music.unload()
                    return 0

        screen.fill((36, 9, 11))
        show_text(screen, text_score, lst=(400 - (30 * len(text_score)), 60), size=60)
        if score > recorde:
            show_text(screen, "New Record!", (230, 150), size=20)
        show_text(screen, 'Press "Q" to exit', (75, 350), size=30)
        show_text(screen, 'Press "R" to play again', (75, 400), size=30)
        pg.display.flip()
