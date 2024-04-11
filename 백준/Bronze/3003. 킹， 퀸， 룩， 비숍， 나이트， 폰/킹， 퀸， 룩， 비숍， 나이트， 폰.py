haveChess = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
text = []

for i in range(6):
    text.append(chess[i] - haveChess[i])

print(("".join(str(x)+" " for x in text)).strip())