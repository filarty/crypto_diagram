import matplotlib.pyplot as plt

import matplotlib

matplotlib.use('TkAgg')

from collections import deque

from random import randrange

class Diagramm:
    def __init__(self) -> None:
        self.__MAX_SIZE_DEQUE = 55
        self.__x_time = deque(maxlen=self.__MAX_SIZE_DEQUE)
        self.__y_price = deque(maxlen=self.__MAX_SIZE_DEQUE)
        self.__fig = plt.figure()

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

    def update(self):
        color = "g"
        self.__ax.plot(self.x_time, self.y_price, color=color)
        self.__fig.canvas.draw()
        self.__fig.canvas.start_event_loop(0.0001)

    def create(self):
        plt.clf()
        self.__ax = self.__fig.add_subplot(1, 1, 1)
        self.__fig.show()