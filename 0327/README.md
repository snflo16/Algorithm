# README

## 1463➗

- N으로 1을 만들 수 있는 최소 횟수

```python
N = int(input())

answer = -1
numbers = [[], [N]]

# N이 1이면 더 이상 바꿀 필요 X
if N == 1:
    answer = 0
else:
    # 이전 번에 만들었던 숫자를 기준으로 만들 수 있는 숫자를 확인
    def make_num(n):
        global answer
        tmp = set()
        for k in numbers[n-1]:
            if k%3 == 0:
                tmp.add(k//3)
            if k%2 == 0:
                tmp.add(k//2)
            tmp.add(k-1)
        # 만일 이번에 만들 수 있다면 n-1을 답으로 치환
        if 1 in tmp:
            answer = n-1
            return
        # 그렇지 않다면 다음번 횟수를 확인
        else:
            numbers.append(list(tmp))
            make_num(n+1)

    make_num(2)

print(answer)
```



## 9095🎰

- 1, 2, 3을 이용해 N을 만들 수 있는 경우의 수

```python
for _ in range(int(input())):
	    
    N = int(input())

    answer = 0
	
    # 완전 탐색을 하며 N까지 만들 수 있는 수를 셈
    def make_num(n):

        global answer 
		
        # N이 되면 answer에 +1
        if n == N:
            answer += 1
            return
        
        # N을 넘으면 더 이상 확인 X
        if n >= N:
            return
        
        for i in (1, 2, 3):
            make_num(n+i)

    make_num(0)

    print(answer)
```

