
import matplotlib.pyplot as plt

import matplotlib

matplotlib.use('TkAgg')

from collections import deque

from random import randrange

class Diagramm:
    def __init__(self) -> None:
        self.__MAX_SIZE_DEQUE = 500
        self.__x_time = deque(maxlen=self.__MAX_SIZE_DEQUE)
        self.__y_price = deque(maxlen=self.__MAX_SIZE_DEQUE)

    @property
    def x_time(self) -> int:
        return self.__x_time

    @x_time.setter
    def x_time(self, value: int) -> None:
        self.__x_time.append(value)

    @property
    def y_price(self) -> int:
        return self.__y_price

    @y_price.setter
    def y_price(self, value: int) -> None:
        self.__y_price.append(value)

diagram = Diagramm()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fig.show()

def update():
    color = "g"
    ax.plot(diagram.x_time, diagram.y_price, color=color)
    fig.canvas.draw()
    fig.canvas.start_event_loop(0.010)



def main():
    x = 20
    while True:
        diagram.y_price = randrange(-100, 100)
        diagram.x_time = x
        update()
        x += 10

if __name__ == "__main__":
        main()