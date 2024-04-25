n = input()
result = []
for i in range(int(n)):
    result.append(input())
for i in sorted(list(set(result)), key = lambda x:(len(x), x)):
    print(i)
