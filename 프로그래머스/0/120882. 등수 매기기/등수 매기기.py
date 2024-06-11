def solution(score):
	averages = [sum(s) for s in score]
	sorted_averages = sorted(averages, reverse=True)
	ranks = [sorted_averages.index(a) + 1 for a in averages]
	return ranks
