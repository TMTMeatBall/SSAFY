# # 100*100크기의 board
# # 1은 n극 2는s극
# # 1은 2에 끌리고 2는 1에 끌린다.
# # 떨어지지 않고 남은 교착 상태의 갯수를 구하기
#
# # 10개의 testcase
# T = 10
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]  # 이차원배열 입력
#     result = 0
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[j][i] == 1:
#                 if cnt == 0 or cnt == 2:
#                     cnt = 1
#             elif arr[j][i] == 2:
#                 if cnt == 1:
#                     cnt = 2
#                     result += 1
#             else:
#                 if cnt == 2:
#                     cnt = 0
#
#
#
#     print(f'#{tc} {result}')
# # 10개의 testcase
T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  # 이차원배열 입력
    result = 0  # 최종 결과
    # 스택에 받아서, 2가 들어간 순간에 날리고 cnt += 1 N이(떨어지거)나 S(올라가거나) 한개만 따져도 된다
    for i in range(N):
        stack = []  # 스택을 여기 두는 이유
        for j in range(N):
            if arr[j][i] == 1:
                stack.append(1)
            if arr[j][i] == 2 and stack.pop() == 1 and len(stack) != 0:
                stack.clear()
                result += 1
    print(f'#{tc} {result}')

    # 열로 받아서, 우선 열 안에 1개씩만 들어있는 경우는 전부 0으로
    # result = 0
    # a = []
    # for i in range(100):
    #     for j in range(100):
    #         a.append(arr[j][i])
    # B = []
    # for i in range(len(a)):
    #     if a[i] != 0:
    #         B.append(a[i])
    # while B[0] == 2:
    #     B.pop(0)
    #
    # while B[-1] == 1:
    #     B.pop(-1)
    #
    # for i in range(len(B)):
    #     if B[i] == 1 and B[i + 1] == 2:
    #
    #         result += 1
    #
    # # for i in B:
    # #     if B[i] == 1 and B[i+1]:
    # #         result += 1

    # 세는 방법에 대해서...
    # 1인 경우에,열 받은 리스트의 뒤에 2가 있으면, result += 1
    # 1 다음이 바로 2인 경우 또는 2 다음이 바로 1인 경우만
    # 시작이 2면 삭제 1이면 카운트 열순 안의 작은 리스트의 원소가 짝수일 때에만?
    # print(f'#{tc} {result}')

