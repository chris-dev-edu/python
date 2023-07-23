memo_list = []

def add_memo():
    new_memo = input('새로운 메모를 입력하세요: ')
    memo_list.append(new_memo)

def remove_memo():
    show_memo()

    number = int(input('삭제할 메모 번호를 입력하세요: '))
    del memo_list[number-1]

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
    return int(input('입력: '))