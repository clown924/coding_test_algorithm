import sys
def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a

T = int(sys.stdin.readline())

for i in range(T):
    list_A = list(map(int,sys.stdin.readline().split()))
    N = list_A.pop(0)
    total = 0
    for j in range(N):
        for k in range(N):
            if j < k:
                total += gcd(list_A[j], list_A[k])
    print(total)

# 문제 해결 방법
# 입력 받은 수들을 리스트로 만든 후 gcd를 구하는 알고리즘으로
# 가능한 쌍들의 gcd를 구한다. 이후 total에 모두 더해준다
# ex)
# 10, 20 => 10
# 10, 30 => 10
# 10, 40 => 10
# 20, 30 => 10
# 20, 40 => 20
# 30, 40 => 10
# 따라서, 10 + 10 + 10 + 10 + 20 + 10 = 70
