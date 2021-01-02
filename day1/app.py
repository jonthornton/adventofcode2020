# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

def main():
    numbers = []
    with open('input.txt', 'r') as file:
        numbers = [int(line) for line in file]

    pair = find2020pair(numbers)
    print(pair)

    print(pair[0] * pair[1] * pair[2])

def find2020pair(numbers):
    for i, number1 in enumerate(numbers):
        for j, number2 in enumerate(numbers[i+1:]):
            for number3 in numbers[i+j+1:]:
                if number1 + number2 + number3 == 2020:
                    return [number1, number2, number3]


if __name__ == '__main__':
    main()
