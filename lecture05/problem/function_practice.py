import time

# problem_number = 1
# a와 b의 합을 반환하는 함수
def add_numbers(a, b):
    return

# problem_number = 2
# a와 b의 곱을 반환하는 함수
def multiply_numbers(a, b):
    return

# problem_number = 3
# 1부터 n까지의 합을 반환하는 함수
def calculate_sum(n):
    return

# problem_number = 4
# n이 짝수라면 True, 홀수라면 False를 반환하는 함수
def is_even(n):
    return

# problem_number = 5
# 반지름 r인 원의 넓이를 구하는 함수(π = 3.141592)
def calculate_circle_area(r):
    return


def grade_function(problem_number):
    passed_test = 0
    total_test = 0
    testing = False
    types = []

    with open('test_case.txt', "r", encoding='utf-8') as file:
        func = ''
        for read in file:
            line = read.strip()

            if testing:
                time.sleep(0.1)
                print('.', end="")

                if len(line) == 0:
                    print(f'{passed_test}/{total_test} passed')
                    break

                variables = line.split()

                for i in range(len(types)):
                    if types[i] == 'int':
                        variables[i] = int(variables[i])
                    elif types[i] == 'bool':
                        variables[i] = variables[i] == 'True'
                    elif types[i] == 'float':
                        variables[i] = float(variables[i])

                if func in globals() and callable(globals()[func]):
                    f = globals()[func]
                    answer = f(*variables[:-1])

                    if answer == variables[-1]:
                        passed_test += 1

                total_test += 1

            else:
                try:
                    num, func_name, desc, t = line.split('%')
                    if int(num) == problem_number:
                        testing = True
                        func = func_name
                        print(f'{num}번 문제 {desc} 입니다')
                        types = t.split(',')
                except:
                    continue

for i in range(1,6):
    grade_function(i)