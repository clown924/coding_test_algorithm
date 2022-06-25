def solution(n):
    answer = ''
    while n >= 1 :
        if n % 2 == 1 :
            answer += "수"
            n -= 1
        else :
            answer += "박"
            n -= 1
    return answer[::-1]

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0 :
            answer += "수"
        else :
            answer += "박"
    return answer