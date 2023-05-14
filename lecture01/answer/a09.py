"""
1. prime_numbers 리스트를 만들어서 1 ~ 100 총 100개의 수를 넣어준다.
2. 1을 prime_numbers 에서 뺀다
3. 2를 제외한 2의 배수를 prime_numbers 에서 뺀다.
4. 3, 5, 7을 제외한 3, 5, 7의 배수를 prime_numbers 에서 뺀다
5. prime_number 와 길이를 출력한다.
"""

prime_numbers = []
for i in range(1, 101):
    prime_numbers.append(i)

prime_numbers.remove(1)

for i in [2, 3, 5, 7]:
    multiply = 2
    while i * multiply <= 100:
        if i*multiply in prime_numbers:
            prime_numbers.remove(i*multiply)
        multiply += 1

print(prime_numbers)
print(len(prime_numbers))