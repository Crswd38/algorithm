num = input()
sum = 0

for i in range(len(num)):
    if('A' == num[i] or 'B' == num[i] or 'C' == num[i]):
        sum += 3
    elif('D' == num[i] or 'E' == num[i] or 'F' == num[i]):
        sum += 4
    elif('G' == num[i] or 'H' == num[i] or 'I' == num[i]):
        sum += 5
    elif('J' == num[i] or 'K' == num[i] or 'L' == num[i]):
        sum += 6
    elif('M' == num[i] or 'N' == num[i] or 'O' == num[i]):
        sum += 7
    elif('P' == num[i] or 'Q' == num[i] or 'R' == num[i] or 'S' == num[i]):
        sum += 8
    elif('T' == num[i] or 'U' == num[i] or 'V' == num[i]):
        sum += 9
    elif('W' == num[i] or 'X' == num[i] or 'Y' == num[i] or 'Z' == num[i]):
        sum += 10
print(sum)