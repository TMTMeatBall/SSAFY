# 문제 1. 봉우리의 수
T = int(input())  # T는 지도의 갯수
for tc in range(1, T + 1):  # testcase를 1부터 반환하기 위해 1, T+1범위로
    N = int(input())  # 지도의 크기 N
    arr = [list(map(int, input().split())) for _ in range(N)]  # 지도의 크기 N*N인 이차원 배열을 선언

    result = []  # 봉우리의 빈 리스트 선언. 봉우리의 조건을 만족한다면, result.append(arr[i][j]) 할 것.

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] > arr[i - 1][j - 1] \
                    and arr[i][j] > arr[i - 1][j] \
                    and arr[i][j] > arr[i - 1][j + 1] \
                    and arr[i][j] > arr[i][j - 1] \
                    and arr[i][j] > arr[i][j + 1] \
                    and arr[i][j] > arr[i + 1][j - 1] \
                    and arr[i][j] > arr[i + 1][j] \
                    and arr[i][j] > arr[i + 1][j + 1]:
                result.append(arr[i][j])  # 각 2차원배열에서 가장자리 구역을 제외하는(1,N-1)범위에서 arr[i][j]가 8방 탐색한 좌표들의\
                # 크기와 비교했을 때, 모두 높다면, 봉우리 조건을 만족했으므로 result에 append

    if len(result) <= 1: #봉우리의 갯수가 없거나, 하나뿐이라면,
        print(f'#{tc} -1') #-1을 결과값으로 반환
    else:#그 외의 경우에는
        result.sort() #list.sort()는 오름차순으로 리스트 안의 요소를 정리한다.
        ans = result[-1] - result[0] #가장 높은 봉우리인 마지막 값 - 가장 낮은 봉우리는 첫 번째 값의 차가 곧 정답이 된다.
        print(f'#{tc} {ans}') #출력
