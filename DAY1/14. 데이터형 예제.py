
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
