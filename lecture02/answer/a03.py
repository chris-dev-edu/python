"""
1. 빈 Dictionary my_dict를 생성한다.
2. my_dict에 name, age, school, grade, phone-number key와 그에 맞게 이름, 나이, 학교, 학년, 전화번호를 넣는다.
3. my_dict를 print 한다
4. 1년이 지나 2024년이 되었다. 나의 나이를 한살 올린 후 my_dict를 다시 print 한다
"""

my_dict = {}

my_dict['name'] = 'chris'
my_dict['age'] = 20
my_dict['school'] = 'Yonsei University'
my_dict['grade'] = 1
my_dict['phone-number'] = '010-1234-5678'

print(my_dict)

my_dict['age'] += 1

print(my_dict)