def get_program():
    return open("Day10\input", mode='r').read().split()

def get_signal_strengths(program, interesting_cycles):
    x, ans = 1, []
    for l in range(len(program)):
        if l + 1 in interesting_cycles:
            ans.append(x * (l + 1))
        try: x += int(program[l])
        except: continue
    return ans

def main():
    ans = get_signal_strengths(get_program(), [20, 60, 100, 140, 180, 220])
    print(sum(ans))

if __name__ == "__main__":
   main()