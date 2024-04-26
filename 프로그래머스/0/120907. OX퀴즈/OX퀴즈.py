def solution(quiz):
    for i in range(len(quiz)):
        quiz[i] = quiz[i].replace('=', '==')
        if eval(quiz[i]):
            quiz[i] = "O"
        else:
            quiz[i] = "X"
    return quiz