import sys

N = int(sys.stdin.readline())
result = []
last = 0
num = []
stack = []

for i in range(N):
    num.append(int(sys.stdin.readline())) # num = 4,3,6,8,7,5,2,1

for i in num:
    if last < i:
        for j in range(last, i):
            result.append("+\n")
            stack.append(j+1)
        last = i
        stack.pop()
        result.append("-\n")
    elif i == stack.pop():
        result.append("-\n")
    else:
        result.clear()
        result.append("NO")
        break
print(''.join(result))
