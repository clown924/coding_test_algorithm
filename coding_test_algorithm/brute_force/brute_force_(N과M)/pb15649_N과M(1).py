# 자연수 N과 M이 주어졌을 때,
# 아래 조건을 만족하는
# 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 문제 풀이 방법
# DFS 알고리즘을 통해 백트래킹으로 구현
# DFS란 깊이 우선 탐색. 특정한 상황에서 최대한 깊숙이 들어가
# 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색.

# DFS 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입하고 방문처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면
#    그 인접 노드를 스택에 넣고 방문처리.
#    방문하지 않은 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복.


N, M = map(int,input().split())
visited = [False] * N  # 탐사 여부 check
out = [] # 탐사한 수들을 담을 리스트 선언

def solve(depth, N, M):
    if depth == M: # 탈출 조건
        print(' '.join(map(str,out))) # list를 str로 합쳐 출력
        return
    for i in range(len(visited)): # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면
            visited[i] = True # 탐사 시작(중복 제거)
            out.append(i + 1) # 탐사 내용
            solve(depth + 1, N, M)  # DFS
            visited[i] = False  # 깊이 탐사 완료
            out.pop() # 탐사 내용 제거


solve(0, N, M)

"""
n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()
"""
