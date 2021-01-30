import pygame as pg
from snake_conf import *
from apple import *
from texts import *
from start_and_end_screen import start_screen
from start_and_end_screen import end_screen


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


def load_game():
    global apple_sound, game_over_sound, any_apple, score, game_over, beginning, running, apple_x, apple_y, movement, last_movement
    global snake_head, snake_body
    pg.mixer.music.load("src/snd/8bit-bossa.mp3")
    apple_sound = pg.mixer.Sound("src/snd/apple_sound.wav")
    game_over_sound = pg.mixer.Sound("src/snd/game-over-sound.wav")
    any_apple = True
    score = 0
    game_over = False
    beginning = True
    running = True
    movement = last_movement = None
    apple_x, apple_y = apple_gen(WIDTH, HEIGHT)


pg.mixer.init()

clock = pg.time.Clock()
running = True
beginning = True
game_over = False

while running:

    if beginning:
        start_screen(window)
        load_game()
        pg.mixer.music.play(-1, 0.0)
        pg.mixer.music.set_volume(0.7)

    elif game_over:
        end_screen(window, score)
        load_game()
        snake_head = [randrange(0, 590, 10), randrange(0, 590, 10)]
        snake_body.clear()
        snake_body = [snake_head]
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.7)

    beginning = False

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
    # -- Game over -- #
    for block in snake_body[1:]:
        if block[0] == snake_head[0] and block[1] == snake_head[1]:
            pg.mixer.music.stop()
            pg.mixer.music.unload()
            game_over_sound.play()
            game_over = True

    last_movement = to_lastmove(movement, last_movement, snake_head)

    blackhole_border(snake_head)
    # -- Draw section -- #
    window.fill((0, 0, 0))
    snake_draw(window, snake_body, (0, 255, 0), 10)

    pg.draw.rect(window, (255, 0, 0), (apple_x, apple_y, 10, 10))
    score_text = "Score: " + str(score)
    show_text(window, score_text, (((WIDTH / 2) - (20 * len(score_text)) / 2 + 40), 0), (255, 255, 255))
    pg.display.flip()

pg.quit()
quit()
