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
        self.items_thrown = 0

    def __str__(self) -> str:
        return ('Monke(items: ' + str(self.items)
                    + ', lambda: ' + str(self._lambda)
                    + ', divisible by ' + str(self.div_num)
                    + ', if true throw to monke ' + str(self.true_monke)
                    + ', if false throw to monke ' + str(self.false_monke)
                    + ', items thrown ' + str(self.items_thrown) + ')')

    def get_item(self, item):
        '''Appeds item to monke.'''
        self.items.append(item)

    def test_is_true(self):
        '''Tests wether or not first item is divisible by div_num.'''
        return self.items[0] % self.div_num == 0

    def throw_item(self, target_monke):
        '''Throw first item to target monke.'''
        target_monke.get_item(self.items.popleft())
        self.items_thrown += 1

    def inspect_item(self):
        '''Inspects first element, increasing worry levels, then
        dividing it by three and returning the floor.'''
        item = math.floor((self._lambda(self.items.popleft())/3))
        self.items.appendleft(item)

    def throw_items(self, monkes):
        '''Inspect, test and throw each item the monke has.'''
        while self.items:
            self.inspect_item()
            target_monke = self.true_monke if self.test_is_true() else self.false_monke
            self.throw_item(monkes[target_monke])

def start_round(monkes):
    '''Makes each monke throw its items.'''
    for monke in monkes:
        monke.throw_items(monkes)

def get_monkes():
    '''Reads monkes to input and returns a double ended queue of monkes.'''
    monkes = []
    for monke in open("Day11\input", mode='r').read().split('\n\n'):
        monke_properties = monke.split('\n')
        items = deque(map(int, monke_properties[1].split(': ')[1].split(', ')))
        _lambda = eval('lambda old: ' + monke_properties[2].split('= ')[1])
        div_num = int(monke_properties[3].split('by')[1])
        true_monke = int(monke_properties[4].split('monkey')[1])
        false_monke = int(monke_properties[5].split('monkey')[1])
        monkes.append(Monke(items, _lambda, div_num, true_monke, false_monke))
    return monkes

def get_monke_business(monkes, rounds):
    '''prints each monke after a specific amount of rounds.'''
    for _ in range(rounds):
        start_round(monkes)
    for monke in monkes:
        print(str(monke))

def main():
    '''prints monke business'''
    monkes = get_monkes()
    get_monke_business(monkes, 20)

if __name__ == "__main__":
    main()
