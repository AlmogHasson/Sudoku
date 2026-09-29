import random
NOT_FINISH = 'NOT_FINISH'

example_board = \
[[5,3,-1,-1,7,-1,-1,-1,-1],
 [6,-1,-1,-1,-1,-1,1,-1,-1],
 [-1,-1,9,-1,-1,-1,-1,6,-1],
 [-1,-1,-1,-1,6,-1,-1,-1,3],
 [-1,-1,-1,8,-1,3,-1,-1,1],
 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
 [-1,6,-1,-1,-1,-1,-1,-1,-1],
 [-1,-1,-1,-1,1,-1,-1,-1,-1],
 [-1,-1,-1,-1,8,-1,-1,-1,9]]
perfect_board = [[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,7,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,9,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,8,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]]
impossible_board = [[5,1,6,8,4,9,7,3,2],
 [3,-1,7,6,-1,5,-1,-1,-1],
 [8,-1,9,7,-1,-1,-1,6,5],
 [1,3,5,-1,6,-1,9,-1,7],
 [4,7,2,5,9,1,-1,-1,6],
 [9,6,8,3,7,-1,-1,5,-1],
 [2,5,3,1,8,6,-1,7,4],
 [6,8,4,2,-1,7,5,-1,-1],
 [7,9,1,-1,5,-1,6,-1,8]]
bug_board = [[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,9],
 [1,9,8,3,4,2,5,6,7],
 [8,5,9,7,6,1,4,2,3],
 [4,2,6,8,5,3,7,9,1],
 [7,1,3,9,2,4,8,5,6],
 [9,6,1,5,3,7,2,8,4],
 [2,8,7,4,1,9,6,3,5],
 [3,4,5,2,8,6,1,7,9]]
interesting_board = [[5,3,4,6,7,8,9,1,2],
 [6,7,2,1,9,5,3,4,8],
 [1,9,8,3,4,2,5,6,7],
 [-1,-1,-1,7,6,1,4,2,3],
 [-1,-1,-1,8,5,3,7,9,1],
 [-1,-1,-1,9,2,4,8,5,6],
 [-1,-1,-1,-1,3,7,2,8,4],
 [-1,-1,-1,-1,1,9,6,3,5],
 [-1,-1,-1,-1,8,6,1,7,9]]
random_board =[[5,-1,-1,-1,7,-1,-1,-1,-1],
 [6,-1,-1,-1,-1,-1,1,-1,-1],
 [-1,-1,9,-1,-1,-1,-1,6,-1],
 [-1,-1,-1,-1,6,-1,-1,-1,3],
 [-1,-1,-1,8,-1,3,-1,-1,1],
 [-1,-1,-1,-1,-1,-1,-1,-1,-1],
 [-1,6,-1,-1,9,-1,-1,-1,-1],
 [-1,-1,-1,-1,1,-1,-1,-1,-1],
 [-1,-1,-1,-1,8,-1,-1,-1,-1]]



def get_square(loc: tuple) -> tuple:
    line = loc[0]
    col = loc[1]
    square_line = line // 3
    square_col = col // 3

    return square_line, square_col


def get_values_in_square(square: tuple, board: list) -> list:
    values_list = []
    square_line = square[0] * 3
    square_col = square[1] * 3

    for line in range(square_line, square_line + 3):
        for col in range(square_col, square_col + 3):
            if board[line][col] != -1:
                values_list.append(board[line][col])

    return values_list


def get_row_values(sudoku_board: list, loc: tuple) -> list:
    row_values = []
    row = loc[0]
    for option in sudoku_board[row]:
        if option != -1:
            row_values.append(option)

    return row_values


def get_col_values(sudoku_board: list, loc: tuple) -> list:
    col_values = []
    col = loc[1]
    for line in range(len(sudoku_board)):
        if sudoku_board[line][col] != -1:
            col_values.append(sudoku_board[line][col])

    return col_values

def is_legit(sudoku_board:list)->bool:
    for row in range(len(sudoku_board)):
        for col in range(len(sudoku_board)):
            loc = (row,col)
            col_values = get_col_values(sudoku_board,loc)
            row_values = get_row_values(sudoku_board,loc)
            square_values = get_values_in_square(get_square(loc),sudoku_board)

            found_col_set = set(col_values)
            found_row_set = set(row_values)
            found_square_set = set(square_values)

            if (len(col_values) != len(found_col_set)
                    or len(row_values) != len(found_row_set)
                    or len(square_values) != len(found_square_set)):
                return False


    return True


