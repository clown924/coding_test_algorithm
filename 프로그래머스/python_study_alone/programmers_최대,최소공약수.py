def gcd(n1,n2):
    if n1 < n2:
        n1 , n2 = n2, n1
    while n2 != 0:
        (n1, n2) = (n2, n1%n2)
    
    return n1

def solution(n, m):
    answer = [gcd(n,m),(n * m) / gcd(n,m)]
    return answer