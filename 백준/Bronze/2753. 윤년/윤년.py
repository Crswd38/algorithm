A = input()

A = int(A)

if(A % 4 == 0):
    if(A % 100 != 0):
        print(1)
    else:
        if(A % 400 == 0):
            print(1)
        else:
            print(0)
else:
    print(0)