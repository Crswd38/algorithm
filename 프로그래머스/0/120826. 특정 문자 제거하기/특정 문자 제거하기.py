def solution(my_string, letter):
    return my_string.translate({ord(letter): None})