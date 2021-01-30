from random import randrange
snake_head = [randrange(0, 590, 10), randrange(0, 590, 10)]
snake_body = [snake_head]

last_movement = None
movement = None


def growing_up_snake(lst, lst_head):
    lst.insert(0, list(lst_head))


def snake_move(mvmnt, lst):
    if mvmnt == "RIGHT":
        lst[0] += 10
    elif mvmnt == "LEFT":
        lst[0] += -10
    elif mvmnt == "UP":
        lst[1] += -10
    elif mvmnt == "DOWN":
        lst[1] += 10


def snake_draw(screen, lst, color, tam):
    import pygame.draw as pd
    for pos in lst:
        pd.rect(screen, color, (pos[0], pos[1], tam, tam))


def to_lastmove(mvmt, last_mvmt, lst):
    if mvmt == "UP" and last_mvmt != "DOWN":
        last_mvmt = "UP"
    if mvmt == "LEFT" and last_mvmt != "RIGHT":
        last_mvmt = "LEFT"
    if mvmt == "RIGHT" and last_mvmt != "LEFT":
        last_mvmt = "RIGHT"
    if mvmt == "DOWN" and last_mvmt != "UP":
        last_mvmt = "DOWN"
    snake_move(last_mvmt, lst)
    return last_mvmt


def get_colision(body1: list, body2: list):
    return body1[0] == body2[0] and body1[1] == body2[1]
