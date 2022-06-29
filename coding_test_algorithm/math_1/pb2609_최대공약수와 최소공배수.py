# 두 개의 자연수를 입력받아
# 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

N, M = list(map(int,input().split()))

def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a

def lc(a,b): # 최소 공배수 = 두 자연수의 곱 / 최대공약수
    return a * b // gcd(a,b)

print(gcd(N,M))
print(lc(N,M))

# 2개의 자연수 a, b에 대해서
# a를 b로 나눈 나머지를 r이라 하면(단, a > b)
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# b를 r로 나눈 나머지 r'를 구하고
# 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
