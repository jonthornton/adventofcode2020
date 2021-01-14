# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os
import pprint

LOOKBACK = 25

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [split_word(line) for line in file]

    run_processing(input)

def split_word(word):
    return [char for char in word.strip()]

def print_seats(seat_map):
    for line in seat_map:
        for char in line:
            print(char, end='')
        print('')

def run_processing(seat_map):

    i=0
    prev_seat_map_str = ''
    current_seat_map = seat_map

    while prev_seat_map_str != str(current_seat_map):
        prev_seat_map_str = str(current_seat_map)
        current_seat_map = process_seats(current_seat_map)

        print('')
        print(i)
        print_seats(current_seat_map)
        i += 1

    print(count_seats(current_seat_map))    # TODO: current answer is too low

def deep_copy_seat_map(seat_map):
    new_seat_map = []

    for row in seat_map:
        new_row = []

        for seat in row:
            new_row.append(seat)

        new_seat_map.append(new_row)

    return new_seat_map

def process_seats(seat_map):

    new_seat_map = deep_copy_seat_map(seat_map)

    for i, row in enumerate(seat_map):
        for j, seat in enumerate(row):
            apply_seat_rules(seat_map, i, j, new_seat_map)

    return new_seat_map

def count_seats(seat_map):
    count = 0

    for row in seat_map:
        count += row.count('#')

    return count
            
def apply_seat_rules(old_seat_map, i, j, new_seat_map):
    if old_seat_map[i][j] == '.':
        new_seat_map[i][j] = '.'
        return

    adjacent = get_visible(old_seat_map, i, j)
    adjacent_count = adjacent.count('#')

    if old_seat_map[i][j] == '#' and adjacent_count >= 5:
        new_seat_map[i][j] = 'L'
    elif old_seat_map[i][j] == 'L' and adjacent_count == 0:
        new_seat_map[i][j] = '#'


def get_adjacent(seat_map, i, j):
    collector = []

    for i1 in range(i-1, i+2):
        for j1 in range(j-1, j+2):
            if i1 == i and j1 == j:
                continue

            if 0 <= i1 < len(seat_map) and 0 <= j1 < len(seat_map[0]):
                collector.append(seat_map[i1][j1])

    return collector

def safe_get(array_2d, i, j):
    if i < 0 or j < 0:
        return None

    if i < len(array_2d) and j < len(array_2d[i]):
        return array_2d[i][j]
    else:
        return None

def get_visible(seat_map, i, j):
    collector = []

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue

            step = 1
            val = safe_get(seat_map, i + di, j + dj)

            while val is not None:
                if val == '.':
                    step += 1
                    val = safe_get(seat_map, i + (di * step), j + (dj * step))
                else:
                    collector.append(val)
                    break
    # print(collector)
    return collector

if __name__ == '__main__':
    main()
