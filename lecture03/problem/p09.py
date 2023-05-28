"""
반복문을 활용하여 아래와 같은 삼각형을 그려보시오.

    *
   **
  ***
 ****
*****
"""

for i in range(1, 10, 2):
    # 1, 3, 5, 7, 9 x
    # 1, 2, 3, 4, 5 5 - (x+1)//2
    # 4, 3, 2, 1, 0
    for j in range(5 - (i+1)//2):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()