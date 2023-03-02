def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (i << j) else '0'
    print(output, end=' ')


a = 0x10
x = 0x01020304
print('%d = ' % a, end='')
Bbit_print(a)
print()
print('0%X = ' % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i * 8) & 0xff)
# 0 과 1로 이뤄진 1차 배열에서 7개 byte 를 묶어서 10진수로 출력하기
# 00000010001101
