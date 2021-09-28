
# 빼기 곱하기 나눗셈 구현
"""""
a = 100
b = 50
result= a+b
print (result)
print (a ,'+', b, '=', result)
result = a-b
print (a, '-', b, '=', result)
result = a*b
print (a, '*', b ,'=', result)
result = a/b
print (a, '/', b ,'=', result)
"""""

#내장된 라이브러리 사용
"""
import os
a = 100
b = 50
result= a+b
print (result)
print (a ,'+', b, '=', result)
result = a-b
print (a, '-', b, '=', result)
result = a*b
print (a, '*', b ,'=', result)
result = a/b
print (a, '/', b ,'=', result)
os.system ("Pause")
"""
# input() 키보드로 무언가를 입력하는 함수임
"""""
a=int(input ("첫번째 숫자 입력 :"))
b=int(input("두번째 숫자 입력 : "))
result = a+b
print (result)
"""""
#int 값을 무조건 정수로 변환하여 준다 input는 문자열만 변환하기 때문에 int를 같이 써야한다.
"""""
a = int(input("첫번째 숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))
result= a+b
print (result)
print (a ,'+', b, '=', result)
result = a-b
print (a, '-', b, '=', result)
result = a*b
print (a, '*', b ,'=', result)
result = a/b
print (a, '/', b ,'=', result)
"""""
# 거북이(터틀 프로그램) import turtle 파이썬에서 제공하는 터틀 프로그램
#turtle.forward 거북이가 가는 거리 #turtle.shape 거북이 모양  # turtle.done() fot문은 6장나갈때
"""""
import turtle
turtle.shape('turtle')
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.done()
"""""

"""""
import turtle       ## 함수 선언부분 ##
myT=None               ## 변수 선언부분 ##
myT = turtle.Turtle()
myT.shape('turtle')
for i in range(0, 5) :
    myT.forward(200)
    myT.right(72)
turtle.done()
"""
"""""
import turtle
import random
# 함수 선언             #def 함수명(매개변수) :
                        #    global 사용할_전역_변수

def screenLeftClick(x, y) :                    #screenLeftClick 함수 생성
    global r, g, b                          #빨강(r) 초록(g) 파랑(b) 변수 생성
    turtle.pencolor((r, g, b))             # 펜 색상
    turtle.pendown()                #거북이가 펜을 내리면서 이동(그려짐)
    turtle.goto(x, y)               # 거북이 이동
def screenRightClick(x, y) :
    turtle.penup()                     # 거북이가 펜을 들면서 이동(인그려짐)
    turtle.goto(x, y)
def screenMidClick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

# 변수 선언
pSize = 10
r, g, b = 0.0, 0.0, 0.0
#메인코드
turtle.title('거북이로 그림그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
"""
"""""
#print 함수 (출력)
print ("안녕하세요")
print ("100")
print ("--------------------------------------------------------")
print ("%d" % 100)
print ("100 + 100")
print ("%d" % (100+100))
# %d가 하나면 숫자도 하나여야 된다. 안그러면 오류가 발생한다.
# %d= 숫자
print ("--------------------------------------------------------")
#print 함수를 사용한 다양한 출력
print ("%d / %d = %d" % (100, 200, 0.5))
# 정수로 출력 된다.        %d %x %o는 정수 출력
# %f는 실수   # %c는 한 글자  # %s는 두글자 이상인 문자열
"""
"""""
print ("%d" % 123)
print ("%5d" % 123)
print ("%05d" % 123)

print ("%f" % 123.45)
print ("%7.1f" % 123.45)
print ("%7.3f" % 123.45)

print ("%s" % "Pytion")
print ("%10s" % "Pytion")
# %d는 숫자 자릿수 만큼 정렬함
# %5d는 오른쪽에 붙여서 정렬
# %0.5d는 오른쪽으로 붙여서 정렬하고 빈칸을 0으로 채움
#%f는 소수점 아래 6자리까지 무조건 출력
#%7.1f는 소수점 아래 첫째자리만 출력 둘째자리는 반올림
#%7.3f는 소수점 아래 셋째자리만 출력 오른쪽 빈칸은 0
#%s는 자릿수만큼 출력
#%10s는 10자리 확보 오른쪽 정렬

## format() 함수 {} 를 함께 사용
print ("%d %5d %05d" % (123, 123, 123))
print ("{0:d} {1:d} {2:05d}" .format (123, 123, 123))

## format() 함수 장점 : 출력 순서를 지정해 주어서 좋음
print ("{2:d} {1:d} {0:d} " .format (100, 200, 300))
## print() 문은 내용을 출력할때 한 행을 넘김
print ("한 행입니다. 또 한 행 입니다.")
print ("한 행입니다. \n 또 한 행 입니다.")
# 강제로 한행을 넘길땐 \n을 사용
"""
"""""
# \n 새로운 줄로 이동
# \t 다음 탭으로 이동
# \b 뒤로 한 칸 이동
# \\  \출력
#  \'  '출력
#  \"  "출력
print ("\n줄바꿈\n연습")
print ("\t 탭키\t연습")
print ("글자가 \"강조\"되는 효과1")
print ("글자가 \ '강조\' 되는 효과2 ")
print ("\\\\\\ 역슬래시 세 개 출력")
print (r"\n \t \" \\를 그대로 출력")
# r 형식은 이스케이프 문자까지도 그대로 출력한다.
print ("    *    ")
print ("   ***   ")
print ("  *****   ")
print (" ******** ")
print ("**********")
print (" ******** ")
print ("  *****   ")
print ("   ***   ")
print ("    *    ")
"""


