from collections import deque
import math

class Monke():
    '''Monke stuff.'''

    def __init__(self, items, _lambda, div_num, true_monke, false_monke) -> None:
        self.items = items
        self._lambda = _lambda
        self.div_num = div_num
        self.true_monke = true_monke
        self.false_monke = false_monke
        self.items_throwed = 0

    def __str__(self) -> str:
        return ('Monke(items: ' + str(self.items)
                    + ', lambda: ' + str(self._lambda)
                    + ', divisible by ' + str(self.div_num)
                    + ', if true throw to monke ' + str(self.true_monke)
                    + ', if false throw to monke ' + str(self.false_monke) + ')')

    def get_item(self, item):
        self.items.append(item)

    def throw_item(self, target_monke):
        target_monke.get_item(self.items.popleft())

    def inspect_item(self):
        item = math.floor((self._lambda(self.items.popleft())/3))
        self.items.appendleft(item)

    def throw_items(self):
        while self.items:
            item = self.items.popleft()
            item = self._lambda(item)
        item
        pass

def get_monkes():
    ans = []
    for monke in open("Day11\input", mode='r').read().split('\n\n'):
        monke_properties = monke.split('\n')
        items = deque(map(int, monke_properties[1].split(': ')[1].split(', ')))
        _lambda = eval('lambda old: ' + monke_properties[2].split('= ')[1])
        div_num = int(monke_properties[3].split('by')[1])
        true_monke = int(monke_properties[4].split('monkey')[1])
        false_monke = int(monke_properties[5].split('monkey')[1])
        ans.append(Monke(items, _lambda, div_num, true_monke, false_monke))
    return ans

def get_monke_business(monkes):
    return ' '

def main():
    monkes = get_monkes()
    get_monke_business(monkes)

if __name__ == "__main__":
   main()