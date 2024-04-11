T = int(input())

for _ in range(T):
    R,S = input().split()
    list = []
    for x in S:
        for _ in range(int(R)):
            list.append(x)
    print(''.join(list))