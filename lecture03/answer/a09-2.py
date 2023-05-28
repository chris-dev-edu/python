"""
반복문을 활용하여 아래와 같은 삼각형을 그려보시오.

          *
        ***
      *****
    *******
  *********
***********
"""

for i in range(1, 12, 2):
    for a in range(11-i):
        print(" ", end="")
    for b in range(i):
        print("*", end="")
    print()