"""
1. my_list1과 my_list2를 합치고 combined_list에 저장한다.
2. combined_list가 오름차순이 될 수 있도록 정렬한다.
3. combined_list를 print 한다.
"""

my_list1 = [1, 3, 5]
my_list2 = [2, 4, 8]

combined_list = my_list1 + my_list2
combined_list.sort()
print(combined_list)