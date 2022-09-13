S = list(input())
stack = ''
tag = False
answer = ''

for i in S:
    if tag == False:
        if i == '<':
            tag = True
            stack += i
        elif i == ' ':
            stack += i
            answer += stack
            stack = ''
        else:
            stack = i + stack
    elif tag == True:
        stack += i
        if i == '>':
            tag = False
            answer = answer + stack
            stack = ''
print(answer + stack)
