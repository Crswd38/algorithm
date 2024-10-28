import sys

while True:
    N = int(sys.stdin.readline())

    if N == -1:
        break

    divisors = [i for i in range(1, N) if N % i == 0]

    if sum(i for i in divisors) == N:
        print(f"{N} = {' + '.join(str(i) for i in divisors)}")
    else:
        print(str(N) + " is NOT perfect.")