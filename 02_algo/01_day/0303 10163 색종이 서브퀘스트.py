# 인풋 받고 뒤집을 것이므로 x,y 에서 y,x로 바꿔서 쓰기
N = int(input())
# 순회하면서 지정한 사각형의 숫자가 아닐 경우에, 싹 덮어주는 방식으로 구하기
board = [[0] * 1001 for _ in range(1001)]

for _ in range(1,N+1):
    x, y, garo, sero = map(int, input().split())

    for i in range(y,y+sero):
        board[i][x:x+garo] = _*garo #편하게 뒤집기 y를 x로 x를 y로
    for i in range(1,N+1):
        result = 0
        for cnt in range(1001):
            result += board[cnt].count(i)

print(result)