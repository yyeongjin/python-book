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