# 16진수 문자로 이뤄진 1차 배열이 주어질 때, 암호비트패-탄을 찾아 차례대로출력하시오.
num = '0269FAC9A0'
transformed = 0
pattern_table = {'0': '001101',
                 '1': '010011',
                 '2': '111011',
                 '3': '110001',
                 '4': '100011',
                 '5': '110111',
                 '6': '001011',
                 '7': '111101',
                 '8': '011001',
                 '9': '101111',
                 }
idx = 0
for i in range(len(binary_string)):
    if binary_string[i:i + 6] in pattern_table:
        idx = i
        break
for i in range(idx, len(binary_string), 6):
    string = binary_string[i:i + 6]
    if len(binary_string) != 6:
        break
    print(pattern_table[string], end=' ')
#진짜루짜루몰르갯읆..