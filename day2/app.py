# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

def main():
    count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            [policy, password] = line.split(':')
            if is_other_valid_password(policy, password):
                count += 1

    print(count)

def is_valid_password(policy, password):
    [counts, letter] = policy.split(' ')
    [mincount, maxcount] = counts.split('-')

    count = password.count(letter)
    if count < int(mincount) or count > int(maxcount):
        return False
    else:
        return True

def is_other_valid_password(policy, password):
    [counts, letter] = policy.split(' ')
    [mincount, maxcount] = counts.split('-')

    if password[int(mincount)] == letter and password[int(maxcount)] != letter:
        return True
    elif password[int(mincount)] != letter and password[int(maxcount)] == letter:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
