# 문제 해결 방법
# 1. 0 번째 전구를 바꿔주고 시작할지
# 2. 0 번째 전구를 바꾸지 않고 시작할지 구분한다.
# 3. 이전 전구를 비교하며 다시 되돌아가지 않는다.(그리디, 전에 이미 바꾼 것을 다시 바꿀 필요X)

N = int(input())
A = list(map(int,input()))
B = list(map(int,input()))

def change(C, D):
    count = 0
    temp = C[:]
    for i in range(1,N):
        if temp[i-1] == D[i-1]:  # 이전 전구가 같은 상태면 넘기기
            continue

        count += 1               # 이전 전구가 상태가 다르면
        for j in range(i-1,i+2):
            if j < N :
                temp[j] = 1 - temp[j]

    return count if temp == D else 1e9

# 0 번째 전구의 스위치를 누르지 않은 경우
res = change(A,B)

# 0 번쨰 전구의 스위치를 누르는 경우
A[0] = 1 - A[0]
A[1] = 1 - A[1]
res = min(res,change(A,B) + 1)
print(res if res != 1e9 else -1)
