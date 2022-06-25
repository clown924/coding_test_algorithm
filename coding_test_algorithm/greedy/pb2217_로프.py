# 문제 해결 방법

# k개의 로프로 중량이 w인 물체를 들어올리 때, 각각의 로프에는 w/k 만큼의 중량
# 8 8 8 10 20 있으면 40을 들어올릴 수 있음. (각 8의 무게로)
# 하지만, 8 8 8 40 40이 있으면 40 40 만으로 80을 들어올릴 수 있음.
# 임의로 몇 개를 사용 가능 하므로.
# 따라서, 가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 로프 갯수
# Ex) [100, 80, 60, 40, 20] 이 있다면 [100*1, 80*2, 60*3, 40*4, 20*5] 해서 가장 큰 값이 정답
N = int(input())
list1 = []
for i in range(N):
    list1.append(int(input()))
 
list1.sort(reverse=True)
answer = 0

for i in range(N):
    list1[i] = list1[i] * (i+1)

answer = max(list1)

print(answer)
