# #1.
# print('hello world')
# #2.
# print("Mary's cosmetics")
# #3.
# print('신씨가 소리질렀다. "도둑이야"')
# #4.
# print("C:\windows")
# #5.
# print("안녕하세요.\n만나서\t\t반갑습니다.") #\n은 줄바꿈 \t는 tab(Spacebar*4)
# #6.
# print("오늘은","일요일")
# #7.
# print('naver;kakao;sk;samsung')
# print('naver', 'kakao', 'sk', 'samsung',sep=';')
# #8.
# print('naver', 'kakao', 'sk', 'samsung',sep='/')
# #9.
# print(5/3)
# #10
# print('first',end='');print('second') #print의 end와 sep는 첫 print 이후
# #11.
# Samsung_elec=int(str(50,000))
# your_stonks=int(10)
# total = print(Samsung_elec * your_stonks)
# #12
# Totalvalue = 298,000,000,000,000
# Stonk_Value_Today= 50,000
# PER = int(Totalvalue/Stonk_Value_Today)
# print('시가총액',int(298000000000000))
# print('현재가',int(50000) )
# print('PER', int(15.79))
# #13.
# s="hello"
# t="python"
# print(s+'!',t)#문자열에도 +를 사용할 수 있다.
# #14.
# print(2+2*3)
# #15.
# a='132'
# print(type(a)) #문자열화되므로 str일 것이다.
# #16.
# num_str="720"
# num_int=int(num_str)
# type(int(num_str))
# print(int(num_str))
# print(num_int+1,type(num_int))
# #17
# num=100
# print(str(num))
# #18
# data='15.79'
# #float(실수)
# data = float(data)
# print(data, type(float(data)))
# #19
# year='2020'
# year=int(year)
# print(year-1,year,year+1,sep=', ')
# print(year-3,year-2,year-1,sep=', ')
# #20
# per_month=48584
# months=36
# total = (per_month*months)
# print('매달 낼 금액은',per_month,'원 이고,',months,'개월 납부하여야 하며','총액은',total,'원 입니다.')
# #21
# letters ='python'
# print(letters[0],letters[2])
# #22
# license_plate = '24가 2210'#왼쪽부터는 0이 최초 시작값이지만, 오른쪽 역순은 -1부터가 시작이다.
# print(license_plate[-4:])
# #23
# string='홀짝홀짝홀짝'
# print(string[0],string[2],string[4],sep='')
# #24
# string='PYTHON'
# print(string[-1::-1])
# print(string[2::-1])
# # tho를 출력해보기 print(string[2:5])
# # 역순으로 OHTY를 출력해보기
#
# #25,26
# phone_number = '010-1111-2222'
# #1.replace
# phone_number.replace('-',' ')
# #2.for
# a=[]
# for a in phone_number:
#     if a.isdigit():
#         print(a,end='')
#
# #27
# url = "http://sharebook.kr"
# url.count()
# url_split=url.split('.')
# print(url_split[1])
# #28
# lang='python'
# lang[0]='PP'
# #만약 수정하고 싶다면?
# lang.replace('p','P',1)
# #29
# string = 'abcdfe2a354a32a'
# string.replace('a','A')
# #30
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# #31
# a='3'
# b='4'
# print(a+b) #34 문자열이므로
# #32
# print('hi'*3) #hihihi
# #33
# print('-'*80)
# #34
# t1='python'
# t2='java'
# print((t1+' '+t2+' ')*3)
# 66
# a = input('하나의 문자열을 입력하세요:')
# result =''
# for i in a:
#     if i != 'a':
#         result += i
#
# print(result)
# 67
# friends = ['우진','시은','메이킷','지연','지훈']
# for i in range(len(friends)):
#     print(f'{i+1} 번 친구 {friends[i]} 을 소개합니다.')
# 68
# result = []
# for i in range(1,31):
#     if i % 5:
#         result.append(i)
# print(*result)
# 69
# a1=3, d=5인 등차수열의 선언을 for문을 통해 하기
# a = 3
# d = 5
# n = 100
# for i in range(2,n+1):
#     a += d
# print(a)
# 70
# print(f'# 입력')
# a = list(map(int,input().split()))
# print(f'# 출력')
# # a.sort()
# # print(a[0])
# min = 999
# for i in a:
#     if i < min:
#         min = i
# print(min)
# 71
# a = int(input())
# b = list(map(int, input().split()))
# cnt = 0
# stuck = []
# go = []
# for i in range(len(b)):
#     if a >= b[i]:
#         cnt += 1
#         stuck.append(b[i])
#     else:
#         go.append(b[i])
# if cnt > 0:
#     print('터널 통과 불가능')
#     print(*stuck, sep='\n')
# else:
#     print('터널 통과 가능')
#     print(*go, sep='\n')
# 72
# sevens = []
# onlysevens = []
# cnt = 0
# for i in range(1, 1001):
#     if '7' in str(i):
#         sevens.append(i)
# for i in range(len(sevens)):
#     onlysevens.extend(str(sevens[i]))#extend의 특징을 잘 알자..
# for i in range(len(onlysevens)):
#     if onlysevens[i] == '7':
#         cnt += 1
# print(cnt)
#73
