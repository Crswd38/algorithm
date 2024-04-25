def solution(numbers):
    result = []
    while(len(numbers) != 0):
        if numbers[0:4] == "zero":
            result.append("0")
            numbers = numbers[4:]
        elif numbers[0:3] == "one":
            result.append("1")
            numbers = numbers[3:]
        elif numbers[0:3] == "two":
            result.append("2")
            numbers = numbers[3:]
        elif numbers[0:5] == "three":
            result.append("3")
            numbers = numbers[5:]
        elif numbers[0:4] == "four":
            result.append("4")
            numbers = numbers[4:]
        elif numbers[0:4] == "five":
            result.append("5")
            numbers = numbers[4:]
        elif numbers[0:3] == "six":
            result.append("6")
            numbers = numbers[3:]
        elif numbers[0:5] == "seven":
            result.append("7")
            numbers = numbers[5:]
        elif numbers[0:5] == "eight":
            result.append("8")
            numbers = numbers[5:]
        elif numbers[0:4] == "nine":
            result.append("9")
            numbers = numbers[4:]
    return int(''.join(result))