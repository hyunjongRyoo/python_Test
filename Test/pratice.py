# # #자료형
# # #숫자
# # print(5)
# # print(-10)
# # print(3.14)
# # print(1000)
# # print(5 + 3)
# # print(2 * 4)
# # print(3*(3+1))
# # #문자
# # print('풍선')
# # print("풍선")
# # print("z"* 9)
# # print(5 > 10)
# # print(5 < 10)
# # #boolean
# # print(True)
# # print(False)
# # print(not True)
# # print(not False)
# # print(not (5>10))
# # #변수
# # animal ="개"
# # name ="연탄이"
# # age = 4 
# # hobby = "산책"
# # is_adult = age >=3 
# # print("우리집 "+ animal +"의 이름은" + name + "예요")
# # hobby = "공놀이"
# # # print( name + "는" + str(age) + "살이며" +hobby+"을 아주 좋아합니다")
# # print( name , "는" , str(age) ,"살이며" ,hobby,"을 아주 좋아합니다")
# # print(name +"는 어른일까요?" + str(is_adult))
# # #주석
# # '''  
# # 전체적으로 주석처리 하고싶으면 작은 따옴표 3개 
# # '''
# # # 문장 전체 선택후 command / 주석처리

# # # QUIZ CHATER 1
# # station = "사당"
# # print(station +"행 열차가 들어오고 있습니다")

# # #연산자
# # print(1+1)
# # print(3-2)
# # print(5*2)
# # print(6/2)

# # print(2**3) #2의 3제곱
# # print(5%3) #나머지 구하기 2 
# # print(10%3) 
# # print(5//3) #몫 구하기 1 
# # print(10//3) #몫 구하기 3

# # print(10 >3)
# # print(4 >=7)
# # print(10<3)
# # print(5<=5)

# # print(3 == 3)
# # print(4 == 2)
# # print(3+4 == 7)

# # print(1 != 3) # 같지 않음
# # print(not(1 !=3)) #false

# # print((3>0) and (3< 5)) # true
# # print((3>0 )& (3<5)) #and 연산자
# # print((3>0) or (3>5))#or 연산자
# # print((3>0) | (3>5))#or 연산자

# # print(5>4>3)
# # print(5>4>7)
# # #숫자별 계산 순서
# # print(2+3*4)
# # print((2+3)*4)
# # #변수 적용
# # number= 2+3*4
# # print(number)
# # number=  number +2
# # print(number)
# # number +=2
# # print(number)
# # number *= 2
# # print(number)
# # number /=2
# # print(number)
# # number -=2
# # print(number)

# # number %= 5 #0
# # print(number)

# # #숫자 처리 함수
# # print(abs(-5)) #absolute 절댓값
# # print(pow(4,2)) #4의 제곱
# # print(max(5,12)) #최댓값
# # print(min(5,12)) #최솟값
# # print(round(3.14)) #3 반올림
# # print(round(4.99)) #5 반올림

# # from math import * #math 라이브러리 이용
# # print(floor(4.99)) #내림
# # print(ceil(3.14)) #올림
# # print(sqrt(16)) #제곱근

# # #랜덤 함수
# # from random import *

# # print(random()) #random 함수 사용 0.0~ 1.0 미만의 임의의 값을 생성
# # print(random() * 10 ) #random 함수 사용 0.0~ 10.0 미만의 임의의 값을 생성
# # print(int(random() * 10)) #random 함수 사용 0~ 10 미만의 임의의 값을 생성(소수점 삭제)
# # print(int(random() * 10)+1) #random 함수 사용 0~ 10 이하의 임의의 값을 생성(소수점 삭제 , 0은 안나오게 설정)

# # print(int(random()* 45)+1)# 1~45 이하의 임의값 생성

# # print(randrange(1,45)) # 1~ 45미만의 값 생성
# # print(randint(1,45)) # 1~45 이하의 임의의 값 생성

# #chapter 2 QUIZ

# from random import * #module 호출
# date= randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월" + str(date) +"일로 선정되었습니다")


# # 문자열
# sentence = '나는 소년입니다' 
# print(sentence)
# sentence2 = "파이썬은 쉽다" 
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요 
# """
# print(sentence3)

# #슬라이싱
# jumin= "990120-1234567"
# print("성별:" + jumin[7])
# print("년:"+jumin[0:2]) #0~2의 직전까지 즉 0~1까지 출력
# print("월:"+jumin[2:4])
# print("일:"+jumin[4:6])

# print("생년월일:"+jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리:"+jumin[7:14])
# print("뒤 7자리:"+jumin[7:]) #7자리부터 끝까지 출력
# print("뒤에서 부터 7자리:"+jumin[-7:]) #7자리부터 끝까지 출력

python ="python is amazing"
print(python.lower())
print(python.upper())
print(python[0].islower()) #첫글자가 소문자인지
print(python[0].isupper()) #첫글자가 대문자인지
print(len(python))
print(python.replace("python", "java")) # 변수에 대입되는 값을 바꿔줌

index = python.index("n")
print(index)
index = python.index("n", index +1)
print(index)

print(python.find("java")) #원하는 값이 없으면  -1을 반환함
# print(python.index("java")) #원하는 값이 없으면  error 

print(python.count("n")) #원하는 값이 없으면  -1을 반환함

#문자열 포맷 :문자열의 특정한위치에 특정한 값을 삽입시키는 기술
#방법1
print("a" + "b")
print("a", "b")
print("나는 %d살입니다" %20)
print("나는 %s를 좋아합니다" %"Python")
print("apple은 %a로 시작함" %"a")
#s
print("나는 %s살입니다" %20)
print("나는 %s색과 %s색을 좋아해요" %("파랑","빨강"))

#방법2
print("나는 {}살 입니다" .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파랑","빨강"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파랑","빨강")) 

#방법3 
print("나는 {age}살이며 , {color}색을 좋아해요".format(age=20,color="빨강"))
print("나는 {age}살이며 , {color}색을 좋아해요".format(color="빨강",age=20))

#방법4 (v 3.6이상)
age =30 
color ="빨강"
print(f"나는 {age}살이며 , {color}색을 좋아해요")

#탈출문자(줄바꿈) escape
print("백문이 불여일견\n백견이 불여일타")

#\" \"   \'\' 문장 내에서 따옴표를 표시
#저는 "나도코딩" 입니다
print("저는 \"나도 코딩입니다\"")
print("저는 \'나도 코딩입니다\'")

#\\ 문장 내에서 \ 표시
#ex)경로 표시  c:\\users\\python ~
#r 커서를 맨 앞으로 이동
print("red apple\rPine")

#b :백스페이스(한글자 삭제)
print("redd\b apple")

#t: 탭
print("red \tApple")

#Quiz )사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#ex) https://naver.com
#pw = "https://naver.com"
# pw = "https://daum.net"
pw = "https://google.com"
'''
print(pw)
print(pw[8:]) #규칙1 
'''
my_pw = pw.replace("https://" ,"") #규칙 1
# print(my_pw)
my_pw =my_pw[:my_pw.index(".")] #규칙 2
# my_pw[0:5] # 0 ~5 직전까지 (0,1,2,3,4)
# print(my_pw)
password = my_pw[:3] + str(len(my_pw)) + str(my_pw.count("e")) + "!" 
print("{0} 의 비밀번호는 {1} 입니다".format(pw, password))














