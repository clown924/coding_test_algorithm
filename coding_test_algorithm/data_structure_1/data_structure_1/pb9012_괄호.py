T = int(input())

for _ in range(T):
    str = input()
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        elif str[i] == ')':
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
