from random import randrange

from Diagramm import Diagramm

diagram = Diagramm()
diagram.x_time = 0
diagram.y_price = 0


async def main():
    x = 20
    count = 0
    diagram.create()
    while True:
        if count == 55:
            count = 0
            diagram.update()
            diagram.create()
        diagram.y_price = randrange(-100, 100)
        diagram.x_time = x
        diagram.update()
        x += 10
        count += 1
if __name__ == "__main__":
        main()