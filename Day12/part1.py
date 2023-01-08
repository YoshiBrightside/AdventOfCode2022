'''
Part 1 of Day 12, Hill Climbing Algorithm
https://adventofcode.com/2022/day/11
'''

from collections import deque

class Heightmap:

    def __init__(self, heightmap) -> None:
        self.heightmap = heightmap
        self.start = self.find_value('S')
        self._exit = self.find_value('E')

    def find_value(self, value):
        for i in range(len(self.heightmap)):
            for j in range(len(self.heightmap[0])):
                if self.heightmap == value:
                    # Save coords and replace S and E with respective elevation
                    self.heightmap[i][j] = 'a' if value == 'S' else 'z'
                    return i, j
        return None

    def find_shortest_path(self):
        shortest_path = {self._exit: 0}
        queue = deque([self._exit])
        shortest_path[self._exit[0]][self._exit[1]] = 0
        steps = 0
        next_queue = deque()
        while queue:
            coords = queue.popleft()
            shortest_path[coords] = steps
            possible_moves = ([(coords[0] + 1, coords[1]), (coords[0], coords[1] + 1),
                               (coords[0] - 1, coords[1]), (coords[0], coords[1] - 1)])
            for x, y in possible_moves:
                if self.are_valid_neightbours(coords[0], coords[1], x, y):
                    if (x, y) not in shortest_path:
                        shortest_path[(x, y)] = -1
                        next_queue.append((x, y))
            if not queue:
                queue = next_queue
                next_queue = deque()
        return shortest_path
    
    def are_valid_neightbours(self, x1, y1, x2, y2):
        if (x2 > 0 and x2 < self.heightmap and
            y2 > 0 and y1 < self.heightmap[0] and
            abs(ord(self.heightmap[x1][y1]) - ord(self.heightmap[x2][y2]) <= 1)):
            return True
        return False

    

def main():
    '''prints monke business'''
    monkes = make_monke_business(get_monkes(), 20)
    heapq.heapify(monkes)
    ans = heapq.nlargest(2, monkes)
    print(ans[0].items_thrown * ans[1].items_thrown)

if __name__ == "__main__":
    main()
