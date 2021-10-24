from settings import *
from random import randrange
import pygame as pg

class Snake:

    def __init__(self):
        self.head = [randrange(0, 590, 10), randrange(0, 590, 10)]
        self.body = [self.head]

        self.movement = self.last_movement = None

        self.color = (0, 255, 0)
        self.size = 10

    def grow_up_snake(self):
        self.body.insert(0, list(self.head))

    def update(self):
        # Movement
        print(self.movement, self.last_movement)
        if self.movement == "UP" and self.last_movement != "DOWN":
            self.last_movement = "UP"
        if self.movement == "LEFT" and self.last_movement != "RIGHT":
            self.last_movement = "LEFT"
        if self.movement == "RIGHT" and self.last_movement != "LEFT":
            self.last_movement = "RIGHT"
        if self.movement == "DOWN" and self.last_movement != "UP":
            self.last_movement = "DOWN"

        if self.last_movement == "RIGHT":
            self.head[0] += 10
        elif self.last_movement == "LEFT":
            self.head[0] += -10
        elif self.last_movement == "UP":
            self.head[1] += -10
        elif self.last_movement == "DOWN":
            self.head[1] += 10

        # Blackhole border
        if self.head[0] > WIDTH:
            self.head[0] = 0
        if self.head[0] < 0:
            self.head[0] = WIDTH - 10
        if self.head[1] > HEIGHT:
            self.head[1] = 0
        if self.head[1] < 0:
            self.head[1] = HEIGHT - 10

    def draw(self, canvas):
        for pos in self.body:
            pg.draw.rect(canvas, self.color, (pos[0], pos[1], self.size, self.size))    

    def getColision(self, apple_pos):
        return (self.head[0] == apple_pos[0] and self.head[1] == apple_pos[1])
