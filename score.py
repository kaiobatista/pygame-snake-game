def get_highscore(arq):
    try:
        with open(arq, 'r+') as file:
            return file.read()
            file.close()
    except FileNotFoundError:
        with open(arq, 'w+') as file:
            file.close()


def set_highscore(arq, scr):
    with open(arq, 'w+') as file:
        file.write(str(bin(scr)))
