"""
아래의 코드를 실행하면, num1, num2, num3 변수에 각각 숫자 세개를 입력받는다.
세개의 숫자 중 가장 큰 수를 print하는 코드를 작성하시오.
"""

num1 = int(input("첫번째 숫자를 입력하세요: "))
num2 = int(input("두번째 숫자를 입력하세요: "))
num3 = int(input("세번째 숫자를 입력하세요: "))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)