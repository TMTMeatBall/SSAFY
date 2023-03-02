T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    performance = 0
    a = N // 2
    b = N // 2
    for i in range(N):
        for j in range(a, b + 1):
            performance += arr[i][j]

        if i < N // 2:
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1
    print(f'#{tc} {performance}')

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     farms = 0
#     a = N // 2
#     b = N // 2
#     for i in range(N):
#         for j in range(a, b + 1):
#             farms += arr[i][j]
#
#         if i < N // 2:
#             a -= 1
#             b += 1
#         else:
#             a += 1
#             b -= 1
#
#     print(f'#{tc} {farms}')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    brr = [list(map(int,input().split()))for _ in range(N)] #input().split() 쓰면 한개씩 아니라 열씩 묶여서 나온다.
    print(arr)
    print(brr)