'''
Part 1 of Day 12, Hill Climbing Algorithm
https://adventofcode.com/2022/day/11
'''

import ast

def get_signal():
    '''Reads signal packages and pass it as lists of list.'''
    signal = []
    for line in open("Day13\input", mode='r').read().split('\n'):
        if line:
            signal.append(ast.literal_eval(line))
    return signal

def evaluate_packets(pckt1, pckt2):
    for i in range(max(len(pckt1), len(pckt2))):
        if len(pckt1) == i: return True
        if len(pckt2) == i: return False
        if type(pckt1[i]) == int and type(pckt2[i]) == int:
            if pckt1[i] < pckt2[i]: return True
            if pckt1[i] > pckt2[i]: return False
        if type(pckt1[i]) == list or type(pckt2[i]) == list:
            if type(pckt1[i]) != list: pckt1[i] = [pckt1[i]]
            if type(pckt2[i]) != list: pckt2[i] = [pckt2[i]]
            ans = evaluate_packets(pckt1[i], pckt2[i])
            if ans is not None: return ans
    return None

def correct_pairs_indices(signal):
    ans = []
    for i in range(0, len(signal), 2):
        pckt1, pckt2 = signal[i], signal[i+1]
        if evaluate_packets(pckt1, pckt2):
            ans += [i//2+1]
    return ans


def main():
    signal = get_signal()
    ans = correct_pairs_indices(signal)
    print(sum(ans))

if __name__ == "__main__":
    main()
