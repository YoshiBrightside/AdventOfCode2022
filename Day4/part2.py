ans, line = 0, input().split(',')
while(len(line) >= 2):
    sect1, sect2 = [int(x) for x in line[0].split('-')] , [int(x) for x in line[1].split('-')]
    if (sect1[0] >= sect2[0] and sect1[0] <= sect2[1]) or (sect2[0] >= sect1[0] and sect2[0] <= sect1[1]):
        ans +=1
    line = input().split(',')
print(ans)