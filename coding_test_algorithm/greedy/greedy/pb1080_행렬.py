# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데
# 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

# 문제 해결 방법
# 1. 첫번째 A 행렬의 값과 B 행렬의 값이 일치하지 않으면 뒤집는다.
# 2. 두번쨰 A 행렬의 값과 B 행렬의 값이 일치하지 않으면 뒤집는다.
# 3. A와 B 비교

N, M = list(map(int,input().split()))  # N, M 입력 받기
count = 0
A = []
B = []

for i in range(N):
    A.append(list(map(int,input())))
for j in range(N):
    B.append(list(map(int,input())))

def reverse_matrix(X,Y): # 3x3 행렬 뒤집기
    for i in range(X, X+3):
        for j in range(Y,Y+3):
            A[i][j] = 1 - A[i][j]

for i in range(N-2):  # 행이 5행이면 3번까지 이동 가능, 따라서 N - 2
    for j in range(M-2): # 열이 5열이면 3번까지 이동 가능, 따라서 M -2
        if A[i][j] != B[i][j]:
            reverse_matrix(i,j)
            count += 1
        if A == B:
            break
if A != B:
    print(-1)
else:
    print(count)
