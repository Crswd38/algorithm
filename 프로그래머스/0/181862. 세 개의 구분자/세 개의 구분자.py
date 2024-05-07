def solution(myStr):
    myStr = (' ').join(myStr.split("a"))
    myStr = (' ').join(myStr.split("b"))
    myStr = (' ').join(myStr.split("c"))
    myStr = myStr.split()
    return myStr if myStr != [] else ["EMPTY"]