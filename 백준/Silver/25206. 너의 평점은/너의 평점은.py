sum = 0
sum2 = 0

for _ in range(20):
    c,b,a = input().split()
    b = float(b)
    if(a == "A+"):
        sum += 4.5*b
        sum2 += b
    elif(a == "A0"):
        sum += 4.0*b
        sum2 += b
    elif(a == "B+"):
        sum += 3.5*b
        sum2 += b
    elif(a == "B0"):
        sum += 3.0*b
        sum2 += b
    elif(a == "C+"):
        sum += 2.5*b
        sum2 += b
    elif(a == "C0"):
        sum += 2.0*b
        sum2 += b
    elif(a == "D+"):
        sum += 1.5*b
        sum2 += b
    elif(a == "D0"):
        sum += 1.0*b
        sum2 += b
    elif(a == "F"):
        sum += 0.0*b
        sum2 += b
    elif(a == "P"):
        pass

print(sum/sum2)