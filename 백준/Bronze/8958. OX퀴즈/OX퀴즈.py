t = int(input())
for _ in range(t):
    n = input().split('X')
    print(sum([len(i)*(len(i)+1)//2 for i in n]))