"""
1. A, B라는 이름의 set을 각각 만든다
2. A에는 50 이하의 짝수, B에는 50 이하의 자연수 중 3의 배수가 아닌 수를 넣는다.
3. A ∩ B, A ∪ B, A - B, B - A 값을 각각 계산하여 출력한다.
"""

A = set()
B = set()

for i in range(1, 51):
    if i % 2 == 0:
        A.add(i)

    if i % 3 != 0:
        B.add(i)

intersection = A.intersection(B)
union = A.union(B)
differenceA_B = A.difference(B)
differenceB_A = B.difference(A)

print("A ∩ B", intersection)
print("A ∪ B", union)
print("A - B", differenceA_B)
print("B - A", differenceB_A)