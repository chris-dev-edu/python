def add():
    a, b = get_two_numbers()
    show_result(a+b)

def subtract():
    a, b = get_two_numbers()
    show_result(a - b)

def multiply():
    a, b = get_two_numbers()
    show_result(a * b)

def divide():
    a, b = get_two_numbers()
    show_result(a / b)

def get_two_numbers():
    num1 = int(input('첫번째 수 입력: '))
    num2 = int(input('두번째 수 입력: '))

    return num1, num2

def show_result(result):
    print(f'계산 결과: {result}')

def show_option():
    print('\n\n┏ 원하는 기능을 골라주세요')
    print('┃ [1] 더하기')
    print('┃ [2] 빼기')
    print('┃ [3] 곱하기')
    print('┃ [4] 나누기')
    print('┃')
    print('┃ [9] 끝내기')
    print('┖━━━━━━━━━━━━━━━━━━━━━━')

    return int(input('입력: '))
