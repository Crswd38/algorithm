def solution(food):
    arr = [str(i) for i in range(1, len(food)) for j in range(food[i]//2)]
    return ''.join(arr) + "0" + ''.join(arr[::-1])