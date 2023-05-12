"""
1. 주어진 List에 3이라는 element를 추가한다.
2. 주어진 List의 4라는 element를 제거한다.
3. 주어진 List의 맨 뒤의 3개 element만 new_list라는 변수에 저장한다.
4. new_list를 print 한다.
"""
my_list = [1, 2, 4, 8, 16, 32, 64]

my_list.append(3)
my_list.remove(4)
new_list = my_list[-4:-1]
print(new_list)
