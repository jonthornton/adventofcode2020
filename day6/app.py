# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

def main():
    yessum = 0
    input_collector = []
    with open('input.txt', 'r') as file:
        for line in file:
            if line == '\n':
                yessum += count_yeses(input_collector)
                input_collector = []
            else:
                input_collector.append(line.strip())

    yessum += count_yeses(input_collector)
        
    print(yessum)

def count_yeses(group_lines):
    yeses = {}
    for line in group_lines:
        for char in line:
            yeses[char] = yeses.get(char, 0) + 1

    count = 0
    for key in yeses:
        if yeses[key] == len(group_lines):
            count += 1

    return count

if __name__ == '__main__':
    main()

