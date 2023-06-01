sudoku = [
    [8, 0, 9, 0, 5, 0, 2, 1, 4],
    [0, 7, 2, 0, 4, 1, 5, 0, 0],
    [1, 0, 0, 8, 0, 2, 0, 0, 7],
    [0, 4, 0, 2, 0, 0, 0, 0, 6],
    [0, 0, 7, 4, 9, 6, 3, 5, 0],
    [0, 0, 0, 7, 0, 5, 4, 0, 8],
    [7, 1, 0, 3, 2, 9, 0, 0, 5],
    [0, 2, 0, 1, 6, 4, 8, 7, 0],
    [4, 0, 0, 0, 7, 8, 0, 0, 0],
]

num_of_zero = 38

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