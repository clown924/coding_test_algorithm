# 수열 A가 주어졌을 때, 가장 긴 증가하는
# 부분 수열을 구하는 프로그램을 작성하시오.
# ex) A = {10, 20, 10, 30, 20, 50}
# =>  A = {10, 20, 30, 50}, len(A) = 4

# 문제 해결 방법
# dp 리스트에 자신을 포함하여 만들 수 있는 부분 수열 크기 저장
# 현재 위치(i)와 이전에 있는 원소(j) 비교
#

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
