snake_head = [200, 300]
snake_body = [[200, 300]]

last_movement = None
movement = None


def growing_up_snake(lst, lst_head):
    lst.insert(0, list(lst_head))


def snake_move(mvmnt):
    if mvmnt == "RIGHT":
        snake_head[0] += 10
    elif mvmnt == "LEFT":
        snake_head[0] += -10
    elif mvmnt == "UP":
        snake_head[1] += -10
    elif mvmnt == "DOWN":
        snake_head[1] += 10


def snake_draw(screen, color, tam):
    import pygame.draw as pd
    for pos in snake_body:
        pd.rect(screen, color, (pos[0], pos[1], tam, tam))


def to_lastmove(mvmt, last_mvmt):
    if mvmt == "UP" and last_mvmt != "DOWN":
        last_mvmt = "UP"
    if mvmt == "LEFT" and last_mvmt != "RIGHT":
        last_mvmt = "LEFT"
    if mvmt == "RIGHT" and last_mvmt != "LEFT":
        last_mvmt = "RIGHT"
    if mvmt == "DOWN" and last_mvmt != "UP":
        last_mvmt = "DOWN"
    snake_move(last_mvmt)
    return last_mvmt


def get_colision(body1: list, body2: list):
    return body1[0] == body2[0] and body1[1] == body2[1]
