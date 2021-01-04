# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

def main():
    instructions = []
    with open('input.txt', 'r') as file:
        instructions = [line for line in file]

    out = brute_force_fix_instructions(instructions)
    print(out)


def execute_instructions(instructions):
    visited = set()
    accumulator = 0
    i = 0
    while i < len(instructions):
        if i in visited:
            break

        visited.add(i)

        [operation, argument] = instructions[i].strip().split(' ')
        if operation == 'acc':
            accumulator += int(argument)
            i += 1
        elif operation == 'jmp':
            i += int(argument)
        elif operation == 'nop':
            i += 1

    return accumulator

def brute_force_fix_instructions(instructions):
    for i in range(len(instructions)):

        out = brute_force_helper(instructions, i)
        if out:
            print(i)
            return out


def brute_force_helper(instructions, idx_to_flip):
    visited = set()
    accumulator = 0
    i = 0
    while i < len(instructions):
        if i in visited:
            return False

        visited.add(i)

        [operation, argument] = instructions[i].strip().split(' ')

        if i == idx_to_flip:
            if operation == 'jmp':
                operation = 'nop'
            elif operation == 'nop':
                operation = 'jmp'
            else:
                return False

        if operation == 'acc':
            accumulator += int(argument)
            i += 1
        elif operation == 'jmp':
            i += int(argument)
        elif operation == 'nop':
            i += 1

    return accumulator


if __name__ == '__main__':
    main()
