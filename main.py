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

    def load_game(self):
        pg.mixer.music.load(GAME_MUSIC)
        pg.mixer.music.play()
        self.apple_sound = pg.mixer.Sound(APPLE_SOUND)
        self.game_over_sound = pg.mixer.Sound(GAME_OVER_SOUND)
        self.any_apple = True
        self.score = 0
        self.running = True
        
        self.apple_x, self.apple_y = self.apple_gen()

        self.snake = Snake()
    
    def run(self):
        self.start_screen()
        self.load_game()
        while self.running:
            self.clock.tick(30)
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
        self.snake.grow_up_snake()

        if self.snake.getColision([self.apple_x, self.apple_y]):
            self.apple_sound.play()
            self.any_apple = False
            self.score += 1
        else:
            self.snake.body.pop()

        if not self.any_apple:
            self.apple_x, self.apple_y = self.apple_gen()
            self.any_apple = True
        
        for block in self.snake.body[1:]:
            if block[0] == self.snake.head[0] and block[1] == self.snake.head[1]:
                pg.mixer.music.stop()
                pg.mixer.music.unload()
                self.game_over_sound.play()
                self.running = False        

    def draw(self):
        self.window.fill((0, 0, 0))
        self.snake.draw(self.window)
        pg.draw.rect(self.window, (255, 0, 0), (self.apple_x, self.apple_y, 10, 10))
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

    def exit(self):
        pg.quit()
        quit()

    @staticmethod
    def apple_gen():
        from random import randrange
        x = randrange(0, WIDTH - 10, 10)
        y = randrange(0, HEIGHT - 10, 10)
        return x, y

    def start_screen(self):
        
        pg.mixer.music.load(START_SCREEN_MUSIC)
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

            self.window.fill((194, 245, 66))
            show_text(self.window, "Snake Game", (30, 100), size=80)
            pg.draw.rect(self.window, (131, 171, 31), (200, 350, 200, 100))
            show_text(self.window, "Play!", (240, 400 - 30), (255, 255, 255), size=50)
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
                    pg.quit()
                    quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_q:
                        return False
                    if event.key == pg.K_r:
                        pg.mixer.music.stop()
                        pg.mixer.music.unload()
                        return True

            self.window.fill((36, 9, 11))
            show_text(self.window, text_score, lst=(400 - (30 * len(text_score)), 60), size=60)
            if self.score > highscore:
                set_highscore(self.score)
                show_text(self.window, "New Record!", (230, 150), size=20)
            show_text(self.window, 'Press "Q" to exit', (75, 350), size=30)
            show_text(self.window, 'Press "R" to play again', (75, 400), size=30)
            pg.display.flip()


if __name__ == "__main__":
    g = Game()
    g.run()
