import sys

N, K = map(int, sys.stdin.readline().split())
josephus = [i for i in range(1,N+1)]

answer = []
num = 0

for t in range(N):
    num += K-1
    if num >= len(josephus):  
        num = num%len(josephus)
 
    answer.append(str(josephus.pop(num)))
print("<",", ".join(answer)[:],">", sep='')