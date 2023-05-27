"""
아래 numbers는 숫자로 이루어진 리스트 이다.
sum = 0이라는 변수를 지정하여
numbers 를 순회하며, 0이 나오기 전까지 양수인 element만 더한 값을 sum에 저장하고
sum을 출력하시오.
"""

numbers = [1, 3, -2, -15, 67, -41, 9, 0, 22, 165, -312, 22]

sum = 0

for number in numbers:
    if number > 0:
        sum += number
    elif number < 0:
        continue
    else:
        break

print(sum)