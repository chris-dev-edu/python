import calculator_module as cal
import memo_module as memo

menu = 0

def show_menu():
    print('\n\n┏ 원하는 기능을 골라주세요')
    print('┃ [1] 계산기')
    print('┃ [2] 메모장')
    print('┃')
    print('┃ [9] 끝내기')
    print('┖━━━━━━━━━━━━━━━━━━━━━━')

    return int(input('입력: '))

while menu != 9:
    if menu == 1:
        option = 0

        while option != 9:
            if option in [1, 2, 3, 4]:
                if option == 1:
                    cal.add()
                elif option == 2:
                    cal.subtract()
                elif option == 3:
                    cal.multiply()
                else:
                    cal.divide()
                option = 0
            else:
                option = cal.show_option()

        menu = 0
    elif menu == 2:
        option = 0

        while option != 9:
            if option in [1, 2, 3]:
                if option == 1:
                    memo.show_memo()
                elif option == 2:
                    memo.add_memo()
                elif option == 3:
                    memo.remove_memo()
                option = 0
            else:
                option = memo.show_option()
        menu = 0
    else:
        menu = show_menu()