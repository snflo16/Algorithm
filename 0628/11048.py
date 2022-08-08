from re import L


N, M = map(int, input().split())

candy = [list(input().split()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            candy[i][j] = int(candy[i][j])
            continue
        up = 0
        left = 0
        if i != 0:
            up = candy[i-1][j] 
        if j != 0:
            left = candy[i][j-1]
        candy[i][j] = int(candy[i][j]) + max(up, left)

print(candy[N-1][M-1])