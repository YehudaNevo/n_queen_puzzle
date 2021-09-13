import numpy as np

# --parameters ------

columns = []
indexers = []
size = int(input('please enter size of the board \n'))
board = np.zeros((size, size))


#  -- FUNCTION ---------------------------


def display(columns, size):
    for row in range(size):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()
    print()


def creat_board(n):
    return np.zeros((n, n))


def change_queen(board, location, add_or_remove_threat):  # location = [row , column]

    column = location[1]
    row = location[0]
    left = column - 1  # left diagonal adding
    right = column + 1  # right diagonal adding

    board[row] += add_or_remove_threat

    for i in range(row + 1, len(board)):
        if left < 0:
            break
        board[i][left] += add_or_remove_threat
        left -= 1

    left = column - 1
    for i in range(0, row):
        if left < 0:
            break
        board[row - 1 - i][left] += add_or_remove_threat
        left -= 1

    for i in range(row + 1, len(board)):
        if right >= len(board):
            break
        board[i][right] += add_or_remove_threat
        right += 1

    right = column + 1
    for i in range(0, row):
        if right >= len(board):
            break
        board[row - 1 - i][right] += add_or_remove_threat
        right += 1

    # sign the columns
    for i in range(0, len(board)):
        board[i][column] += add_or_remove_threat

    return board


def next_row_is_safe(column):
    row = len(columns)
    return board[row][column] == 0


def place_in_next_row(column, rand_columns):
    row = len(columns)
    change_queen(board, [row, rand_columns[column]], 1)
    columns.append(rand_columns[column])
    indexers.append(column)


def remove_in_current_row(rand_columns):
    if len(columns) > 0:
        column = indexers.pop()
        columns.pop()
        row = len(columns)
        change_queen(board, [row, rand_columns[column]], -1)
        return column
    return -1


def solve_queen_forword_checking(size):
    columns.clear()
    indexers.clear()
    board = np.zeros((size, size))

    rand_columns = np.arange(size)
    np.random.shuffle(rand_columns)

    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    row = 0
    # iterate over rows of board
    column = 0
    while True:
        # place queen in next row
        while column < size:
            number_of_iterations += 1
            if next_row_is_safe(rand_columns[column]):
                place_in_next_row(column, rand_columns)
                number_of_moves += 1  # add queen
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if column == size or row == size:
            number_of_iterations += 1
            # if board is full, we have a solution
            if row == size:
                print("I did it! Here is my solution")
                display(columns, size)
                print(number_of_moves)
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row(rand_columns)
            number_of_moves += 1  # remove queen
            if (prev_column == -1):  # I backtracked past column 1
                print("There are no solutions")
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column
