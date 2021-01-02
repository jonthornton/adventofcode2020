# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

def main():
    seats = []
    with open('input.txt', 'r') as file:
        for line in file:
            seats.append(seat_to_id(line))
            
    myseat = find_missing(seats)

    print(myseat)

def seat_to_id(seat_string):
    binary = seat_string.strip().replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    # print(int(binary, 2))
    return int(binary, 2)

def find_missing(seats):
    sorted_seats = sorted(seats)
    for i, id in enumerate(sorted_seats):
        if sorted_seats[i+1] - sorted_seats[i] > 1:
            return sorted_seats[i] + 1

    return False

if __name__ == '__main__':
    main()

