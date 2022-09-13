# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

N = int(input())

for i in range(2,N):
    if N == 1:
        break
    while (N % i == 0):
        print(i)
        N = N / i
