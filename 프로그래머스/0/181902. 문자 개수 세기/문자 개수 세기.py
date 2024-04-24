def solution(my_string):
    arr = [0]*52
    for i in my_string:
        if i.isupper():
            arr[ord(i) - 65] += 1
        else:
            arr[ord(i) - 71] += 1
    return arr