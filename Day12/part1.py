class Heightmap:

    def __init__(self, heightmap) -> None:
        self.heightmap = heightmap
        self.min_steps = self.get_min_steps()

    def get_min_steps(self):
        for i in self.heightmap:
            for j in self.heightmap[0]:
                if self.min_steps[i][j] == -1

def find_shortest_path():
    

def main():
    '''prints monke business'''
    monkes = make_monke_business(get_monkes(), 20)
    heapq.heapify(monkes)
    ans = heapq.nlargest(2, monkes)
    print(ans[0].items_thrown * ans[1].items_thrown)

if __name__ == "__main__":
    main()
