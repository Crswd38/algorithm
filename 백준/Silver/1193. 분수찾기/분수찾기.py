X = int(input())

line = 1  # 현재 대각선 라인
while X > line:
    X -= line
    line += 1

# 홀수번째 라인인 경우 분자가 큰 수에서 시작, 짝수번째 라인인 경우 분모가 큰 수에서 시작
if line % 2 == 0:
    numerator = X  # 분자
    denominator = line - X + 1  # 분모
else:
    numerator = line - X + 1  # 분자
    denominator = X  # 분모

print(f"{numerator}/{denominator}")