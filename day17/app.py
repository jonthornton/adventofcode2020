# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""

def main():
    input = []
    with open('input.txt', 'r') as file:
        input = [line.strip() for line in file]

    s = Solution()
    # print(s.part1(input))
    print(s.part2(input))

class Solution:
    def part1(self, input):

        active_blocks = set()

        x = 0
        y = 0
        z = 0
        for y, line in enumerate(input):
            for x, block in enumerate(line):
                if block == '#':
                    active_blocks.add((x, y, z))
        
        for i in range(6):
            # print(active_blocks)
            active_blocks = self.do_cycle(active_blocks)

        return len(active_blocks)

    def part2(self, input):

        active_blocks = set()

        x = 0
        y = 0
        z = 0
        w = 0
        for y, line in enumerate(input):
            for x, block in enumerate(line):
                if block == '#':
                    active_blocks.add((x, y, z, w))
        
        for i in range(6):
            # print(active_blocks)
            active_blocks = self.do_cycle_4d(active_blocks)

        return len(active_blocks)


    def do_cycle_4d(self, active_blocks):
        new_active = set()

        for block in active_blocks:
            if self.should_be_active_block_4d(block, active_blocks):
                new_active.add(block)

            neighbors = self.get_neighbors_4d(block)
            for n in neighbors:
                if self.should_be_active_block_4d(n, active_blocks):
                    new_active.add(n)

        return new_active

    def do_cycle(self, active_blocks):
        new_active = set()

        for block in active_blocks:
            if self.should_be_active_block(block, active_blocks):
                new_active.add(block)

            neighbors = self.get_neighbors(block)
            for n in neighbors:
                if self.should_be_active_block(n, active_blocks):
                    new_active.add(n)

        return new_active


    def should_be_active_block(self, block, active_blocks):
        is_active = block in active_blocks
        active_neighbors = self.get_active_neighbors(block, active_blocks)


        if is_active and 2 <= len(active_neighbors) <= 3:
            return True
        elif not is_active and len(active_neighbors) == 3:
            return True

        return False

    def should_be_active_block_4d(self, block, active_blocks):
        is_active = block in active_blocks
        active_neighbors = self.get_active_neighbors_4d(block, active_blocks)


        if is_active and 2 <= len(active_neighbors) <= 3:
            return True
        elif not is_active and len(active_neighbors) == 3:
            return True

        return False

    def get_active_neighbors(self, block, active_blocks):
        neighbors = self.get_neighbors(block)
        collector = []
        for n in neighbors:
            if n in active_blocks:
                collector.append(n)

        return collector

    def get_active_neighbors_4d(self, block, active_blocks):
        neighbors = self.get_neighbors_4d(block)
        collector = []
        for n in neighbors:
            if n in active_blocks:
                collector.append(n)

        return collector

    def get_neighbors(self, block):
        collector = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if x == 0 and y == 0 and z == 0:
                        continue

                    collector.append((block[0] + x, block[1] + y, block[2] + z))

        return collector

    def get_neighbors_4d(self, block):
        collector = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        if x == 0 and y == 0 and z == 0 and w == 0:
                            continue

                        collector.append((block[0] + x, block[1] + y, block[2] + z, block[3] + w))

        return collector

if __name__ == '__main__':
    main()
