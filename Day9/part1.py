def get_moves():
    file = open("Day9\input", mode='r').read().split()
    return [(d, int(s)) for d, s in zip(file[::2], file[1::2])]

def get_tail_visited_coordinates(moves):
    head, tail, visited_by_tail = [0, 0], [0, 0], {(0, 0): 1}
    for dir, times in moves:
        for _ in range(int(times)):
            head_prev_pos = head.copy()
            # Update head position
            if dir == 'U': head[1] += 1
            elif dir == 'D': head[1] -= 1
            elif dir == 'L': head[0] -= 1
            elif dir == 'R': head[0] += 1
            # Check if tail position needs update
            if max(tail[0], head[0]) - min(tail[0], head[0]) > 1 or max(tail[1], head[1]) - min(tail[1], head[1]) > 1:
                tail = head_prev_pos
                if (tail[0], tail[1]) not in visited_by_tail:
                    visited_by_tail[tail[0], tail[1]] = 1
                else:
                    visited_by_tail[tail[0], tail[1]] += 1
    return visited_by_tail


def main():
    visited_coord = get_tail_visited_coordinates(get_moves())
    print(len(visited_coord.keys()))

if __name__ == "__main__":
   main()