def solution(a, b):
    dates = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    return week[(sum(dates[:a]) + b - 1) % 7]