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