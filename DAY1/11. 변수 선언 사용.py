"""""
boolVar = True , intVar = 0 , floatVar = 0.0 , strVar = ""  #변수값 대입
type(boolVar), type(intVar), type(floatVar), type(strVar)
"""
#type()을 확인하면 boot(불형) int(정수)형 float(실수)형 str(문자열)형인지 확인할 수 잇음
#변수는 전에 있는 값을 무시하고 새로운 값으로 덮어씀
 
 #변수 1 : var2 = 200, var1= 100+100, var1= var2 + 100  var1은 300이 된다.
 #변수 2 : var1 = var2 = var3 = var4 = var5 = 100 이라는 변수를 생성하면 기존값은 모두 무시하고 100이된다.
 # 변수 3 : var1+200 오류가 발생할수 있으므로 처음에 var1=0 이런식으로 지정한 다음에 한다.
 """""
 myVar = 100
 type(myVar)
 myVar = 100.0
 type (myVar)
 """""
 