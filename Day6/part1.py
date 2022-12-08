def detect_start_of_packet(s):
    ans = -1
    cur_seq = {} # Storing the number of appearances inside our sequence
    for i in range(len(s)):
        if i >= 4:
            if cur_seq[s[i - 4]] == 1:
                cur_seq.pop(s[i - 4])
            else:
                cur_seq[s[i - 4]] -= 1
        if s[i] in cur_seq:
            cur_seq[s[i]] += 1
        else:
            cur_seq[s[i]] = 1
        if len(cur_seq) == 4:
            ans = i + 1
            break
    return ans
        

def main():
    print(detect_start_of_packet(input()))

if __name__ == "__main__":
   main()