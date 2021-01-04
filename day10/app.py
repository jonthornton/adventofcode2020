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



    sorted_input = sorted(input)

    diffs = calc_differences(sorted_input)

    print(diffs[1] * diffs[3])

    print(count_solutions(sorted_input))


def calc_differences(sorted_input):
    prev = 0
    diffs = {
        1: 0,
        2: 0,
        3: 1
    }

    for adapter in sorted_input:
        diff = adapter - prev
        prev = adapter
        diffs[diff] += 1

    print(diffs)
    return diffs

def count_solutions(sorted_input, start=0):
    prev = start
    count = 0

    # print(sorted_input)

    for i, adapter in enumerate(sorted_input):
        if i + 1 < len(sorted_input):
            next = sorted_input[i + 1]
        else:
            next = sorted_input[-1] + 3

        if next - prev <= 3:
            # we can skip this adapter
            count += count_solutions(sorted_input[i+1:], prev)

        prev = adapter
    
    count += 1
    return count


if __name__ == '__main__':
    main()
