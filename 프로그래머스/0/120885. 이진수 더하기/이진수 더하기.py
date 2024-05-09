def solution(bin1, bin2):
    return bin(int("0b"+bin1, 2) + int("0b"+bin2, 2))[2:]