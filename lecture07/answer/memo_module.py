memo_list = []

def load_memo():
    try:
        with open('memo_data.txt', 'r', encoding='utf-8') as file:
            for read in file:
                line = read.strip()
                memo_list.append(line)
    except FileNotFoundError:
        print("저장된 메모를 불러올 수 없습니다.")

def save_memo():
    try:
        with open('memo_data.txt', 'w', encoding='utf-8') as file:
            for memo in memo_list:
                file.write(memo + '\n')
            file.close()
    except IOError:
        print("메모를 저장하는 중 에러가 발생했습니다.")
def add_memo():
    new_memo = input('새로운 메모를 입력하세요: ')
    memo_list.append(new_memo)
    save_memo()

def remove_memo():
    show_memo()

    number = int(input('삭제할 메모 번호를 입력하세요: '))

    try:
        del memo_list[number-1]
    except IndexError:
        print("해당 번호의 메모는 존재하지 않습니다.")

    save_memo()

def show_memo():
    if len(memo_list) == 0:
        print('저장된 메모가 없습니다')
    else:
        for i, memo in enumerate(memo_list):
            print(f'[{i + 1}] {memo}')

def show_option():
    print('\n\n┏ 원하는 기능을 골라주세요')
    print('┃ [1] 메모 확인')
    print('┃ [2] 메모 추가')
    print('┃ [3] 메모 삭제')
    print('┃')
    print('┃ [9] 끝내기')
    print('┖━━━━━━━━━━━━━━━━━━━━━━')

    try:
        selected_option = int(input('입력: '))
        return selected_option
    except (ValueError, TypeError):
        print("1, 2, 3, 9 중의 수를 입력해주세요")

load_memo()