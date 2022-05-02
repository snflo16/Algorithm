# 프로그래머스 땅따먹기

def solution(land):
    answer = 0

    N = len(land)
    dp = [[0]*4 for _ in range(N)]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, N):
        tmp_lst = dp[i-1]
        for j in range(4):
            tmp_lst = dp[i-1][::]
            tmp_lst[j] = 0
            dp[i][j] = max(dp[i][j], max(tmp_lst) + land[i][j])
    
    return max(dp[N-1])