N = int(input())
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오.

# 문제 해결 방안
# B에 있는 수는 재배열 하면 안되므로, B의 가장 큰 숫자에는 A에서 가장 작은 숫자를
# 대입하여 곱한다.
 
# 방법 1
result = 0
list1 = []
list2 = []

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

list1.sort(reverse=True)
list2.sort()

for i in range(N):
    result += list1[i] * list2[i]

print(result)


# 방법 2
# A의 최소값과 B의 최대값을 구한 후 두 값을 곱해 result에 더한다.
# 이후 A의 최소값과 B의 최대값을 pop을 이용해 각 list에서 pop해준다.
