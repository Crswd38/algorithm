import sys

while(True):
    try:
        A, B = sys.stdin.readline().rstrip().split()
        print(int(A)+int(B))
    except:
        break