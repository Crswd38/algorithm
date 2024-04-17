def solution(age):
    result = []
    age = str(age)
    l = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    for k in range(len(age)):
        for n, m in l.items():
            if age[k] == n:
                result.append(m)
    return ''.join(result)