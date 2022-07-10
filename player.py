from settings import *
from random import randrange
import pygame as pg

class Snake:

    def __init__(self):
        self.size = 40
        self.head = [randrange(0, WIDTH - self.size, self.size), randrange(0, HEIGHT - self.size, self.size)]
        self.body = [self.head]

        self.movement = self.last_movement = None

        self.color = SNAKE_COLOR[1]
        self.head_color = SNAKE_COLOR[0]
        

    def grow_up(self):
        self.body.insert(0, list(self.head))

    def update(self):
        # Movement
        if self.movement == "UP" and self.last_movement != "DOWN":
            self.last_movement = "UP"
        if self.movement == "LEFT" and self.last_movement != "RIGHT":
            self.last_movement = "LEFT"
        if self.movement == "RIGHT" and self.last_movement != "LEFT":
            self.last_movement = "RIGHT"
        if self.movement == "DOWN" and self.last_movement != "UP":
            self.last_movement = "DOWN"

        if self.last_movement == "RIGHT":
            self.head[0] += self.size
        elif self.last_movement == "LEFT":
            self.head[0] += -self.size
        elif self.last_movement == "UP":
            self.head[1] += -self.size
        elif self.last_movement == "DOWN":
            self.head[1] += self.size

        # Wormhole border
        if self.head[0] > WIDTH:
            self.head[0] = 0
        if self.head[0] < 0:
            self.head[0] = WIDTH - self.size
        if self.head[1] > HEIGHT:
            self.head[1] = 0
        if self.head[1] < 0:
            self.head[1] = HEIGHT - self.size

    def draw(self, canvas):
        for pos in self.body:
            pg.draw.rect(canvas, self.color if not pos == self.head else self.head_color, (pos[0], pos[1], self.size, self.size))    

    def getColision(self, apple_pos):
        return (self.head[0] == apple_pos[0] and self.head[1] == apple_pos[1])
