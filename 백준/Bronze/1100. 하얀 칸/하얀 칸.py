arr = []
sum = 0
for i in range(8):
    arr.append(list(input()))
    for j in range(i%2, 8, 2):
        sum += int(arr[i][j] == "F")
print(sum)