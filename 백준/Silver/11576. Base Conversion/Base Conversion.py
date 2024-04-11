import string
import sys

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r] 
    else:
        return convert(q, base) + tmp[r]

A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
sum = 0
result = ""

for i in range(m):
    sum += number[len(number)-i-1] * A ** i

sum = convert(sum, B)
for i in str(sum):
    if i.isalpha():
        i = ord(i) - 87
    result += str(i) + " "

print(result.strip())