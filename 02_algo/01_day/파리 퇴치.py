T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N - M+1 ):
        for j in range(N - M +1 ):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += arr[i + k][j + l]

            if tmp > max:
                max = tmp

    print(f'#{tc} {max}')
