class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.score = {}

    def set_score(self, subject, score):
        self.score[subject] = score

    def calculate_average_score(self):
        total_score = 0

        for score in self.score.values():
            total_score += score

        return total_score / len(self.score.keys())

    def __str__(self):
        student_report = ""

        for subject, score in self.score.items():
            student_report += f'{subject}: {score}점\n'

        return f'---------------\n' \
               f'이름: {self.name}\n' \
               f'학번: {self.student_id}\n\n' \
               f'{student_report}' \
               f'평균: {self.calculate_average_score()}점\n' \
               f'---------------'

    def __lt__(self, other):
        return self.calculate_average_score() < other.calculate_average_score()

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

sorted_students = sorted(students)

for student in sorted_students:
    print(student)