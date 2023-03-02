dic = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # 1. 암호코드 받기 거꾸로 세어서 1이 나오는 순간, 그곳부터 56자를 받을 수 있어야 함
    binary_code = ''
    for i in range(N):
        for j in range(M - 1, 54, -1):  # M-1열 부터 55열까지 거꾸로
            if arr[i][j] == '1':
                binary_code = arr[i][j - 55:j + 1]  # 거꾸로 세어서 1이 나온 순간에 해당 열-55부터 100까지 하면 56개 찾을 수 있다
                break
        if binary_code != '':
            break
    # 2. 7개씩 끊어 받은 이진배열을 dic에서 어떤 값인지 code에 받기
    code = [0]*8
    tuple_binary_code = [tuple(i) for i in binary_code]
    for i in range(8): #01234567
        code[i] = dic[binary_code[i*7:i*7+7]] #0-6 7-13 14-20 21-27 ...50-56



    print(f'{tc} {binary_code}')
