# 문제 2. 탐사 로봇
T = int(input())  # 구역의 갯수 T
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    track = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 0:
                k = arr[i][j + 1]
                track.append(0)

            elif arr[i][j] == 1:
                k = arr[i - 1][j]
                track.append(1)

            elif arr[i][j] == 2:
                k = arr[i][j - 1]
                track.append(2)

            else:
                k = arr[i - 1][j]
                track.append(3)

    print(track)
x = 0
y = 0
visit = [[0]*N for _ in range(N)]
for i in range(1,N-1):
    if y + 1 <= N and arr[x][y] == 0:
        track.append(0)
        visit[i] = 1
        y = y+1
    if x + 1 <= N and arr[x][y] == 1:
        track.append(1)
        visit[i] = 1
        x = x+1
    if y - 1 >= 0 and arr[x][y] == 2
        track.append(2)
        y = y-1
    if x - 1 >= 0 and arr[x][y] == 3
        track.append(3)
        x = x+1
# x-1
# -=1
# y-1
# -=1
# x+1
# y+1
# 범위에 대해서 +1하는 경우는 N-1까지
# -1하는 경우는 1 까지
# 그냥 이동을 기록해서 for i 돌게 한 뒤에 같은 것이 만나는 경우엔 삭제하고 다른것이 나오면 바로 continue
