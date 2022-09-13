from collections import deque

N, K = map(int,input().split())
queue = deque(range(1, N + 1))
answer = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
print(str(answer).replace('[','<').replace(']','>'))

# 문제 풀이
# 1. queue에 1부터 N까지의 숫자를 넣어준다.
# 2. while문의 조건을 queue안의 모든 숫자가 없어질 때까지로 정하고
#    for문의 범위를 range(k-1), K로 정한다.
# 3. queue의 왼쪽 값을 popleft해서 append함으로써 없애야하는
#    K번째 수를 가장 왼쪽에 둔다.
# 4. K번째 수를 제거해서 정답 배열인 answer에 추가한다.

# 중요한 로직
# 가장 왼쪽의 수를 popleft하여 append함으로써
# 원형의 큐가 생성된다.
# 큐와 스택의 혼합된 개념인 디큐(덱)을 이용한다.
