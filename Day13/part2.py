'''
Part 2 of Day 13, Distress Signal
https://adventofcode.com/2022/day/13
'''

from functools import cmp_to_key
import ast

def get_signal():
    '''Reads signal packages and pass it as lists of list.'''
    signal = []
    for line in open("Day13\input", mode='r').read().split('\n'):
        if line:
            signal.append(ast.literal_eval(line))
    return signal

def get_divider_packets():
    '''Returns list of divider packets.'''
    return [[[2]], [[6]]]

def evaluate_packets(pckt1, pckt2):
    '''Compare packets and returns if pckt1 is less than pckt2.'''
    for i in range(max(len(pckt1), len(pckt2))):
        if len(pckt1) == i:
            return -1
        if len(pckt2) == i:
            return 1
        if isinstance(pckt1[i], int) and isinstance(pckt2[i], int):
            if pckt1[i] < pckt2[i]:
                return -1
            if pckt1[i] > pckt2[i]:
                return 1
        if isinstance(pckt1[i], list) or isinstance(pckt2[i], list):
            e1 = pckt1[i] if isinstance(pckt1[i], list) else [pckt1[i]]
            e2 = pckt2[i] if isinstance(pckt2[i], list) else [pckt2[i]]
            ans = evaluate_packets(e1, e2)
            if ans != 0:
                return ans
    return 0

def correct_pairs_indices(signal):
    '''Returns the list of pairs in the right order.'''
    ans = []
    for i in range(0, len(signal), 2):
        pckt1, pckt2 = signal[i], signal[i+1]
        if evaluate_packets(pckt1, pckt2):
            ans += [i//2+1]
    return ans

def main():
    '''Returns the sum of the indices of the pairs in the right order.'''
    signal = get_signal()
    signal += get_divider_packets()
    signal.sort(key=cmp_to_key(evaluate_packets))
    print((signal.index([[2]]) + 1)*(signal.index([[6]]) + 1))

if __name__ == "__main__":
    main()
