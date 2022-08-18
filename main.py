import matplotlib as mpl
import matplotlib.pyplot as plt

import time

from collections import deque


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


def f(x: int) -> int:
    if x < 6:
        return x + 2
    return x - 2


def main():
    x = [0, 1, 5, 9, 15]
    y = []
    for i in x:
        y.append(f(x = i))
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show() 

if __name__ == "__main__":
        main()