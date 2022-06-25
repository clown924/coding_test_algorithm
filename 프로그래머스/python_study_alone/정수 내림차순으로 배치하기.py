def solution(n):
    answer = 0
    list1 = []
    for i in str(n):
        list1.append(i)
    list1.sort()
    list1.reverse()
    answer = int("".join(list1))
    return answer
