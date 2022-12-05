ans, line = 0, input()
while(line):
    seen = {}
    for i in range(len(line)//2):
        if line[i] not in seen:
            seen[line[i]] = True
    for i in range(len(line)//2, len(line)):
        if line[i] in seen:
            val = ord(line[i]) - 38 if line[i].isupper() else ord(line[i]) - 96
            ans += val
            break
    line = input()
print(ans)