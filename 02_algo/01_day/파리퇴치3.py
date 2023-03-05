T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    ddx = [-1, -1, 1, 1]
    ddy = [-1, 1, -1, 1]

    cross_total = 0
    x_total = 0
    answer = 0
    for i in range(N):
        for j in range(N):
            a = arr[i][j]
            b = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l
                    nnx = i + ddx[k] * l
                    nny = j + ddy[k] * l

                    if -1 < nx < N and -1 < ny < N:
                        a += arr[nx][ny]
                    if -1 < nnx < N and -1 < nny < N:
                        b += arr[nnx][nny]  # 각 X자에서의 좌표값들을 더함
            if cross_total < a:
                cross_total=a

            if x_total < b:
                x_total = b
    if cross_total > x_total:
        answer = cross_total
    else:
        answer = x_total

    print(f'#{tc} {answer}')