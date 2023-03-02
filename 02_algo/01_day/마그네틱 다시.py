T = 1
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0  # 1,2 인 떄에 +=1씩 반환할 변수
    for j in range(N): #j(열)이 가장 마지막에 바뀌므로 i가 먼저 빠르게 변하면서j=0상태인 열을 stack에 반영
        i = 0 #j의 초기화 때마다 i=0으로 바꾼다
        stack = []  # 1은 만날 때마다 담고, 2를 만나면 전부 pop 할 빈 스택 이 스택도 j가 변할 때마다 초기화된다.
        while i < N:
            if not stack and arr[i][j] == 1: #arr[i][j]이지만 j가 고정인 상태에서 i만 변하므로 열만 따는 셈. i가 변하는 경우에서만 stack, i가 계속 바뀌고, j가 변하는 순간 두값을 초기화 한다.
                stack.append(1)
            elif stack and arr[i][j] == 2:
                cnt += stack.pop()
            i += 1

    print(f'#{tc} {cnt}')
#열을 순회하면서 한칸씩 오른쪽으로 가야하는 게 아닌가?
