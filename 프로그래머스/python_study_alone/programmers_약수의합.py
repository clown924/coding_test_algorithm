def solution(n):
    list1 = []
    answer = 0
    for i in range(1,n+1):
        if n % i == 0: # n % i == 0 이면 약수
            list1.append(i)
        else:
            continue
    for i in list1:
        answer += i
    return answer

print(solution(5))