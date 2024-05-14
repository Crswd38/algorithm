def solution(id_pw, db):
    result = "fail"
    for i in range(len(db)):
        if id_pw[0] == db[i][0]:
            if id_pw[1] == db[i][1]:
                return "login"
            else:
                result = "wrong pw"
    return result
            
            