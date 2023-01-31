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
    '''Compare packets and returns if they are in the right order.'''
    for i in range(max(len(pckt1), len(pckt2))):
        if isinstance(pckt1[i], int) and isinstance(pckt2[i], int):
            if pckt1[i] < pckt2[i]:
                return True
            if pckt1[i] > pckt2[i]:
                return False
        if isinstance(pckt1[i], list) or isinstance(pckt2[i], list):
            if not isinstance(pckt1[i], list):
                pckt1[i] = [pckt1[i]]
            if not isinstance(pckt2[i], list):
                pckt2[i] = [pckt2[i]]
            ans = evaluate_packets(pckt1[i], pckt2[i])
            if ans is not None:
                return ans
    return None

def correct_pairs_indices(signal):
    '''Returns the list of pairs in the right order.'''
    ans = []
    for i in range(0, len(signal), 2):
        pckt1, pckt2 = signal[i], signal[i+1]
        if evaluate_packets(pckt1, pckt2):
            ans += [i//2+1]
    return ans

def flatten_packet(pckt):
    ans = []
    for e in pckt:
        if isinstance(e, list):
            ans += flatten_packet(e)
        else:
            ans.append(e)
    return ans

def compare_packets(pckt1, pckt2):
    '''Bad comparator'''
    flat_pckt1, flat_pckt2 = flatten_packet(pckt1), flatten_packet(pckt2)
    if not flat_pckt1 and not flat_pckt2:
        depth1, depth2 = pckt1, pckt2
        while depth1 or depth2:
            if not depth1: return -1
            if not depth2: return 1
            depth1, depth2 = depth1[0], depth2[0]
    for i in range(max(len(flat_pckt1), len(flat_pckt2))):
        if i >= len(flat_pckt1):
            return -1
        if i >= len(flat_pckt2):
            return 1
        if flat_pckt1[i] > flat_pckt2[i]:
            return 1
        if flat_pckt1[i] < flat_pckt2[i]:
            return -1
    return 0

def main():
    '''Returns the sum of the indices of the pairs in the right order.'''
    signal = get_signal()
    signal += get_divider_packets()
    signal.sort(key=cmp_to_key(compare_packets))
    for s in signal: print(s)
    print((signal.index([[2]])+1)*(signal.index([[6]])+1))
    #for s in signal: print(s)

if __name__ == "__main__":
    main()
