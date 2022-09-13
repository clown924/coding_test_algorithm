N = int(input())
list1 = []
# 문제 해결 방안
# 빨리 끝나는 회의 순서대로 정렬 후
# 빨리 시작하는 회의 순서대로 정렬

for i in range(N) :
    first, second = map(int,input().split())
    list1.append([first,second])
 
list1.sort(key = lambda a: (a[1],a[0]))

cnt = 1
end_time = list1[0][1]  # end_time은 마지막 회의 시각
for i in range(1,N):
    if list1[i][0] >= end_time:
        cnt += 1
        end_time = list1[i][1]

print(cnt)
