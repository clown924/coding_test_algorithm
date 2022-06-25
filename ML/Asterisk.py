# Asterisk
# - 흔히 알고 있는 * 를 의미함
# - 단순 곱셈, 제곱연산, 가변 인자 활용 등 다양하게 사용됨
def asterisk_test(a,*args): # tuple 타입
    print(a,args)
    print(type(args))
asterisk_test(1,2,3,4,5,6)

def asterisk_test2(a,**kargs): # dict 타입
    print(a,kargs) 
    print(type(kargs))
asterisk_test2(1,b=2,c=3,d=4,e=5,f=6)

# Asterisk - unpacking a container
# - tuple, dict 등 자료형에 들어가 있는 값을 unpacking
# - 함수의 입력값, zip 등에 유용하게 사용가능

def asterisk_test3(a, *args):
    print(a,args[0])
    print(type(args))
asterisk_test3(1,(2,3,4,5,6))

def asterisk_test4(a,args):
    print(a,*args)
    print(type(args))
asterisk_test4(1, (2,3,4,5,6))

a,b,c = ([1,2],[3,4],[5,6])
print(a,b,c)
data = ([1,2],[3,4],[5,6])
print(*data)

def asterisk_test5(a,b,c,d):
    print(a,b,c,d)
data = {"b":1,"c":2,"d":3}
asterisk_test5(10,**data)

for data in zip(*([1,2],[3,4],[5,6])):
    print(data)
