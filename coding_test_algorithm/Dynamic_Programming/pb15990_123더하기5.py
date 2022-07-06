# 1 = (1)  => 1개
# 2 = (2)  => 1개
# 3 = (1 + 2), (2 + 1), (3)  => 3개
# 4 = (1 + 2 + 1), (1 + 3), (3 + 1)  => 3개
# 5 = (1 + 3 + 1), (2 + 3), (3 + 2), (2 + 1 + 2)  => 4개
# 6 = (1 + 2 + 3), (1 + 3 + 2), (3 + 2 + 1), (3 + 1 + 2),
#     (1 + 2 + 1 + 2), (2 + 1 + 2 + 1), (2 + 3 + 1),
#     (2 + 1 + 3)    => 8

# 문제 풀이
# 같은 수를 연속해서 두 번 쓸 수 없으므로
# 핵심은 마지막으로 사용한 수
# n = 6이면
# 3에서 1과 2로 끝나는 거에 3을 붙인다.
# 4에서 1과 3으로 끝나는 것에 2를 붙인다.
# 5에서 2와 3으로 끝나는 것에 1을 붙인다.

# 각각 1,2,3으로 끝나는 것의 개수이다.
# dp[1] = [1,0,0]
# dp[2] = [0,1,0]
# dp[3] = [1,1,1]

# 점화식
# dp[i][0] = dp[i-1][1] + dp[i-1][2]  => 1로 끝나는 것
# dp[i][1] = dp[i-2][0] + dp[i-2][2]  => 2로 끝나는 것
# dp[i][2] = dp[i-3][0] + dp[i-3][1]  => 3으로 끝나는 것

import sys
dp = [[0 for _ in range(3)] for _ in range(100001)]

dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4,100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % 1000000009)
