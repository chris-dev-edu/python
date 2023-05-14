"""
1. 아래 maze는 미로를 표시해놓은 2차원 List 이며, print_maze() 함수는 maze 상태를 print 해주는 함수이다.
2. 말의 현재 위치는 ✪로 표시한다.
3. 목적지는 E 이다.
4. 말은 한번에 한칸만 이동할 수 있다.
5. 칸을 이동할 때 마다 말의 위치를 변경해주고, 그 때의 maze상황을 print_maze()를 통해 표시한다.
6. 말이 최단 경로로 E까지 도착하게 하고, 이동 과정을 print한다.
"""
count = 0
maze = [
    ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
    ["■", "✪", " ", " ", " ", " ", " ", " ", " ", "■"],
    ["■", " ", "■", "■", "■", "■", " ", "■", " ", "■"],
    ["■", " ", " ", " ", " ", "■", " ", "■", " ", "■"],
    ["■", "■", " ", "■", " ", "■", "■", "■", " ", "■"],
    ["■", " ", " ", "■", " ", " ", " ", "■", " ", "■"],
    ["■", " ", "■", "■", "■", "■", " ", "■", "■", "■"],
    ["■", " ", " ", " ", "■", "■", " ", "■", "■", "■"],
    ["■", "■", "■", "■", "■", "■", " ", " ", "E", "■"],
    ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
]

def print_maze():
    global count
    count += 1
    print(f'[{count}]번째 이동 --------')
    for row in maze:
        for cell in row:
            print(cell, end=" ")
        print()
    print('--------------------')

maze[2][1] = '✪'
maze[1][1] = ' '
print_maze()

maze[3][1] = '✪'
maze[2][1] = ' '
print_maze()

maze[3][2] = '✪'
maze[3][1] = ' '
print_maze()

maze[3][3] = '✪'
maze[3][2] = ' '
print_maze()

maze[3][4] = '✪'
maze[3][3] = ' '
print_maze()

maze[4][4] = '✪'
maze[3][4] = ' '
print_maze()

maze[5][4] = '✪'
maze[4][4] = ' '
print_maze()

maze[5][5] = '✪'
maze[5][4] = ' '
print_maze()

maze[5][6] = '✪'
maze[5][5] = ' '
print_maze()

maze[6][6] = '✪'
maze[5][6] = ' '
print_maze()

maze[7][6] = '✪'
maze[6][6] = ' '
print_maze()

maze[8][6] = '✪'
maze[7][6] = ' '
print_maze()

maze[8][7] = '✪'
maze[8][6] = ' '
print_maze()

maze[8][8] = '✪'
maze[8][7] = ' '
print_maze()