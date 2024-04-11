list = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        try:
            if(list[i][j] != None):
                print(list[i][j], end="")
        except:
            pass