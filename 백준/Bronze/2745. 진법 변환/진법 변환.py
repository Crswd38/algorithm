N, B = input().split()
N = N[::-1]
result = 0

for i in range(len(N)):
    if(N[i].isdigit()):
        result += (int(N[i])) * (int(B) ** i)
    else:
        result += (ord(N[i])-55) * (int(B) ** i)
print(result)