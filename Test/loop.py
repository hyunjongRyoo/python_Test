#for 반복문
for i in range(10):
    print("안녕하세요 반갑습니다")
 

# list 반복문
student =[1,2,3,4,5]

for a in student:
    print(a,"번의 학생 성적 처리 완료") 

# while 반복문 
b = 1
while b < 11:
    print(b)
    b +=1

#1~100 합 구하기
num =1
sum =0

while num <=100:
    sum += num 
    num += 1

print(sum)

#배열과 반복문
#배열 자체를 사용
arr=['사과', '바나나', '복숭아']
for i in arr:
    print(i)

#배열의 인덱스를 사용(for 문)

arr=['빵','우유','옥수수']
for i in range(0, len(arr)):
    print(arr[i])

#while 문 사용
arr=['김밥','라면','돈가스']
i=0
while i<len(arr):
    print(arr[i])
    i += 1 

#break를 사용한 흐름 제어문
#조건이 맞으면 루프를 탈출
length =[12.3 , 34.5, 56.7, 89.1]
for i in length:
    if(i<1.1 or i > 99.1):
        print("불량품입니다!(길이:",i,",mm)")
        break
    print(i,"mm")
print("검사 종료")

#continue
#조건이 맞으면 그 구문을 건너뛰고 계속 실행
length=[100.1 ,99.5 ,102.1 , 100.3, 98.9]

for i in length:
    if(i<98.5 or i>101.5):
        print("불량품 발생(길이: ",i,"mm)")
        continue
    print(i,"mm")
print("검사 종료")

#break continue차이 
#break는 루프를 빠져나오는것
#continue는 하나만 건너뛰고 선두로 돌아가 루프를 계속 실행
