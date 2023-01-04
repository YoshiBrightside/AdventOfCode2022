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
        seen = set()
        # uses deques to do a BFS starting from E

    

def main():
    '''prints monke business'''
    monkes = make_monke_business(get_monkes(), 20)
    heapq.heapify(monkes)
    ans = heapq.nlargest(2, monkes)
    print(ans[0].items_thrown * ans[1].items_thrown)

if __name__ == "__main__":
    main()
