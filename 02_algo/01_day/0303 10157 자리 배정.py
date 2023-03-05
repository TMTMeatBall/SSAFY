# C, R = map(int, input().split())
# K = int(input())

# 1.가장 좌측의 열값은 1부터 시작한다
# 2. 자리의 행값은 아래부터 시작하고, 1이 최소값이다
# 3. 시계방향으로 달팽이 돌리는데, 처음은 위,우,하,좌 로 시작한다.
##. 대기 순서가 K인 관객에게 몇 번 좌석(x,y)가 배정되는가를 코드로 작성

# 이차원배열 선언
# x 감소 y증가 x 증가 y 감소
# 위아래를 뒤집어서 00부터 10 20 30... 으로 달팽이 해버린다. 출력은 열을 다시 뒤집는다
# if K > C*R:
#     print(0)
#
#
# board = [[0] * R for _ in range(C)]
# board[0][0] = 1 # 뒤집었으므로 시작위치를 이렇게 잡는다
# x, y = 0, 0
# move = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 밑으로,오른쪽으로,위로,왼쪽으로
# direction = 0  # 방향을 잡는다 사용례는 move[direction] 가 된다
# for i in range(2, K + 1):  # 1을 board[0][0]에 받았음
#     a, b = move[direction]
#     nx = x + a  # 변화 적용
#     ny = y + b  # 변화 적용
#     if 0 <= nx < C and 0 <= ny < R and board[nx][ny] == 0:
#         board[nx][ny] == 1
#         x = nx
#         y = ny
#         break
#     else:
#         direction = (direction + 1) % 4
# print(y + 1, x + 1)


dx = []
dy =










