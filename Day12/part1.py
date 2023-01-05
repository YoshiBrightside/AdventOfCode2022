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
                    return i, j
        return None

    def find_shortest_path(self):
        ans = [[-1 for  _ in range(len(self.heightmap[0]))] for _ in range(len(self.heightmap))]
        seen = set([self._exit])
        queue = deque([self._exit])
        ans[self._exit[0]][self._exit[1]] = 0
        while queue:
            coords = queue.popleft()
            if coords[0] != -1:

            if
        return ans
        # uses deques to do a BFS starting from E

    

def main():
    '''prints monke business'''
    monkes = make_monke_business(get_monkes(), 20)
    heapq.heapify(monkes)
    ans = heapq.nlargest(2, monkes)
    print(ans[0].items_thrown * ans[1].items_thrown)

if __name__ == "__main__":
    main()
