# N = int(input())
# lst = set()

# for i in range(1, int(N**0.5)+1):
#     lst.add(i**2)

# if N in lst:
#     print(1)
# else:
#     ans = 1
#     while N not in lst:
#         tmp_lst = set()
#         ans += 1
#         lst = list(lst)
#         lst.sort()
#         for j in range(len(lst)):
#             for i in range(1, int(N**0.5)+1):
#                 tmp = i**2 + lst[j]
#                 if tmp <= N:
#                     tmp_lst.add(tmp)
#                 else:
#                     break
#         lst = list(tmp_lst)
#         if N in lst:
#             break
#     print(ans)

N = int(input())

nums = [-1]*(N+2) # [-1, -1, -1]

lst = set()
for i in range(1, int(N**0.5) + 1):
    nums[i**2] = 1
    lst.add(i**2)

if N in lst:
    print(1)
else:
    ans = 1
    while nums[N] == -1:
        ans += 1
        lst = list(lst)
        lst.sort()
        tmp_lst = set()
        for i in range(len(lst)):
            for j in range(1, int(N**0.5) + 1):
                tmp = j**2 + lst[i]
                if tmp <= N and nums[tmp] == -1:
                    tmp_lst.add(tmp)
                    nums[tmp] = ans
                elif tmp > N:
                    break
            if nums[N] != -1:
                break
        if nums[N] != -1:
                break
        lst = tmp_lst
    print(nums[N])
