import time

maze = [
    ['*', 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 'f']
]

icon = {
    '*': '*',
    0: '■',
    1: '□',
    'f': 'f',
}

row_range = range(len(maze))
col_range = range(len(maze[0]))
destination = []

for row_index, row in enumerate(maze):
    for column_index, element in enumerate(row):
        if element == 'f':
            destination = [row_index, column_index]

count = 0
def print_maze():
    time.sleep(1)
    print(f'<count: {count}>')
    for row in maze:
        for element in row:
            print(icon[element], end=" ")
        print()

print_maze()
final_routes = []
def find_route(prev_point, routes):
    global final_routes
    if prev_point[0] == destination[0] and prev_point[1] == destination[1]:
        final_routes = routes
    for [delta_r, delta_c] in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        next_point = [prev_point[0]+delta_r, prev_point[1]+delta_c]
        if next_point in routes:
            continue
        [next_row, next_col] = next_point
        if next_row in row_range and next_col in col_range and maze[next_row][next_col] in [1, 'f']:
            next_routes = [*routes]
            next_routes.append(next_point)
            find_route(next_point, next_routes)

find_route([0, 0], [[0, 0]])

for i in range(len(final_routes)-1):
    count += 1
    [prev_row, prev_col] = final_routes[i]
    [next_row, next_col] = final_routes[i+1]
    maze[prev_row][prev_col] = 1
    maze[next_row][next_col] = '*'
    print_maze()