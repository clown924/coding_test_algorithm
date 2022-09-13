# 일곱 난쟁이의 키의 합이 100
# 아홉 난쟁이의 키가 주어졌을 때,
# 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

# 문제 해결 방법
# 9명이 주어졌을 때, 7명의 키의 합은 100이다
# 9명 중 2 명을 빼고 7명의 키를 더하면 100이다
# 9명 중 2명을 순차적으로 빼며 100이 나오는 지 확인한다.

A = []
for _ in range(9):
    A.append(int(input()))

total = sum(A)

for i in range(9):
    for j in range(i+1, 9):
        if total - (A[i] + A[j]) == 100:
            num1, num2 = A[i], A[j]

            A.remove(num1)
            A.remove(num2)
            A.sort()
            for c in range(len(A)):
                print(A[c])
            break
    if len(A) < 9:
        break
