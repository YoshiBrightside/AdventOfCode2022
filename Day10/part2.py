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

def print_crt_image(program, pix_per_line):
    x, cur_line, ans = 1, [], []
    for l in range(len(program)):
        if l % pix_per_line >= x-1 and l % pix_per_line < x+2: cur_line.append('#')
        else: cur_line.append('.')
        if l % pix_per_line == 39:
            ans.append(cur_line)
            cur_line = []
        try: x += int(program[l])
        except: continue
    return ans

def main():
    ans = print_crt_image(get_program(), 40)
    for line in ans:
        print(''.join(line))

if __name__ == "__main__":
   main()