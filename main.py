import pygame as pg
from player import Snake
from settings import *

def show_text(screen, text_input, lst=(0, 0), color=(255, 255, 255), font_type=DEFAULT_FONT, size=20):
    _font = pg.font.Font(font_type, size)
    _text = _font.render(text_input, True, color)
    screen.blit(_text, lst)

def get_highscore():
    try:
        with open(HIGHSCORE_PATH, 'r+') as file:
            return file.read()
    except FileNotFoundError:
        with open(HIGHSCORE_PATH, 'w+') as file:
            file.close()

def set_highscore(scr):
    with open(HIGHSCORE_PATH, 'w+') as file:
        file.write(str(bin(scr)))


class Game: 

    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        self.clock = pg.time.Clock()
        self.beginning = True
        self.game_over = False
        self.running = True
        self.fruit_colors = {
                            "apple": (255, 0, 0), 
                            "blueberry": (0, 0, 255),
                            "orange": (255, 145, 0)
                            }
        self.fruit_sound = pg.mixer.Sound(FRUIT_SOUND)
        self.fruit_sound.set_volume(0.3)
        self.game_over_sound = pg.mixer.Sound(GAME_OVER_SOUND)
        self.game_over_sound.set_volume(0.4)

    def load_game(self):
        pg.mixer.music.load(GAME_MUSIC)
        pg.mixer.music.play()
        self.snake = Snake()

        self.any_fruit = True
        self.score = 0
        self.running = True
        
        self.fruit_x, self.fruit_y, self.fruit_type = self.fruit_gen()
        
        self.grid_on = False
        
    def run(self):
        self.start_screen()
        self.menu_screen()
        self.load_game()
        while self.running:
            self.clock.tick(20)
            self.events()
            self.update()
            self.draw()
        if self.end_screen():
            self.run()
        else:
            pg.quit()
            quit()

    def update(self):
        self.snake.update()

        self.snake.grow_up()
        if self.snake.getColision([self.fruit_x, self.fruit_y]):
            self.fruit_sound.play()
            self.any_fruit = False
            self.score += 1
            if self.fruit_type == 'blueberry':
                self.score +=1
            elif self.fruit_type == 'orange':
                self.snake.body.pop()
        else:
            self.snake.body.pop()

        if not self.any_fruit:
            self.fruit_x, self.fruit_y, self.fruit_type = self.fruit_gen()
            self.any_fruit = True
        
        for block in self.snake.body[1:]:
            if block[0] == self.snake.head[0] and block[1] == self.snake.head[1]:
                pg.mixer.music.stop()
                pg.mixer.music.unload()
                self.game_over_sound.play()
                self.running = False

    def draw(self):
        self.window.fill((10, 10, 10))
        if self.grid_on:
            self.draw_grid()
        self.snake.draw(self.window)
        pg.draw.rect(self.window, self.fruit_colors[self.fruit_type], (self.fruit_x, self.fruit_y, 40, 40))
        score_text = "Score: " + str(self.score)
        show_text(self.window, score_text, (((WIDTH / 2) - (20 * len(score_text)) / 2 + 40), 0), (255, 255, 255))
        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    self.snake.movement = "RIGHT"
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    self.snake.movement = "LEFT"
                if event.key == pg.K_w or event.key == pg.K_UP:
                    self.snake.movement = "UP"
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    self.snake.movement = "DOWN"

                # Debug controls
                if event.key == pg.K_SPACE:
                    self.snake.grow_up()
                if event.key == pg.K_g:
                    self.grid_on = not self.grid_on

    def exit(self):
        pg.quit()
        quit()

    def fruit_gen(self):
        import random
        while True:
            x = random.randrange(0, WIDTH - 40, 40)
            y = random.randrange(0, HEIGHT - 40, 40)
            if [x, y] not in self.snake.body:
                break
        chance = random.random()
        chance = 0

        if chance > 1 - 0.1:
            fruit_type = 'orange'
        elif chance > 1 - 0.3:
            fruit_type = 'blueberry'
        else:
            fruit_type = 'apple'
        return x, y, fruit_type

    def draw_grid(self):
        for i in range(int(WIDTH / 40)):
            pg.draw.line(self.window, (255, 255, 255), (0, 40 * i), (WIDTH, 40 * i))
            pg.draw.line(self.window, (255, 255, 255), (40 * i, 0), (40 * i, HEIGHT))

    def start_screen(self):
        
        pg.mixer.music.load(START_SCREEN_MUSIC)
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play()
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                        pg.mixer.music.stop()
                        pg.mixer.music.unload()
                        return 0

                if event.type == pg.MOUSEBUTTONDOWN:
                    click = pg.mouse.get_pos()
                    if WIDTH / 2 - 100 <= click[0] <= WIDTH / 2 + 100:
                        if 350 <= click[1] <= 450:
                            pg.mixer.music.stop()
                            pg.mixer.music.unload()
                            return 0

            self.window.fill((194, 245, 66))
            show_text(self.window, "Snake Game", (WIDTH / 2 - len("Snake Game") * 50 / 2, 100), size=80)
            pg.draw.rect(self.window, (131, 171, 31), (WIDTH / 2 - 100, 350, 200, 100))
            show_text(self.window, "Play!", (WIDTH / 2 - 60, 400 - 30), (255, 255, 255), size=50)
            pg.display.flip()

    def end_screen(self):
        pg.mixer.music.load(GAME_OVER_MUSIC)
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.7)
        highscore = get_highscore()
        try:
            highscore = int(highscore, 2)
        except (ValueError, TypeError):
            if highscore is not int:
                highscore = 0
        text_score = f"Score: {self.score}"
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_q:
                        return False
                    if event.key == pg.K_r:
                        pg.mixer.music.stop()
                        pg.mixer.music.unload()
                        return True

            self.window.fill((36, 9, 11))
            show_text(self.window, text_score, lst=(WIDTH / 2 - (15 * len(text_score)), 60), size=60)
            if self.score > highscore:
                set_highscore(self.score)
                show_text(self.window, "New Record!", (WIDTH / 3, 150), size=20)
            show_text(self.window, '> Press "Q" to exit', (WIDTH / 3 - 200, 350), size=30)
            show_text(self.window, '> Press "R" to play again', (WIDTH / 3 - 200, 400), size=30)
            pg.display.flip()

    def menu_screen(self):
        cor_fundo = (0, 0, 0)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit()
            
                if event.type == pg.MOUSEBUTTONDOWN:
                    click = pg.mouse.get_pos()
                    if (click[0] - WIDTH * 0.25) ** 2 + (click[1] - HEIGHT / 2) ** 2 <= 40 ** 2:
                        SNAKE_COLOR[0] = (0, 255, 0)
                        SNAKE_COLOR[1] = cor_fundo = (20, 170, 0)
                    elif (click[0] - WIDTH * 0.5) ** 2 + (click[1] - HEIGHT / 2) ** 2 <= 40 ** 2:
                        SNAKE_COLOR[0] = (46, 191, 143)
                        SNAKE_COLOR[1] = cor_fundo = (49, 125, 100)
                    elif (click[0] - WIDTH * 0.75) ** 2 + (click[1] - HEIGHT / 2) ** 2 <= 40 ** 2:
                        SNAKE_COLOR[0] = (136, 51, 214)
                        SNAKE_COLOR[1] = cor_fundo = (98, 53, 133)
                    elif WIDTH / 2 - 25 + 90> click[0] > WIDTH / 2 - 50 and HEIGHT / 2 + 120 > click[1] > HEIGHT / 2 + 80:
                        if len(SNAKE_COLOR[0]) > 0 and len(SNAKE_COLOR[1]) > 0:
                            return 0

            self.window.fill(cor_fundo)
            show_text(self.window, "Choose the snake's color:", (WIDTH / 2 - 10 * len("Choose the snake's color:"), 80), size=40)
            pg.draw.circle(self.window, (0, 255, 0), (WIDTH * 0.25, HEIGHT / 2), 40)
            pg.draw.circle(self.window, (46, 191, 143), (WIDTH * 0.5 , HEIGHT / 2), 40)
            pg.draw.circle(self.window, (136, 51, 214), (WIDTH * 0.75, HEIGHT / 2), 40)
            pg.draw.rect(self.window, (0, 0, 0), (WIDTH / 2 - 50, HEIGHT / 2 + 80, 100, 40))
            show_text(self.window, "Start", (WIDTH / 2 - 25, HEIGHT / 2 + 90))
            pg.display.flip()


if __name__ == "__main__":
    g = Game()
    g.run()
