def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:
        result = ''
        for j in range(len(word)):
            if j % 2 == 1 :
                result += word[j].lower()
            else:
                result += word[j].upper()
        answer.append(result)
    return ' '.join(answer)