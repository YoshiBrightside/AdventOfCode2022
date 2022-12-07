from collections import deque

# get_crates() breaks if over 9 columns. Good thing we don't have those lol.
def get_crates():
    line = input()
    crates = [deque() for _ in range(len(line) // 4 + 1)] # Calculate crate columns by line length
    while (line[1] != '1'): # If we reach 1 on index 1 it means we finished geting crates input
        for i in range(len(crates)):
            crate = line[i * 4 + 1]
            if crate != ' ':
                crates[i].appendleft(crate)
        line = input()
    input() # Final empty line
    return crates

def move_crates(crates):
    line = input().split(' ')
    while (line[0]):
        for _ in range(int(line[1])):
            crates[(int(line[5]) - 1)].append(crates[(int(line[3]) - 1)].pop())
        line = input().split(' ')
    return crates

def main():
    crates = get_crates()
    crates = move_crates(crates)
    ans = [crates[x][-1] for x in range(len(crates))]
    print(''.join(ans))

if __name__ == "__main__":
   main()