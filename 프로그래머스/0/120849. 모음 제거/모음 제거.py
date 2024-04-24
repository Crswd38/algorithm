def solution(my_string):
    my_string = list(my_string)
    for _ in range(len(my_string)):
        if "a" in my_string:
            my_string.remove("a")
        elif "e" in my_string:
            my_string.remove("e")
        elif "i" in my_string:
            my_string.remove("i")
        elif "o" in my_string:
            my_string.remove("o")
        elif "u" in my_string:
            my_string.remove("u")
    return ''.join(my_string)