import calculator_module as calc
import memo_module as memo

menu = 0
option = 0


def reset():
    global menu, option
    menu = 0
    option = 0


def show_menu():
    global menu

    print('\n\n┏ 원하는 기능을 골라주세요')
    print('┃ [1] 계산기')
    print('┃ [2] 메모장')
    print('┃')
    print('┃ [9] 끝내기')
    print('┖━━━━━━━━━━━━━━━━━━━━━━')

    menu = int(input("입력: "))


def select_calculator():
    print('\n┏ 원하는 기능을 골라주세요')
    print('┃ [1] 더하기')
    print('┃ [2] 빼기')
    print('┃ [3] 곱하기')
    print('┃ [4] 나누기')
    print('┃ [9] 끝내기')
    print('┖━━━━━━━━━━━━━━━━━━━━━━┚')

    option = int(input("입력: "))

    return option


def input_two_numbers():
    print('두 수를 입력하세요')
    num1 = int(input('수1: '))
    num2 = int(input('수2: '))

    return num1, num2


def show_result(result):
    print(f'계산 결과: {result}')

def select_memo():
    print('\n┏ 원하는 기능을 골라주세요')
    print('┃ [1] 메모 확인')
    print('┃ [2] 메모 추가')
    print('┃ [3] 메모 삭제')
    print('┃ [9] 끝내기')
    print('┖━━━━━━━━━━━━━━━━━━━━━━┚')

    option = int(input("입력: "))

    return option

while True:
    if menu == 0:
        show_menu()
    elif menu == 1:
        if option == 0:
            option = select_calculator()
        elif option == 9:
            reset()
        else:
            num1, num2 = input_two_numbers()
            result = 0
            if option == 1:
                result = calc.add(num1, num2)
            elif option == 2:
                result = calc.subtract(num1, num2)
            elif option == 3:
                result = calc.multiply(num1, num2)
            else:
                result = calc.divide(num1, num2)

            show_result(result)
            reset()
    elif menu == 2:
        if option == 0:
            option = select_memo()
        elif option == 9:
            reset()
        elif option == 1:
            memo.show_memo()
            option = 0
        elif option == 2:
            new_memo = input('메모를 입력하세요: ')
            memo.add_memo(new_memo)
            option = 0
        elif option == 3:
            memo.show_memo()
            memo_num = int(input('삭제할 메모 번호를 입력하세요: '))
            memo.remove_memo(memo_num)
            option = 0

    else:
        break
