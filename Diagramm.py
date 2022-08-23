import matplotlib.pyplot as plt

import matplotlib.animation

import matplotlib.dates as mdate

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
    def x_time(self) -> str:
        return self.__x_time

    @x_time.setter
    def x_time(self, value: str) -> None:
        x = mdate.num2date(mdate.datestr2num(value))
        self.__x_time.append(x)

    @property
    def y_price(self) -> float:
        return self.__y_price

    @y_price.setter
    def y_price(self, value: float) -> None:
        self.__y_price.append(value)

    def animate(self, i):
        color = "g"
        self.__ax.clear()
        if len(self.__y_price) != 0:
            if self.__y_price[len(self.__y_price) - 1] > self.__y_price[len(self.__y_price) - 2]:
                 color="g"
            else:    
                color="r"
        self.__ax.plot(self.__x_time, self.__y_price, color=color)
        plt.xlabel("Время")
        plt.ylabel("Цена")

    def update(self):
        anim = matplotlib.animation.FuncAnimation(self.__fig, self.animate, interval=1000)
        plt.show()