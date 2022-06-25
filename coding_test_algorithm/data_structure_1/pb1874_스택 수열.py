# ex) N = 8, Ax = [4, 3, 6, 8, 7, 5, 2, 1]
# stack = [1,2,3,4] -> + + + +
# 4, 3이 나와야 되므로 ->   - -  하면 4, 3이 차례대로 나옴
# 이후에 stack = [1,2,5,6] -> + + 이 되고,
# 6이 나와야 되므로 -> - 하면 Ax = [4, 3, 6], stack = [1, 2, 5]
# 이후에 stack = [1, 2, 5, 7, 8] -> + +
# 8, 7 이 나와야 되므로 -> - - 하면 Ax = [4, 3, 6, 8, 7]
# stack = [1, 2, 5] 이후에 차례대로 - - - 하면 된다.
# 따라서 + + + + - - + + - + + - - - - -

# 문제 해결 방법
# stack의 특성상 LIFO 특성을 가지고 있다.
# num을 입력받으며 num과 stack의 마지막 원소가 같으면 pop을 해준다.
# count를 세면서 num 이전의 값은 stack에 append해준다.

# stack의 특성을 활용하는 문제이다.

N = int(input())
stack = []
answer = []
temp = True
count = 1

for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        temp = False

if temp == False:
    print("NO")
else:
    for answers in answer:
        print(answers)
