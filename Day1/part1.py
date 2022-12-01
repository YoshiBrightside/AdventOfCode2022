ans, cur_cal = 0, 0
while(True):
    line = input()
    if not line:
        cur_cal = 0
        line = input()
        if not line:
            break
    cur_cal += int(line)
    ans = max(ans, cur_cal)
print(ans)