'''
Part 1 of Day 14, Regolith Reservoir.
https://adventofcode.com/2022/day/14
'''

import math

def process_input():
    '''Reads file and creates a list of structures.'''
    structures = []
    for line in open("Day14\input", mode='r').read().split('\n'):
        if not line:
            return structures
        cur_structure = []
        for coords in line.split(' -> '):
            coord_x, coord_y = coords.split(',')
            cur_structure.append([int(coord_x), int(coord_y)])
        structures.append(cur_structure)
    return structures

def create_matrix(structures, min_max_coords):
    '''
    Create an appropiate matrix based on points of the structure.
    It is important to note that the y axis is inverted a.k.a. 0 is above 1.

    Each cell can contain the following values:

    0 for empty (represented below as a .)
    1 for rock (represented below as a #)
    2 for a sand (not represented below)

      0123456789
    0 ..........
    1 ..........
    2 ..........
    3 ..........
    4 ....#...##
    5 ....#...#.
    6 ..###...#.
    7 ........#.
    8 ........#.
    9 #########.
    '''
    left_x, right_x, bot_y, top_y = min_max_coords
    matrix = [[0 for _ in range(right_x - left_x)] for _ in range(bot_y - top_y)]
    for m in matrix:
        print(m)
    for structure in structures:
        for i in range(len(structure) - 2):
            print(i, structure[i], structure[i+1])
            if structure[i][0] == structure[i+1][0]:
                for j in range(min(structure[i][1], structure[i+1][1]), max(structure[i][1], structure[i+1][1])+1):
                    matrix[structure[i][0] - left_x][structure[i][1] + j] = 1
            else:
                for j in range(min(structure[i][0], structure[i+1][0]), max(structure[i][0], structure[i+1][0])+1): # 498,4 -> 498,6 -> 496,6
                     matrix[structure[i][0] - left_x + j][structure[i][1]] = 1
    return matrix

def get_min_max_coords(structures):
    '''
    Return the bottom leftmost and the top rightmost point.
    It is important to note that the y axis is inverted a.k.a. 0 is above 1.
    For a better example, see create_matrix example.
    '''
    left_x, right_x, bot_y, top_y = math.inf, -math.inf, -math.inf, 0
    for structure in structures:
        for coords in structure:
            left_x = min(left_x, coords[0])
            right_x = max(right_x, coords[0])
            bot_y = max(bot_y, coords[1])
            top_y = min(top_y, coords[1])
    return [left_x, right_x, bot_y, top_y]

def main():
    '''Returns the sum of the indices of the pairs in the right order.'''
    structures = process_input()
    min_max_coords = get_min_max_coords(structures)
    matrix = create_matrix(structures, min_max_coords)
    for line in matrix:
        print(line)

if __name__ == "__main__":
    main()