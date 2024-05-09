def solution(myString):
    return ''.join(["l" if ord(i) < 108 else i for i in myString])
    