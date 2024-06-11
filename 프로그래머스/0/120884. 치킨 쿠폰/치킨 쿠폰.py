def solution(chicken):
    a = 0
    service = 0
    while chicken >= 10:
        service += chicken // 10
        a = chicken % 10
        chicken = chicken // 10
        chicken += a
    return service