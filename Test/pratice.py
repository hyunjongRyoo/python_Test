#자료형
#숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 4)
print(3*(3+1))
#문자
print('풍선')
print("풍선")
print("z"* 9)
print(5 > 10)
print(5 < 10)
#boolean
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
#변수
animal ="개"
name ="연탄이"
age = 4 
hobby = "산책"
is_adult = age >=3 
print("우리집 "+ animal +"의 이름은" + name + "예요")
hobby = "공놀이"
# print( name + "는" + str(age) + "살이며" +hobby+"을 아주 좋아합니다")
print( name , "는" , str(age) ,"살이며" ,hobby,"을 아주 좋아합니다")
print(name +"는 어른일까요?" + str(is_adult))
#주석
'''  
전체적으로 주석처리 하고싶으면 작은 따옴표 3개 
'''
# 문장 전체 선택후 command / 주석처리

# QUIZ CHATER 1
station = "사당"
print(station +"행 열차가 들어오고 있습니다")

#연산자
print(1+1)
print(3-2)
print(5*2)
print(6/2)

print(2**3) #2의 3제곱
print(5%3) #나머지 구하기 2 
print(10%3) 
print(5//3) #몫 구하기 1 
print(10//3) #몫 구하기 3

print(10 >3)
print(4 >=7)
print(10<3)
print(5<=5)

print(3 == 3)
print(4 == 2)
print(3+4 == 7)

print(1 != 3) # 같지 않음
print(not(1 !=3)) #false

print((3>0) and (3< 5)) # true
print((3>0 )& (3<5)) #and 연산자
print((3>0) or (3>5))#or 연산자
print((3>0) | (3>5))#or 연산자

print(5>4>3)
print(5>4>7)
#숫자별 계산 순서
print(2+3*4)
print((2+3)*4)
#변수 적용
number= 2+3*4
print(number)
number=  number +2
print(number)
number +=2
print(number)
number *= 2
print(number)
number /=2
print(number)
number -=2
print(number)

number %= 5 #0
print(number)

#숫자 처리 함수
print(abs(-5)) #absolute 절댓값
print(pow(4,2)) #4의 제곱
print(max(5,12)) #최댓값
print(min(5,12)) #최솟값
print(round(3.14)) #3 반올림
print(round(4.99)) #5 반올림

from math import * #math 라이브러리 이용
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

#랜덤 함수
from random import *

print(random()) #random 함수 사용 0.0~ 1.0 미만의 임의의 값을 생성
print(random() * 10 ) #random 함수 사용 0.0~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) #random 함수 사용 0~ 10 미만의 임의의 값을 생성(소수점 삭제)
print(int(random() * 10)+1) #random 함수 사용 0~ 10 이하의 임의의 값을 생성(소수점 삭제 , 0은 안나오게 설정)

print(int(random()* 45)+1)# 1~45 이하의 임의값 생성

print(randrange(1,45)) # 1~ 45미만의 값 생성
print(randint(1,45)) # 1~45 이하의 임의의 값 생성

#chapter 2 QUIZ

from random import * #module 호출
date= randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) +"일로 선정되었습니다")












