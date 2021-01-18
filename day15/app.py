# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os
import math


def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [line.strip() for line in file]

    s = Solution()
    # print(s.part1(input))
    print(s.part2(input))

class Solution:
    def part1(self, input):

        numbers = [int(x) for x in input[0].split(',')]

        for i in range(len(numbers), 2020):

            last_number = numbers[-1]
            last_index = self.get_last_index(numbers, last_number)

            if last_index == -1:
                numbers.append(0)
            else:
                numbers.append(i - last_index - 1)
            
            # print(numbers)

        return numbers[-1]

    def get_last_index(self, numbers, search):
        indexes = [idx for idx, val in enumerate(numbers[:-1]) if val == search]
        if indexes:
            return max(indexes)
        else:
            return -1

    def part2(self, input):

        numbers = [int(x) for x in input[0].split(',')]
        reverse_index = Indexer(numbers)

        for i in range(len(numbers), 30000000):
            last_number = numbers[-1]
            last_index = reverse_index.get(last_number)
            # print(last_number, last_index)
            if last_index == -1:
                numbers.append(0)
            else:
                numbers.append(i - 1 - last_index)
            
            reverse_index.add(i, numbers[i])
            # print(numbers)

        return numbers[-1]


class Indexer:
    def __init__(self, initial=[]):
        self.reverse_index = {}

        self.next_number = initial[-1]
        self.next_i = len(initial) - 1

        for i, number in enumerate(initial[:-1]):
            self.reverse_index[number] = i

    def add(self, i, number):
        self.reverse_index[self.next_number] = self.next_i

        self.next_number = number
        self.next_i = i

    def get(self, number):
        return self.reverse_index.get(number, -1)

if __name__ == '__main__':
    main()
