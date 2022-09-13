# 자연수 N과 M이 주어졌을 때,
# 아래 조건을 만족하는
# 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

# 문제 해결 방법
# 15649문제에서 탈출 조건에 또 다른 조건을 붙인다.
# 고른 수열은 오름차순 이어야 하므로
# 왼쪽 수와 오른쪽 수를 비교하여 오른쪽 수가 크면 출력한다.

# 15649 문제에서는 1부터 n까지 모든 숫자 사용했지만
# [2,1]과 같이 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외하기위해
# start부터 n까지 숫자를 사용
# 재귀함수를 호출할때는 i를 이용해서 자신의 다음 숫자를 부르게됨.

N, M = map(int,input().split())
out = []

def solve(start):
    if len(out) == M:
        print(' '.join(map(str,out)))
        return

    for i in range(start, N+1):
        if i not in out:
            out.append(i)
            solve(i+1)
            out.pop()

solve(1)
