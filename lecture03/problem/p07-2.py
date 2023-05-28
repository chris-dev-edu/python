"""
아래 scores는 학생들의 이름을 key로, 점수를 value로 가지는 dictionary 이다.
학생들의 점수를 확인한 후 아래와 같은 평가를 부여한다.
- 90점 이상: A
- 80점 이상: B
- 70점 이상: C
- 70점 미만: F
점수를 부여한다.

학생들의 평가 점수를 확인하여
아래와 같이 출력되도록 하시오

뉴진스 멤버 minji학생의 성적은 F 입니다.
뉴진스 멤버 daniel학생의 성적은 F 입니다.
블랙핑크 멤버 jenny학생의 성적은 C 입니다.
에스파 멤버 karina학생의 성적은 A 입니다.
에스파 멤버 winter학생의 성적은 C 입니다.
블랙핑크 멤버 jisu학생의 성적은 A 입니다.
블랙핑크 멤버 risa학생의 성적은 B 입니다.
"""

scores = {
    'minji': 57,
    'daniel': 68,
    'jenny': 78,
    'karina': 100,
    'winter': 77,
    'jisu': 94,
    'risa': 82,
}

idol = {
    '뉴진스': ['minji', 'daniel'],
    '블랙핑크': ['jenny', 'jisu', 'risa'],
    '에스파': ['karina', 'winter'],
}