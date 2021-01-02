# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os
import re

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def main():
    count = 0
    input_collector = ''
    with open('input.txt', 'r') as file:
        for line in file:
            if line == '\n':
                if is_valid_passport(input_collector):
                    count += 1

                input_collector = ''
            else:
                input_collector += line.strip() + ' '

    if is_valid_passport(input_collector):
        count += 1

    print(count)



def is_valid_passport(collected_input):
    fields = set([])
    pairs = collected_input.strip().split(' ')
    # print(collected_input)
    for pair in pairs:
        [key, val] = pair.split(':')
        fields.add(key)
        if key == 'byr':
            if int(val) < 1920 or int(val) > 2002 or len(val) != 4:
                return False
        if key == 'iyr':
            if int(val) < 2010 or int(val) > 2020 or len(val) != 4:
                return False
        if key == 'eyr':
            if int(val) < 2020 or int(val) > 2030 or len(val) != 4:
                return False
        if key == 'hgt':
            if val[-2:] == 'in':
                if int(val[:-2]) < 59 or int(val[:-2]) > 76:
                    return False
            elif val[-2:] == 'cm':
                if int(val[:-2]) < 150 or int(val[:-2]) > 193:
                    return False
            else:
                return False
        if key == 'hcl':
            if not re.match(r'^#[0-9a-f]{6}$', val):
                return False
        if key == 'ecl':
            if not val in eye_colors:
                return False
        if key == 'pid':
            if not re.match(r'^[0-9]{9}$', val):
                return False
            
    return fields.issuperset(required_fields)


if __name__ == '__main__':
    main()
