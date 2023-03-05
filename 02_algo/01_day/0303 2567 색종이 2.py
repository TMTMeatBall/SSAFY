N = int(input())
board = [[0] * 100 for _ in range(100)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if board[i][j] == 0:
                board[i][j] += 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            cnt = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<100 and 0<=ny<100 and board[nx][ny] == 1:
                    cnt += 1

            if cnt == 3:
                result += 1
            elif cnt == 2:
                result += 2
print(result)