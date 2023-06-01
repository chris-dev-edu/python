sudoku = [
    [0, 3, 5, 4, 6, 9, 2, 7, 8],
    [7, 8, 2, 1, 0, 5, 6, 0, 9],
    [0, 6, 0, 2, 7, 8, 1, 3, 5],
    [3, 2, 1, 0, 4, 6, 8, 9, 7],
    [8, 0, 4, 9, 1, 3, 5, 0, 6],
    [5, 9, 6, 8, 2, 0, 4, 1, 3],
    [9, 1, 7, 6, 5, 2, 0, 8, 0],
    [6, 0, 3, 7, 0, 1, 9, 5, 2],
    [2, 5, 8, 3, 9, 4, 7, 6, 0],
]

num_of_zero = 14

while num_of_zero > 0:
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for x in range(9):
                    if sudoku[r][x] in candidate:
                        candidate.remove(sudoku[r][x])
                    if sudoku[x][c] in candidate:
                        candidate.remove(sudoku[x][c])
                for x in range(3):
                    for y in range(3):
                        if sudoku[r//3 * 3 + x][c//3 * 3 + y] in candidate:
                            candidate.remove(sudoku[r//3 * 3 + x][c//3 * 3 + y])
                if len(candidate) == 1:
                    sudoku[r][c] = candidate[0]
                    num_of_zero -= 1

for row in sudoku:
    for element in row:
        print(element, end=" ")
    print()