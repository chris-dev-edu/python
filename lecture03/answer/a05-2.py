"""
numbers는 5개의 숫자와 2개의 문자로 이루어진 리스트 이다.
sum이라는 변수에 0 값을 할당한 후
for문을 활용하여 numbers 안에 있는 숫자 값들만 모두 sum에 더해주어
numbers 리스트 내 element 들의 총 합을 출력하시오.
"""

numbers = [12, "KCD", 15, 756, "AB", 22, 34, 20]

sum = 0

for number in numbers:
    if type(number) == int:
        sum += number

print(sum)