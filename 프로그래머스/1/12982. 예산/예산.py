def solution(d, budget):
    return sum(1 for i in sorted(d) if (budget := budget-i) >= 0) 
    