import math

def get_moves():
    file = open("Day9\input", mode='r').read().split()
    return [(d, int(s)) for d, s in zip(file[::2], file[1::2])]

def get_tail_visited_coordinates(moves, parts = 2):
    parts, visited_by_tail = [[0, 0] for _ in range(parts)], {(0, 0): 1}
    for dir, times in moves:
        for _ in range(int(times)):       
            # Update head position
            if dir == 'U': parts[0][1] += 1
            elif dir == 'D': parts[0][1] -= 1
            elif dir == 'L': parts[0][0] -= 1
            elif dir == 'R': parts[0][0] += 1
            # Update the following parts
            for p in range(1, len(parts)):
                head, tail = parts[p-1], parts[p]
                # Check if tail position needs update
                if max(tail[0], head[0]) - min(tail[0], head[0]) > 1 or max(tail[1], head[1]) - min(tail[1], head[1]) > 1:
                    # Move vertically/horizontally if head and tail are on the same collumn or row
                    if head[0] == tail[0] or head[1] == tail[1]:
                        motion = [int((math.copysign((max(tail[0], head[0]) - min(tail[0], head[0])) // 2, head[0]))),
                                  int((math.copysign((max(tail[1], head[1]) - min(tail[1], head[1])) // 2, head[1])))]
                    # Else move diagonally
                    else:
                        motion = [int((math.copysign((max(tail[0], head[0]) - min(tail[0], head[0])) // 2, head[0]))),
                                  int((math.copysign((max(tail[1], head[1]) - min(tail[1], head[1])) // 2, head[1])))]
                    tail[0] += motion[0]
                    tail[1] += motion[1]
                    if p != len(parts) -1: continue
                    if (tail[0], tail[1]) not in visited_by_tail:
                        visited_by_tail[tail[0], tail[1]] = 1
                # If tail doesn't need update, neither the following parts
                else: break
    print(parts)
    return visited_by_tail


def main():
    visited_coord = get_tail_visited_coordinates(get_moves(), parts = 10)
    for y in reversed(range(-6, 15)):
        s = []
        for x in range(-11, 15):
            s.append('#') if (x, y) in visited_coord else s.append('.')
        print(s)
    print(visited_coord.keys())
    print(len(visited_coord.keys()))

if __name__ == "__main__":
   main()