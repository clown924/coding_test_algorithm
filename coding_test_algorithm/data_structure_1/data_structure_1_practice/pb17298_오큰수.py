N = int(input())
arr = list(map(int,input().split()))
stack = [0]  # stack은 index저장을 위한 list
answer = [-1 for i in range(N)]

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
