# Q1
korean = 80
English = 75
Math = 55
result = (korean + English + Math) / 3
print(result)

# Q2
a = 13
if(a % 2) :
    print("홀수입니다.")
else :
    print("짝수입니다.")

# Q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
pin = "881120-1068234"
sexual = pin[7]
print(sexual)

# Q5
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# Q6
List1 = [1, 3, 5, 4, 2]
List1.sort()
List1.reverse()
print(List1)

# Q7
List2 = ['Life', 'is', 'too', 'short']
result = ' '.join(List2)
print(result)

# Q8
tuple1 = (1,2,3)
tuple2 = tuple1 + (4,)
print(tuple2)

# Q9
#a = dict()
# a[[1]] = 'python' => dictionary 에는 변경 가능한 값이 들어가지 못함.
# a[[1]]에는 리스트가 들어가지 못함. 튜플 가능

# Q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = list(set(a))
print(b)

# Q12
a = b = [1,2,3]
a[1] = 4
print(b)
# a와 b 변수는 모두 동일한 [1,2,3]이라는 리스트 객체를 가리키고 있기 때문.