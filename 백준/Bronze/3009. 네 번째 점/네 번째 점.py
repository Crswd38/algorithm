import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
e, f = map(int, sys.stdin.readline().split())

if(a == c):
    print(e, end=" ")
if(a == e):
    print(c, end=" ")
if(c == e):
    print(a, end=" ")

if(b == d):
    print(f, end=" ")
if(b == f):
    print(d, end=" ")
if(d == f):
    print(b, end=" ")