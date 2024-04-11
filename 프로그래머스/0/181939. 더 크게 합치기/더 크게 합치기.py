def solution(a, b):
    
    if  int(str(a)+str(b)) >= int(str(b)+str(a)):
        return int(str(a)+str(b))
    elif  int(str(a)+str(b)) < int(str(b)+str(a)):
        return int(str(b)+str(a))