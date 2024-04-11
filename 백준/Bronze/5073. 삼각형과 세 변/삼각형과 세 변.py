import sys

while(True):
    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
    if(num[0]==0 and num[1]==0 and num[2]==0):
        break
    if(num[0] == num[1] and num[1] == num[2] and num[2] == num[0]):
        print("Equilateral")
    elif(num[0]+num[1] <= num[2]):
        print("Invalid")
    elif(num[0] == num[1] or num[0] == num[2] or num[1] == num[2]):
        print("Isosceles")
    elif(num[0] != num[1] or num[0] != num[2] or num[1] != num[2]):
        print("Scalene")