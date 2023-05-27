"""
아래 scores에는 학생들의 점수가 리스트 형식으로 저장되어 있다.
학생들의 점수를 확인한 후 아래와 같은 평가를 부여한다.
- 90점 이상: A
- 80점 이상: B
- 70점 이상: C
- 70점 미만: F
점수를 부여한다.

학생들의 평가를 리스트로 만들어서, 해당 리스트를 출력하시오.
ex)
점수 = [57, 68, 78, 100, 77, 94, 82]
평가 = ['F', 'F', 'C', 'A', 'C', 'A', 'B']
"""

scores = [57, 68, 78, 100, 77, 94, 82]

result = []

for score in scores:
    if score >= 90:
        result.append("A")
    elif score >= 80:
        result.append("B")
    elif score >= 70:
        result.append("C")
    else:
        result.append("F")

print(result)