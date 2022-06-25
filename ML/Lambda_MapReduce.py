# Lambda
# - 함수 이름 없이, 함수처럼 쓸 수 있는 익명함수
# - 수학의 람다 대수에서 유래함
f = lambda x, y : x + y
print(f(1,4)) 

# Map & Reduce
# Map Function - Sequence 자료형 각 element에 동일한 function을 적용함
ex = [1,2,3,4,5]
f = lambda x : x ** 2
print(list(map(f,ex))) # list() 꼭 붙이기

# Redice function
# - map function 과 달리 list에 똑같은 함수를 적용해서 통합

from functools import reduce
print(reduce(lambda x, y:x+y,[1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x,y : x*y, range(1,n+1))
print(factorial(5))