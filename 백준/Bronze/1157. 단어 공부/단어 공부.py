str = input().lower()
alphabet = [0] * 26

for i in str:
        index = ord(i) - ord('a')
        alphabet[index] += 1

max = max(alphabet)
if alphabet.count(max) > 1:
    print('?')
else:
    max_index = alphabet.index(max)
    print(chr(max_index + ord('A')))