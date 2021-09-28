#int 값을 무조건 정수로 변환하여 준다 input는 문자열만 변환하기 때문에 int를 같이 써야한다.

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
