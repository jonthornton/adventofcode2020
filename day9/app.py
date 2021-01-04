# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

LOOKBACK = 25

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [int(line) for line in file]

    invalid = find_invalid(input)
    print(invalid)

    out = find_contiguous(input, invalid)
    print(out)
    print(min(out) + max(out))

def find_contiguous(input, target):
    for i in range(len(input)):
        sum = 0
        collector = []

        for j in range(i, len(input)):
            collector.append(input[j])
            sum += input[j]

            if sum == target:
                return collector
            elif sum > target:
                break

    return False

def find_invalid(input):
    collector = []
    for newnum in input:
        if len(collector) > LOOKBACK:
            if not is_valid_last_number(collector[-1 * LOOKBACK:], newnum):
                return newnum

        collector.append(newnum)


def is_valid_last_number(source, target):

    if find_first_sum_pairs(source, target):
        return True
    else:
        return False

def find_first_sum_pairs(source, target):
    for i in range(len(source)):
        for j in range(i, len(source)):
            if source[i] + source[j] == target:
                return [source[i] + source[j]]

    return False

if __name__ == '__main__':
    main()
