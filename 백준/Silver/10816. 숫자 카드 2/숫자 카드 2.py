import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
list1 = list(map(int, sys.stdin.readline().split()))
list1_count = Counter(list1)
M = int(sys.stdin.readline().strip())
list2 = list(map(int, sys.stdin.readline().split()))


result = [str(list1_count[num]) for num in list2]

print(' '.join(result))