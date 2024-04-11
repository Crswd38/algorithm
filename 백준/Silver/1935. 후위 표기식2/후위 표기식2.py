import sys

N = int(sys.stdin.readline().strip())
postfix_expression = sys.stdin.readline().strip()
stack=[]
alpha = []

for i in range(N):
    alpha.append(int(sys.stdin.readline().strip()))

for i in postfix_expression:
    if i.isalpha():
        stack.append(alpha[ord(i)-65])
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)

print(f"{stack[0]:.2f}")