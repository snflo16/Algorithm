# 백준 정수삼각형
import sys
input = sys.stdin.readline 

N = int(input())
dp = [list(map(int, input().split(" "))) for _ in range(N)]

for i in range(1, N):
    for j in range(len(dp[i])):
        left = 0
        right = 0
        if j-1 >= 0:
            left = dp[i-1][j-1]
        if j < len(dp[i-1]):
            right = dp[i-1][j]
        dp[i][j] = max(dp[i][j] + left, dp[i][j] + right)

print(max(dp[N-1]))
print(dp)