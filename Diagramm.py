import matplotlib.pyplot as plt

import matplotlib.animation

matplotlib.use('TkAgg')

from collections import deque

class Diagramm:
    def __init__(self) -> None:
        self.__MAX_SIZE_DEQUE = 55
        self.__x_time = deque(maxlen=self.__MAX_SIZE_DEQUE)
        self.__y_price = deque(maxlen=self.__MAX_SIZE_DEQUE)
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1, 1, 1)

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

    def animate(self, i):
        print("dawdawd")
        self.__ax.clear()
        self.__ax.plot(self.__x_time, self.__y_price)
        plt.xlabel("Время")
        plt.ylabel("Цена")

    def update(self):
        anim = matplotlib.animation.FuncAnimation(self.__fig, self.animate, interval=1000)
        plt.show()