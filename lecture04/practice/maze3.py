import time

maze = [
    ['*', 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 'f']
]

icon = {
    '*': '*',
    0: '■',
    1: '□',
    'f': 'f',
}

count = 0

def print_maze(maze):
    global count
    count += 1
    print(f'<count: {count}>')

    for row in maze:
        for element in row:
            print(icon[element], end=" ")
        print()

my_point = [0, 0]

print_maze(maze)

while not maze[8][8] == '*':
    [prev_row, prev_col] = my_point

    if prev_row+1 < 9 and maze[prev_row+1][prev_col] != 0:
        my_point[0] += 1
    elif prev_col+1 < 9 and maze[prev_row][prev_col+1] != 0:
        my_point[1] += 1

    [next_row, next_col] = my_point

    maze[prev_row][prev_col] = 1
    maze[next_row][next_col] = '*'

    time.sleep(1)
    print_maze(maze)