def solution(name, yearning, photo):
    yearname = {}
    result = []
    for i in range(len(name)):
        yearname[name[i]] = yearning[i]
    for i in photo:
        result.append(sum(yearname[j] for j in i if j in name))
    return result