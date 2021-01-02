# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

rules = {}

def main():
    with open('input.txt', 'r') as file:
        for line in file:
            # clean up
            line = line.replace(' bags', '').replace(' bag', '').strip('\n .')

            [subject, predicate] = line.split(' contain ')
            rules[subject] = {}
            if predicate != 'no other':
                other_bags = predicate.split(', ')
                for other_bag in other_bags:
                    [count, bag] = other_bag.split(' ', 1)
                    rules[subject][bag] = int(count)
    print(rules)
    # print(len(can_contain('shiny gold')))
    print(count_contains('shiny gold'))

def count_contains(search_bag):
    count = 0

    for bag in rules[search_bag]:
        print(bag, count_contains(bag))
        count += rules[search_bag][bag] + (rules[search_bag][bag] * count_contains(bag))

    return count

def can_contain(search_bag):
    collector = set()

    for target_bag in rules:
        if search_bag in rules[target_bag]:
            collector.add(target_bag)
            # print(target_bag, can_contain(target_bag))
            collector = collector.union(can_contain(target_bag))

    return collector


if __name__ == '__main__':
    main()