"""""
boolVar = True , intVar = 0 , floatVar = 0.0 , strVar = ""  #변수값 대입
type(boolVar), type(intVar), type(floatVar), type(strVar)
"""
#type()을 확인하면 boot(불형) int(정수)형 float(실수)형 str(문자열)형인지 확인할 수 잇음
#변수는 전에 있는 값을 무시하고 새로운 값으로 덮어씀
 
 #변수 1 : var2 = 200, var1= 100+100, var1= var2 + 100  var1은 300이 된다.
 #변수 2 : var1 = var2 = var3 = var4 = var5 = 100 이라는 변수를 생성하면 기존값은 모두 무시하고 100이된다.
 # 변수 3 : var1+200 오류가 발생할수 있으므로 처음에 var1=0 이런식으로 지정한 다음에 한다.
 
"""
 myVar = 100
 type(myVar)
 myVar = 100.0
 type (myVar)
 """
#이진수 -> 십진수 앞에 0b를 붙임 0b(이진수)
"""""
0b10010001
print (0b10010001)
# int ('숫자' 진수) -> 10진수로 변환
int ('10010001', 2)
# 16진수는 앞에 0X를 붙이고 int() 함수를 쓸 수 있음. ;를 사용하면 두 명령을 이어줌
0x93; int ('93', 16)
"""""
# 파이썬은 hex() oct() bin()을 제공한다 hex는 결과를 16진수 oct는 8진수 bin은 2진수 출력

#프로 그램 구현
"""""
sel = int(input("입력 진수 결정 (16/10/8/2 ):"))
num = input("값 입력 :")
if sel == 16 :
    num10 = int(num, 16)
if sel == 10 :
    num10 = int(num, 10)
if sel == 8 :
    num10 = int(num, 8)
if sel == 2 :
    num10 = int(num, 2)

print ("16진수 ==>" , hex(num10))
print ("10진수 ==>" , num10)
print ("8진수 ==>" , oct(num10))
print ("2진수 ==>" , bin(num10))
"""""
"""""
#숫자형
# 정수
# a = 123 , type(a)를 실행하면 <class 'int'> 결과 출력 a에 123이라는 정수가 있기 때문에 int이다
a = 100 ** 100
print (a)           # int 크기에는 제한이 없다.
"정수형엔 2진수는 0B 8진수는 0O 16진수는 0X"
# 실수
#3.14 같은 소수점 있는 데이터인데 3.14e5로 표현이 가능
#  3.14e5는 3.14*10의 5승을 의미
a = 3.14
b = 3.14e5
print (a, b)

# 정수 실수 데이터 형은 사칙 연산이 가능
a = 10; b = 20
print (a+b, a-b, a*b, a/b)
# 제곱을 의미하는 **연산 나머지 구하는 %연산 소수점 버리는 // 연산 사용 가능
a, b = 9, 2
print (a **b, a%b, a//b)

# 불형 
# 참이나 거짓만 저장할 수 있는데 논리형이라고 함
a = type 
type(a)
a = (100 == 100)
b = (10 > 100)
print (a,b)

##문자열
a = "파이썬 만세"
a
print (a)
type (a)
# 큰 따움표나 작은따움표를 출력하고 싶으면 다른 따옴표로 묶으면 된다
"작은따옴표는 ' 모양이다"
'큰 따옴표는 " 모양이다.'

a = "이건 큰 따옴표 \" 모양."
b = "이건 작은따옴표 \' 모양."
print (a,b)

#문자열을 여러줄로 넣으려면 중간에 \n을 포함시키면 된다.
a = '파이썬 \n 만세'
print (a)
# 작은 따옴표나 큰 따옴표 3개를 연속해서 묶어도 된다.
a == """"파이썬"
"""""
#만세"""
"""""""""""""""
a
print(a)
## 함수 선언 부분 ##
def myFunc() :
    print ('함수를 호출함')
# 메인코드 부분
gVar = 100
if __name__ == '__main__' :
    print ('메인함수 부분이 실행됩니다.')
    myFunc()
    print ('전역 변수 값:', gVar)
    

#54행은 __name__ 변수에 __main__을 자동으로 설정하라는 의미이다.
#자세한건 9장에서 다룬다.

#자바처럼 코딩 하려면 54~58행을 다음과 같이 수정한다.

def main() :
    print ('메인 함수 부분이 실행됩니다.')
    myFunc()
    print ('전역 변수 값:', gVer )
if __name__ == '__main__' :
        main()
        """""
    
""""""""""
import sys

## 변수 선언 부분
intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

if __name__=="__main__" :
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print ('int형 기본크기 -->', sys.getsizeof(intVar))
    print ('float형 기본크기 -->', sys.getsizeof(floatVar))
    print ('bool형 기본크기 -->', sys.getsizeof(boolVar))
    print ('str형 기본크기 -->', sys.getsizeof(strVar))
    print ('list형 기본크기 -->', sys.getsizeof(listVar))
    print ('tuple형 기본크기 -->', sys.getsizeof(tupleVar))
    print ('dictionary형 기본크기 -->', sys.getsizeof(dictVar))
    print ('set형 기본크기 -->', sys.getsizeof(setVar))


## 데이터형 크기를 확인하기 위해 sys를 임포트 한다
## 데이터형 함수를 확인하는 전역변수 8개를 선언한다.
"""