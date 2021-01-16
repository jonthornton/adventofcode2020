# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os
import pprint

DIRECTIONS = ['N', 'E', 'S', 'W']

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [line for line in file]

    part2(input)

def part1(instructions):
    x = 0
    y = 0
    bearing = DIRECTIONS.index('E')

    for instruction in instructions:
        [x, y, bearing] = process_instruction(x, y, bearing, instruction)

    print(x, y, abs(x) + abs(y))


def part2(instructions):
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1

    for instruction in instructions:
        [x, y, waypoint_x, waypoint_y] = process_instruction2(x, y, waypoint_x, waypoint_y, instruction)
        print(x, y, waypoint_x, waypoint_y)

    print(x, y, abs(x) + abs(y))


def process_instruction(x, y, bearing, instruction):
    command = instruction[0]
    value = int(instruction[1:])

    if command == 'N':
        y += value
    elif command == 'S':
        y -= value
    elif command == 'E':
        x += value
    elif command == 'W':
        x -= value
    elif command == 'L':
        bearing = int((bearing - value/90) % len(DIRECTIONS))
    elif command == 'R':
        bearing = int((bearing + value/90) % len(DIRECTIONS))
    elif command == 'F':
        new_instruction = '{0}{1}'.format(DIRECTIONS[bearing], value)
        return process_instruction(x, y, bearing, new_instruction)

    return x, y, bearing

def process_instruction2(x, y, waypoint_x, waypoint_y, instruction):
    command = instruction[0]
    value = int(instruction[1:])

    if command == 'N':
        waypoint_y += value
    elif command == 'S':
        waypoint_y -= value
    elif command == 'E':
        waypoint_x += value
    elif command == 'W':
        waypoint_x -= value
    elif command == 'L':
        waypoint_x, waypoint_y = rotate_left(waypoint_x, waypoint_y, int(value/90))
    elif command == 'R':
        waypoint_x, waypoint_y = rotate_right(waypoint_x, waypoint_y, int(value/90))
    elif command == 'F':
        x += waypoint_x * value
        y += waypoint_y * value

    return x, y, waypoint_x, waypoint_y

def rotate_right(x, y, times):
    for i in range(times):
        [x, y] = [y, -1 * x]

    return x, y

def rotate_left(x, y, times):
    for i in range(times):
        [x, y] = [-1 * y, x]

    return x, y

if __name__ == '__main__':
    main()
