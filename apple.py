def apple_gen(width, height):
    from random import randrange
    x = randrange(0, width - 10, 10)
    y = randrange(0, height - 10, 10)
    return x, y
