ans, line, line_num = 0, input(), 0
while(line):
    if line_num % 3 == 0:
        seen = {}
        for i in range(len(line)):
            if line[i] not in seen:
                seen[line[i]] = 1
    if line_num % 3 == 1:
        for i in range(len(line)):
            if line[i] in seen:
                seen[line[i]] = 2
    if line_num % 3 == 2:
        for i in range(len(line)):
            if line[i] in seen and seen[line[i]] == 2:
                val = ord(line[i]) - 38 if line[i].isupper() else ord(line[i]) - 96
                ans += val
                break
    line, line_num = input(), line_num + 1
print(ans)