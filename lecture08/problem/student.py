class Student:
    def __init__(self, name, student_id):
        """
        name: 학생 이름, student_id: 학번을 파라미터로 받아서,
        클래스에 name, student_id 속성을 추가하시오.
        클래스에 score 라는 빈 Dictionary 속성을 추가하시오.
        """

    def set_score(self, subject, score):
        """
        subject: 과목명, score: 과목 점수를 파라미터로 받아서
        클래스의 score 속성에 subject, score 를 각각 key, value로 추가하시오
        """

    def calculate_average_score(self):
        """
        클래스의 속성 중 하나인 score Dictionary에는 과목-점수 를 key-value로 하는 데이터가 들어 있다
        전과목의 평균 점수를 return 하시오
        """

    def __str__(self):
        """
        클래스 객체를 print 했을 때, 아래와 같이 출력되도록 하시오.
        ---------------
        이름: Alice
        학번: 2021001

        수학: 85점
        영어: 90점
        사회: 78점
        과학: 95점
        평균: 87.0점
        ---------------
        """

    def __lt__(self, other):
        """
        __lt__ Magic Method는 클래스 간 sort 확인 시 self와 other중 어떤 객체의 값이 더 작은지를 판단하는 기준이 된다
        self 객체의 value < other 객체의 value 를 return 하시오.
        """


students_info = [
    {"name": "Alice", "student_id": "2021001", "수학": 85, "영어": 90, "사회": 78, "과학": 95},
    {"name": "Bob", "student_id": "2021002", "수학": 72, "영어": 88, "사회": 90, "과학": 65},
    {"name": "Charlie", "student_id": "2021003", "수학": 94, "영어": 85, "사회": 72, "과학": 80},
    {"name": "David", "student_id": "2021004", "수학": 78, "영어": 85, "사회": 92, "과학": 88}
]

subjects = ["수학", "영어", "사회", "과학"]

students = []

for info in students_info:
    student_obj = Student(info["name"], info["student_id"])

    for subject in subjects:
        student_obj.set_score(subject, info[subject])

    students.append(student_obj)

sorted_students = sorted(students, reverse=True)

for student in sorted_students:
    print(student)