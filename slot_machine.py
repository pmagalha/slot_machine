
#init classes
import random

class Slot_machine:
    def __init__(self, capacity=5000):
        if int(capacity) >= 0:
            self.capacity = capacity
            self.balance = 0
            self.bet = 0
            self.matrix = [[0] * 3 for _ in range(3)] #3x3 matrix initialized
            for i in range(3):
                for j in range(3):
                    self.matrix[i][j] = random.randint(1, 6)
        else:
            raise ValueError

#deposit function
    def deposit(self, n):
        if self.balance + n <= self.capacity:
            self.balance += n
        else:
            raise ValueError("Capacity has been exceeded")

#bet function
    def bet_internal(self, n):
        if 1 <= n <= 3:
            self.balance -= n
            self._bet = n
            if self.balance <= 0:
                raise ValueError("You lost")
        else:
            raise ValueError("Invalid bet amount")

    @property
    def capacity(self):
        return self._capacity

    @property
    def bet(self):
        return self._bet

    @property
    def matrix(self):
        return self._matrix

    @property
    def balance(self):
        return self._balance

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @bet.setter
    def bet(self, bet):
        self._bet = bet

    @matrix.setter
    def matrix(self, matrix):
        # Latter add validation logic for the matrix
        self._matrix = matrix