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
        input = [line for line in file]

    # part1(input)
    part2(input)

def part1(input):

    mem = {}
    mask_and = 0
    mask_or = 0

    for line in input:
        [key, val] = line.strip().split(' = ')

        if key == 'mask':
            [mask_and, mask_or] = parse_bitmask(val)
        else:
            register = get_mem_register(key)
            mem[register] = apply_bitmask(int(val), mask_and, mask_or)

    print(mem)
    print(sum(mem.values()))

def part2(input):

    mem = {}
    mask = ''

    for line in input:
        [key, val] = line.strip().split(' = ')

        if key == 'mask':
            mask = val
        else:
            register = get_mem_register(key)
            # print(mask, register)
            registers = get_registers(mask, register)
            print(registers)
            for reg in registers:
                mem[reg] = int(val)

    print(mem)
    print(sum(mem.values()))

def get_registers(mask, number, i=-1):
    number_str = list(bin(number)[2:])
    # print(bin(number)[2:])
    mask_str = list(mask)

    while i >= -1 * len(mask_str):
        if mask_str[i] == 'X':
            mask_str[i] = '1'
            # print(''.join(mask_str))
            heads = get_registers(''.join(mask_str), number, i-1)
            
            mask_str[i] = '0'
            # print(''.join(mask_str))
            tails = get_registers(''.join(mask_str), number, i-1)

            return heads + tails

        if i >= -1 * len(number_str) and number_str[i] == '1':
            mask_str[i] = '1'

        i -= 1

    print(''.join(mask_str), int(''.join(mask_str),2))
    return [int(''.join(mask_str),2)]

def get_mem_register(key):
    [foo, register] = key[:-1].split('[')
    return int(register)

def parse_bitmask(mask_string):
    mask_or = int(mask_string.replace('X', '0'), 2)
    mask_and = int(mask_string.replace('X', '1'), 2)
    return mask_and, mask_or

def apply_bitmask(number, mask_and, mask_or):
    return (number & mask_and) | mask_or

if __name__ == '__main__':
    main()
