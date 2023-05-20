"""
1. 빈 Dictionary my_dict를 생성한다.
2. my_dict에 name, age, school, grade, phone-number key와 그에 맞게 이름, 나이, 학교, 학년, 전화번호를 넣는다.
3. my_dict를 print 한다
4. 위 과정을 진행하면 출력 결과가 다음과 같을 것이다. > {'name': 'chris', 'age': 20, 'school': 'Yonsei University', 'grade': 1, 'phone-number': '010-1234-5678'}
5. 출력 결과를 아래 처럼 개행되어 나오게 한다.

name : chirs
age : 20
school : Yonsei University
grade : 1
phone-number : 010-4500-9591

"""

my_dict = {}

my_dict['name'] = 'chris'
my_dict['age'] = 20
my_dict['school'] = 'Yonsei University'
my_dict['grade'] = 1
my_dict['phone-number'] = '010-1234-5678'

for key, value in my_dict.items():
    print(key, ":", value)