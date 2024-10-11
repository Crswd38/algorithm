def solution(babbling):
    for i in range(len(babbling)):
        while True:
            if babbling[i][:3] == 'aya':
                if babbling[i][3:6] == 'aya':
                    break
                babbling[i] = babbling[i][3:]
                continue
            elif babbling[i][:2] == "ye":
                if babbling[i][2:4] == "ye":
                    break
                babbling[i] = babbling[i][2:]
                continue
            elif babbling[i][:3] == "woo":
                if babbling[i][3:6] == "woo":
                    break
                babbling[i] = babbling[i][3:]
                continue
            elif babbling[i][:2] == "ma":
                if babbling[i][2:4] == "ma":
                    break
                babbling[i] = babbling[i][2:]
                continue
            else:
                break

    return sum(1 for i in babbling if i == "")