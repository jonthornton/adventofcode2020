# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""

import re

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [line.strip() for line in file]

    s = Solution()

    # print(s.part1(input))
    print(s.part2(input))

class Solution:
    def part1(self, input):
        sum = 0
        for expression in input:
            sum += self.evaluate_expression(expression)
            # print(sum)

        return sum

    def part2(self, input):
        sum = 0
        for expression in input:
            sum += self.evaluate_expression2(expression)
            # print(sum)

        return sum

    def evaluate_no_parens_part1(self, expression):
        collector = self.next_number(expression, 0)
        for i, e in enumerate(expression):
            if e == '+':
                collector += self.next_number(expression, i)
            elif e == '*':
                collector *= self.next_number(expression, i)

        # print('evaluated', expression, 'to', collector)
        return collector


    def evaluate_expression(self, expression):

        while self.has_parens(expression):
            lindex = expression.index('(')
            rindex = self.get_closing_bracket(expression[lindex:], lindex)
            

            val = self.evaluate_expression(expression[lindex+1:rindex])
            start = '' if lindex == 0 else expression[:lindex-1]

            # print('old exp', expression)
            # print('new exp', start + str(val) + expression[rindex+1:])

            expression = start + str(val) + expression[rindex+1:]
        
        return self.evaluate_no_parens_part1(expression)

    def evaluate_expression2(self, expression):

        while self.has_parens(expression):
            lindex = expression.index('(')
            rindex = self.get_closing_bracket(expression[lindex:], lindex)
            

            val = self.evaluate_expression2(expression[lindex+1:rindex])
            start = '' if lindex == 0 else expression[:lindex-1]

            # print('old exp', expression)
            # print('new exp', start + str(val) + expression[rindex+1:])

            expression = start + str(val) + expression[rindex+1:]
        
        return self.evaluate_no_parens_part2(expression)

    def evaluate_no_parens_part2(self, expression):
        multiply_groups = expression.replace(' ', '').split('*')
        multiply_me = []
        # print(multiply_groups)
        for group in multiply_groups:
            sum_me = [int(x) for x in group.split('+')]
            # print(sum_me)
            multiply_me.append(sum(sum_me))

        collector = 1
        for num in multiply_me:
            collector *= num

        return collector

    def has_parens(self, expression):
        # print(expression)
        return '(' in expression

    def get_closing_bracket(self, expression, k):
        refs = 0
        for i, char in enumerate(expression):
            if char == '(':
                refs += 1
            elif char == ')':
                refs -= 1

            if refs == 0:

                return i + k

    def next_number(self, expression, i):
        r = re.findall(r'\d+', expression[i:])
        return int(r[0])



    

if __name__ == '__main__':
    main()
