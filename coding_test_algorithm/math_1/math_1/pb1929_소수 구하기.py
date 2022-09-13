M, N = map(int,input().split())
answer = []
def is_prime_number(a):
    if a == 1:
        return False
    else:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True

for i in range(M,N+1):
    if is_prime_number(i):
        print(i)

# pb1979_소수 찾기의 is_prime_number를 사용하게 되면 시간초과.
# 해당 수가 소수인지 확인하려면 해당 수의 제곱근까지만 소수인지
# 아닌지 확인하면 된다.
