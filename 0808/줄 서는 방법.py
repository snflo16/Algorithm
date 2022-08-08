def solution(n, k):
    answer = []
    
	# n_lst => 1~n번째 사람들을 담은 배열
    n_lst = [i+1 for i in range(n)]
	# methods => idx번째까지 만들 수 있는 경의 수
    methods = [0]*(n)
    
	# method => 0번째일 때는 1, 1번째 일때는 1*2, 2번째 일때는 1*2*3 ...
    for i in range(n):
        if i == 0:
            methods[i] = 1
        else:
            methods[i] = methods[i-1]*(i+1)
    
 	# 뒤집기
    methods = methods[::-1]
    
	# [a, b, c, d] => a는 k//(b에서 만들 수 있는 경의 수(tmp)) => b는 k-tmp//(c에서 만들 수 있는 경의 수(tmp))...
    i = 0
    while i < n:
        
        if k == 1:
            for j in range(len(n_lst)):
                answer.append(n_lst[j])
            break
            
        if len(n_lst) == 1:
            answer.append(n_lst[0])
            break
        
		# n=3, k=6처럼 k%i번째 경우의 수 == 0일 떄는 cnt -= 1을 해준다
        if k%methods[i+1] == 0:
            cnt = k//methods[i+1]-1
        else:
            cnt = k//methods[i+1]
        answer.append(n_lst[cnt])
        n_lst.pop(cnt)
        k -= methods[i+1]*cnt
        i += 1
        
    return answer