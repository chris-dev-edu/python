"""
1. 주어진 두개의 List를 합치고, combined_list라는 변수에 저장한다.
2. combined_list를 print 한다.
Hint: list를 합치는 방법을 배운적 있는지 생각해보세요. (없다면 어디선가 찾아봐야겠죠? 모르는 내용을 찾아보는 능력도 실력입니다.)
"""
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

# 정답1
# combined_list = my_list1 + my_list2
# print(combined_list)

# 정답2
# combined_list = [*my_list1, *my_list2]
# print(combined_list)

# #정답3
# my_list1.extend(my_list2)
# combined_list = my_list1
# print(combined_list)