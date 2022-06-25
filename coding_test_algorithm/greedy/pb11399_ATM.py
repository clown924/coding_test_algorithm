N = int(input()) # 사람 수

list1 = list(map(int,input().split()))
result = 0

list1.sort()

for i in range(N):
    for j in range(i+1):
        result += list1[j]

print(result)
 
