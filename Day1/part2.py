import heapq as hq

ans, cur_cal = [0, 0, 0], 0
while(True):
    line = input()
    if not line:
        hq.heappushpop(ans, cur_cal)
        cur_cal = 0
        line = input()
        if not line:
            break
    cur_cal += int(line)
print(sum(ans))