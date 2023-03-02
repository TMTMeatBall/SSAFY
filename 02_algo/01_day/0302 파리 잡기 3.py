T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    ddx = [-1, -1, 1, 1]
    ddy = [-1, 1, -1, 1]

    cross_total = 0 #십자로 뿌렸을 때에 좌표값들의 총합
    x_total = 0 # x자 스프레이의 경우 총합
    answer = 0 #위의 두 값을 비교해서 더 많은 친구를 반환함
    for i in range(N):
        for j in range(N):
            # cross_total = 0 #무조건 중앙값이 탐색에서는 빠지므로 미리 더해줌
            # x_total = 0 #위와 동일
            a = arr[i][j]
            b = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l
                    nnx = i + ddx[k] * l
                    nny = j + ddy[k] * l

                    if -1 < nx < N and -1 < ny < N:
                        a += arr[nx][ny] #각 십자에서의 좌표값들을 더함
                    if -1 < nnx < N and -1 < nny < N:
                        b += arr[nnx][nny] #각 X자에서의 좌표값들을 더함

            if cross_total < a:
                cross_total = a
            if x_total < b:
                x_total = b

    if cross_total > x_total: #서로 비교해서 한 쪽이 크면
        answer = cross_total
    else:
        answer = x_total #다른 경우 반대를 주면 같거나 앞쪽이 작을 때에도 큰 값이 반환될 것.

    print(f'#{tc} {answer}')
    #값이 output보다 크기 때문에.. 어디선가 더 더해졌을 수 있음
    # 해결해야 할 것
    # 1. 십자or대각 탐색->진행 할 때에, m-1만큼 더 나아가야 하는 것
    # 2. 가장 큰, 십자 경우와 가장 큰 대각 경우의 총합을 비교하기

# def crosstotal(x, y, M):
#     spray = arr[x][y]
#     cnt = arr[x][y]
#     for i in range(4):
#         for j in range(1, M):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= N or ny >= N:
#                 continue
#             cnt += arr[nx][ny]
#
#
# def xtotal(x, y, M):
