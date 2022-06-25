# 문제 풀이 방법
# 각 문장별로 입력 받은 후, 단어로 split 한 뒤 각 단어를 뒤집는다.

import sys
T = int(input())

for i in range(T):
    command = sys.stdin.readline().rstrip()
    words = list(command.split())
    reverse_word = []

    for word in words:
        reverse_word.append(word[::-1])

    answer = " ".join(reverse_word)
    print(answer)

# lstrip : 문자열에 왼쪽 공백이나 인자가된 문자열의 모든 조합을 제거
# rstrip : 문자열에 오른쪽 공백이나 인자가된 문자열의 모든 조합을 제거
# strip : 양쪽 문자열에 공백이나 인자가된 문자열의 모든 조합을 제거
