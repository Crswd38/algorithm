import sys

str = sys.stdin.readline()
j = 0
result = ""

for i in str:
    if i.isalpha():
        j = ord(i)+13
        if j > 122:
            j -= 26
        elif j > 90 and j <= 103:
            j -= 26
        result += chr(j)
    else:
        result += i
print(result)