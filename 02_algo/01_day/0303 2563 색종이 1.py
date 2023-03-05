N = int(input())
board = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10): #(3 4 5 6 7 8 9 10 11 12 13)
        for j in range(y, y + 10): #(7 8 9 10 11 12 13 14 15 16 17)
            if board[i][j] == 0:
                board[i][j] += 1
                cnt += 1

print(cnt)

