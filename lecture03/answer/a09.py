"""
반복문을 활용하여 아래와 같은 삼각형을 그려보시오.

    *
   ***
  *****
 *******
*********
"""

for i in range(1, 10, 2):
    for j in range((10-i)//2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()