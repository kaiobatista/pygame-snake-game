import pygame as pg
from snake_conf import *
from apple import *

WIDTH, HEIGHT = 600, 600

pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")


def blackhole_border(lst):
    if lst[0] > WIDTH:
        lst[0] = 0
    if lst[0] < 0:
        lst[0] = WIDTH - 10
    if lst[1] > HEIGHT:
        lst[1] = 0
    if lst[1] < 0:
        lst[1] = HEIGHT - 10


def show_text(screen, text_input, lst=(0, 0), color=(255, 255, 255), font_type="src/fnts/nasalization-rg.ttf", size=20):
    _font = pg.font.Font(font_type, size)
    _text = _font.render(text_input, True, color)
    screen.blit(_text, lst)


any_apple = True

score = 0
# Background music
pg.mixer.init()
pg.mixer.music.load("src/snd/8bit-bossa.mp3")
pg.mixer.music.play(-1, 0.0)
pg.mixer.music.set_volume(0.7)

# Load Some sounds
apple_sound = pg.mixer.Sound("src/snd/apple_sound.wav")
apple_sound.set_volume(0.3)
#

apple_x, apple_y = apple_gen(WIDTH, HEIGHT)

clock = pg.time.Clock()
running = True
while running:
    clock.tick(20)
    # -- Events section -- #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                movement = "RIGHT"
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                movement = "LEFT"
            if event.key == pg.K_w or event.key == pg.K_UP:
                movement = "UP"
            if event.key == pg.K_s or event.key == pg.K_DOWN:
                movement = "DOWN"

    # -- Update section -- #
    growing_up_snake(snake_body, snake_head)
    if get_colision(snake_head, [apple_x, apple_y]):
        apple_sound.play()
        any_apple = False
        score += 1
    else:
        snake_body.pop()

    if not any_apple:
        apple_x, apple_y = apple_gen(WIDTH, HEIGHT)
        any_apple = True
    for block in snake_body[1:]:
        if block[0] == snake_head[0] and block[1] == snake_head[1]:
            running = False

    last_movement = to_lastmove(movement, last_movement)

    blackhole_border(snake_head)
    # -- Draw section -- #
    window.fill((0, 0, 0))
    snake_draw(window, (0, 255, 0), 10)

    pg.draw.rect(window, (255, 0, 0), (apple_x, apple_y, 10, 10))
    score_text = "Score: " + str(score)
    show_text(window, score_text, (((WIDTH / 2) - (20 * len(score_text)) / 2 + 40), 0), (255, 255, 255))
    pg.display.flip()

pg.quit()
quit()
