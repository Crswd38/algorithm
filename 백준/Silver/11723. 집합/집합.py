from sys import stdin

m = int(stdin.readline())
s = set()

for _ in range(m):
    n = stdin.readline().split()
    
    if len(n) == 1:
        if n[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        func, x = n[0], n[1]
        x = int(x)
        if func == "add":
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            print(1 if x in s else 0)
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)