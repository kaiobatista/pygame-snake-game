import os
ABS_PATH = os.path.dirname(os.path.abspath(__file__))

WIDTH, HEIGHT = 600, 600
TITLE = 'Snake Game'

GAME_MUSIC = ABS_PATH + "/src/snd/8bit-bossa.mp3"
FRUIT_SOUND = ABS_PATH + "/src/snd/apple_sound.wav"
GAME_OVER_SOUND = ABS_PATH + "/src/snd/game-over-sound.wav"

GAME_OVER_MUSIC = ABS_PATH + "/src/snd/game-over.ogg"
START_SCREEN_MUSIC = ABS_PATH + "/src/snd/menu.mp3"

DEFAULT_FONT = ABS_PATH + "/src/fnts/nasalization-rg.ttf"

HIGHSCORE_PATH = ABS_PATH + "/highscore.txt"

SNAKE_COLOR = [(), ()]