# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os
import math
from collections import defaultdict

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [line.strip() for line in file]

    s = Solution()
    # print(s.part1(input))
    print(s.part2(input))

class Solution:
    def part1(self, input):
        rules, your_ticket, nearby_tickets = self.parse_input(input)

        invalid = []

        for ticket in nearby_tickets:
            fields = self.get_invalid_fields(ticket, rules)
            invalid += fields
            print(invalid)


        return sum(invalid)

    def is_valid_ticket(self, ticket, rules):
        return len(self.get_invalid_fields(ticket, rules)) == 0

    def get_invalid_fields(self, ticket, rules):
        return list(filter(lambda x: not self.is_valid_for_any_rule(rules, x), ticket))

    def is_valid_for_any_rule(self, rules, value):
        return any([self.is_valid_for_rule(rules[x], value) for x in rules])

    def is_valid_for_rule(self, rule, value):
        for r in rule:
            if r[0] <= value <= r[1]:
                return True

        return False

    def reduce_index_hits(self, index_hits):
        if len(index_hits) == 1:
            for field in index_hits:
                return { field: index_hits[field][0] }

        for field in index_hits:
            if len(index_hits[field]) == 1:
                val, new_index_hits = self.reduce_index_hits_helper(field, index_hits)
                out = self.reduce_index_hits(index_hits)
                out[field] = val
                return out

        print(index_hits)

    def reduce_index_hits_helper(self, field, index_hits):
        val = index_hits[field][0]
        del index_hits[field]
        for f in index_hits:
            index_hits[f] = list(filter(lambda x: x != val, index_hits[f]))

        return val, index_hits


    def part2(self, input):

        rules, your_ticket, nearby_tickets = self.parse_input(input)

        tickets_filtered = list(filter(lambda x: self.is_valid_ticket(x, rules), nearby_tickets))
        # print(tickets_filtered)
        # print(tickets_filtered)
        tickets_rotated = list(zip(*tickets_filtered[::-1]))
        # print(tickets_rotated)

        index_hits = defaultdict(list)
        for rule_field in rules:
            for i, ticket_field in enumerate(tickets_rotated):
                if all([self.is_valid_for_rule(rules[rule_field], x) for x in ticket_field]):
                    index_hits[rule_field].append(i)

        ticket_field_indexes = self.reduce_index_hits(index_hits)


        collector = []
        for field in ticket_field_indexes:
            if field.startswith('departure'):
                idx = ticket_field_indexes[field]
                value = your_ticket[idx]
                collector.append(value)
                # print(field, value)

        print(collector)
        # print(ticket_field_indexes)
        out = 1
        for x in collector:
            out *= x
        
        return out


    def parse_input(self, input):
        rules = {}
        your_ticket = ''
        nearby_tickets = []

        parse_next = ''
        for line in input:
            if ': ' in line:
                [key, ranges] = self.parse_rule(line)
                rules[key] = ranges
                continue

            if line == 'your ticket:' or line == 'nearby tickets:':
                parse_next = line
                continue

            if parse_next == 'nearby tickets:':
                ticket = [int(x) for x in line.split(',')]
                nearby_tickets.append(ticket)
                continue

            if parse_next == 'your ticket:':
                your_ticket = [int(x) for x in line.split(',')]
                parse_next = ''
                continue

        return rules, your_ticket, nearby_tickets

    def parse_rule(self, line):
        [key, val] = line.split(': ')

        ranges_str = val.split(' or ')
        ranges = []
        for r in ranges_str:
            r2 = tuple([int(x) for x in r.split('-')])
            ranges.append(r2)

        return key, ranges



if __name__ == '__main__':
    main()
