for _ in range(int(input())):
    
    N = int(input())

    answer = 0

    def make_num(n):

        global answer 

        if n == N:
            answer += 1
            return
        
        if n >= N:
            return
        
        for i in (1, 2, 3):
            make_num(n+i)

    make_num(0)

    print(answer)