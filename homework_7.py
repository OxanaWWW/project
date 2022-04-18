# 1***********************8
from random import randint


class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        s = ''
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                s += f'{self.nums[i][j]:03} '
            s += '\n'
        return s

    def __add__(self, other):
        ##
        nums = [
            [self.nums[i][j] + other.nums[i][j] for j in range(len(self.nums[i]))]
                for i in range(len(self.nums))]
        return  Matrix(nums)


a = Matrix([[randint(0, 99) for _ in range(10)] for _ in range(10)])
b = Matrix([[randint(0, 99) for _ in range(10)] for _ in range(10)])
print(a)
print(b)
print(a + b)

# 2************************
#
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_cosumption(self, list_siuts):
        a = 0
        for suit in list_siuts:
            a += suit.consumption
        return a


  # for example
coat = Coat(50)
costume = Suit(1.96)
costume_2 = Suit(1.24)
costume_3 = Suit(1.76)
costume_4 = Suit(2.10)
list_cosumes = [costume_4, costume_3, costume_2, costume]
print(coat.consumption)
print(costume.consumption)
print(costume.sum_cosumption(list_cosumes))

#3********************

class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        diff = self.parts  - other.parts
        if diff >= 0:
            return Cell(diff)
        else:
            print(f'subtraction error')
    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_order(self, count):
        s = ''
        for i in range(self.parts//count):
            s += '*' * count + '\n'
        s += '*' * (self.parts % count) + '\n'
        return s

    def __str__(self):
        return f'{self.parts}'


# forEx
cell = Cell(22)
print(cell.make_order(8))
cell2 = Cell(15)
print(cell2.make_order(5))

print(cell - cell2)
print(cell + cell2)
print(cell * cell2)
print(cell / cell2)
print(cell2 - cell)