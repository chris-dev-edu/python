memo_list = []

def add_memo(memo):
    memo_list.append(memo)

def remove_memo(num):
    del memo_list[num-1]

def show_memo():
    if len(memo_list) == 0:
        print('저장된 메모가 없습니다')
    else:
        print('┏     메모 리스트 입니다')
        for index, memo in enumerate(memo_list):
            print(f'┃ [{index+1}] {memo_list[index]}')
        print('┖')