def options(sudoku_board: list, loc: tuple) -> list or None:
    cell_possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    line = loc[0]
    col = loc[1]

    if sudoku_board[line][col] != -1:
        return []

    row_values = get_row_values(sudoku_board, loc)
    col_values = get_col_values(sudoku_board, loc)
    square_values = get_values_in_square(get_square(loc), sudoku_board)

    # eliminate taken numbers in current row, col and 3x3 square
    for option in range(1, 10):
        if option in row_values or option in col_values or option in square_values:
            cell_possibilities.remove(option)

    if len(cell_possibilities) == 0:
        return None

    return cell_possibilities


def possible_digits(sudoku_board: list) -> list:
    board_options = []

    for line in range(len(sudoku_board)):
        board_options.append([])
        for col in range(len(sudoku_board)):
            board_options[line].append(options(sudoku_board, (line, col)))

    return board_options


def one_stage(sudoku_board: list, possibilities: list)->tuple or str:
    minimal_len = 10
    minimal_coordinate = ()
    for line in range(len(sudoku_board)):
        for col in range(len(sudoku_board)):
            # if there are no options(None) and theres -1, there's a prob in the board
            if possibilities[line][col] is None:
                return 'FINISH_FAILURE'

            # if there's a single possibility update board and possible_digits,
            # recursively keep filling the board for this rule
            possibility_len = len(possibilities[line][col])
            if possibility_len == 1:
                sudoku_board[line][col] = possibilities[line][col][0]
                possibilities = possible_digits(sudoku_board)
                result = one_stage(sudoku_board,possibilities)
                return result

            # keep the minimal options cell coordinate
            elif possibility_len > 1 and (possibility_len < minimal_len):
                minimal_len = possibility_len
                minimal_coordinate = (line,col)


    if minimal_len == 10 :
        return 'FINISH_SUCCESS'

    return minimal_coordinate, NOT_FINISH



def fill_board( sudoku_board:list, possibilities:list) -> tuple or str:
    result = one_stage(sudoku_board,possibilities)

    while result[1] == NOT_FINISH:
        minimal_coordinate = result[0]
        line = minimal_coordinate[0]
        col = minimal_coordinate[1]
        current_possibilities = possibilities[line][col]
        new_value = int(input('Fill in the coordinate '+ str(minimal_coordinate) +
                        ' with one of the following options: ' + str(current_possibilities)))

        while new_value not in current_possibilities:
            new_value = int(input('You must choose one of the following options: ' + str(current_possibilities)))

        sudoku_board[line][col] = new_value
        possibilities = possible_digits(sudoku_board)
        result = one_stage(sudoku_board,possibilities)

    return result


def create_random_board(sudoku_board:list)->str or None:
    n = random.randrange(10, 20) #12
    sudoku_cells = [(row, col) for row in range(9) for col in range(9)] #81
    k = len(sudoku_cells) #81

    # reset given board
    for row in range(9):
        for col in range(9):
            sudoku_board[row][col] = -1


    for cell in range(n):
        random_cell_index = random.randrange(1,k)
        random_loc = sudoku_cells.pop(random_cell_index)
        cell_possibilities = options(sudoku_board,random_loc)
        if cell_possibilities is None:
            return "Unsolvable Board"

        #cell = random option from the list by giving a random index of the list cell_possibilities
        sudoku_board[random_loc[0]][random_loc[1]] = cell_possibilities[random.randrange(len(cell_possibilities))]
        k -= 1

    return


def print_board(sudoku_board:list)->None:
    print("-------------------")
    for row in range(len(sudoku_board)):
        row = str(sudoku_board[row])
        row = (row.replace(" ","|")
               .replace("[","|")
               .replace("]","|")
               .replace(",","")
               .replace("-1"," "))
        print(str(row))
        print("-------------------")

    return None


def print_board_to_file(sudoku_board:list, file_name:str)->None:
    with open(file_name,"a") as f:
        f.write("-------------------\n")
        for row in range(len(sudoku_board)):
            row = str(sudoku_board[row])
            row = (row.replace(" ","|")
                   .replace("[","|")
                   .replace("]","|")
                   .replace(",","")
                   .replace("-1"," "))
            f.write(row + "\n")
            f.write("-------------------\n")

    return None


create_random_board(random_board)
board = [example_board,perfect_board,impossible_board,bug_board,interesting_board,random_board]

for b in board:
    if is_legit(b):
        res = fill_board(b,possible_digits(b))
        if res == "FINISH_FAILURE":
            with open("solved_sudoku.txt", "a") as f:
                f.write("Board is unsolvable\n")
        else:
            with open("solved_sudoku.txt", "a") as f:
                f.write("Here is the solved board\n")
            print_board_to_file(b,"solved_sudoku.txt")
    else:
        with open("solved_sudoku.txt","a") as f:
            f.write("Board is not legit!\n")
