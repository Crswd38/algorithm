str = input()
sum = 0

for i in range(len(str)):
    sum +=  1
    if(str[i:i+2] == "c=" or str[i:i+2] == "c-"):
        sum -= 1
    if(str[i:i+3] == "dz=" or str[i:i+2] == "d-"):
        sum -= 1
    if(str[i:i+2] == "lj"):
        sum -= 1
    if(str[i:i+2] == "nj"):
        sum -= 1
    if(str[i:i+2] == "s="):
        sum -= 1
    if(str[i:i+2] == "z="):
        sum -= 1

print(sum)