def solution(data, ext, val_ext, sort_by):
	di = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
	arr = []
	for i in data:
		if i[di[ext]] < val_ext:
			arr.append(i)
	return sorted(arr, key=lambda x : x[di[sort_by]])