"""
아래 코드를 실행하면, 여러개의 정수를 입력받아 numbers 리스트에 저장하게 된다.
sum = 0이라는 변수를 지정하여
numbers 를 뒤에서부터 거꾸로 순회하며, 0이 나오기 전까지 양수인 element만 더한 값을 sum에 저장하고
sum을 출력하시오.
"""

numbers = []

number = 0
while True:
    number = input("정수를 입력하세요(\"숫자가 아닌경우 더이상 입력을 받지 않습니다\")")
    if type(number) == int:
        numbers.append(int(number))
    else:
        break