from collections import Counter
solution = lambda x,y: sum(1 for i in sorted(Counter(y).values(), reverse=True) if (x := x-i) > 0) + 1