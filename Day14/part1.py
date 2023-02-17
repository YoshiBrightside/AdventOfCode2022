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
    matrix = [[0 for _ in range(right_x - left_x + 1)] for _ in range(bot_y - top_y + 1)]
    for structure in structures:
        for i in range(len(structure) - 1):
            if structure[i][0] == structure[i+1][0]:
                point_start = min(structure[i][1], structure[i+1][1])
                point_end = max(structure[i][1], structure[i+1][1])
                for j in range(point_start, point_end+1):
                    matrix[j][structure[i][0] - left_x] = 1
            else:
                point_start = min(structure[i][0], structure[i+1][0])
                point_end = max(structure[i][0], structure[i+1][0])
                for j in range(point_start, point_end+1):
                    matrix[structure[i][1]][j - left_x] = 1
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

def add_sand(matrix, starting_point):
    return [-1, -1] # temp to avoid infinite loops
    if matrix[0][starting_point] != 0:
        return [-1, -1]
    return 1

def fill(matrix, offset = None):
    '''
    Fills given matrix with sand. Sand falls at point 500 without considering
    matrix offset. Returns how many units of sand are placed before falling
    outside the matrix.
    '''
    ans = 0
    starting_point = 500 if offset is None else 500 - offset[0]
    while add_sand(matrix, starting_point) != [-1, -1]:
        ans += 1
    return ans



def main():
    '''Returns the sum of the indices of the pairs in the right order.'''
    structures = process_input()
    min_max_coords = get_min_max_coords(structures)
    matrix = create_matrix(structures, min_max_coords)
    for line in matrix:
        print(line)
    print(fill(matrix, offset=min_max_coords))

if __name__ == "__main__":
    main()
