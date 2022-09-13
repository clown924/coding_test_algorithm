import sys
stack_left = list(sys.stdin.readline().strip())
stack_right = []

M = int(input()) # 명령어 개수

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if stack_left:
            stack_right.append(stack_left.pop())
    elif command[0] == 'D':
        if stack_right:
            stack_left.append(stack_right.pop())
    elif command[0] == 'B':
        if stack_left:
            stack_left.pop()
    else:
        stack_left.append(command[1])

stack_left.extend(reversed(stack_right))
print(''.join(stack_left))

### 중요한 로직
# B 와 P $ 의 로직을 보았을 때, 커서의 왼쪽에 없애고 추가함.
# 따라서, 커서를 기준으로 문자열을 두 스택에 나눠 담는다.
# 그렇게 하면 앞의 스택의 top을 뒤의 스택에 append한다면
# 커서를 옮겨다닐 수 있게 된다.
