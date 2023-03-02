# 0과 1로 이뤄진 1차 배열에서 7개 비트씩 묶어서 10진수로 출력하기
# 7개씩 잘라서 10진수로 표현
num = '0000000111100000011000000111100110000110000111100111100111111001100111'


# num_split_7 = []
# for i in range(0, len(num), 7):
#     a = num[i:i + 7]
#     num = int(a, 2)
#     print(num, end=' ')
# 2.이중 포문의 사용
# for i in range(0, len(num), 7):
#     hap = 0
#     for j in range(6,-1,-1):
#         (1 if num[i+j] == '1' else 0) * (2 ** (6-j))
#     print(hap, end='')
# 3. 다른 이중 for문
def convert(num, n):
    result = ''
    asset = '0123456789ABCDEF'  # 현재는 16진수까지만 표현함
    # num의 값이 0이 될 때까지 반복하며 해당 진수로 나눠야 함
    while num > 0:
        num, tmp = divmod(num, n)  # 몫과 나머지가 나올텐데, 몫은 계속 나눠줄 num에, 나머지는 일시적으로 담고 있으면 되므로 tmp변수에 할당
        result += asset[tmp]

    # 역순으로 뒤집어주면 된다
    result = result[::-1]

    return result
# 입력에 대해서 7씩 끊기
