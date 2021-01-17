# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os
import math

DIRECTIONS = ['N', 'E', 'S', 'W']

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [line for line in file]

    part2(input)

def part1(input):
    start = int(input[0])
    buses = [int(bus) for bus in filter(lambda val: val !='x', input[1].strip().split(','))]

    soonest_bus_time = max(buses)
    soonest_bus = -1

    for bus in buses:
        next_bus = soonest(bus, start)
        delta = next_bus - start
        if delta < soonest_bus_time:
            soonest_bus_time = delta
            soonest_bus = bus

    print(soonest_bus, soonest_bus_time, soonest_bus * soonest_bus_time)

def soonest(bus_id, depart):
    next_bus = math.ceil(depart * 1.0 / bus_id)
    return next_bus * bus_id

def part2(input):
    buses = ['x' if bus == 'x' else int(bus) for bus in input[1].strip().split(',')]
    print(buses)

    t = 0
    incr = buses[0]
    for i, bus in enumerate(buses):
        if i == 0:
            continue

        if bus == 'x':
            continue

        while (t + i) % bus != 0:
            # print(t, incr)
            t += incr

        print(t, bus)
        incr *= bus

    # print(t)


if __name__ == '__main__':
    main()