
"""
Solutions to the programming problems from quiz #9.

Author: Dominic Flocco 
"""

def pretty_print(board):
    """ Prints a Minesweeper board in a human-friendly format.

    If the input board is None, then no output is produced.

    Parameters:
        board - a list of strings representing the board to be printed.

    Returns:
        None.
    """
    if (board != None):
        for row in board:
            print(row)



def solve_board(board):
    """ Solves the given Minesweeper board.

    Solving a board involves replacing all occurrences of . in the original
    board description with a single digit between 0-8 indicating how many of
    that cell's neighbors contain mines.

    Parameters:
        board - a list of strings describing a Minesweeper board. Each string
                is made up of .s and *s, with the former indicating empty
                cells and the latter indicating mines.

    Returns:
        A list of strings, where each . in one of the original strings has
        been replaced with a digit between 0-8, denoting the number of
        adjacent cells that contain a mine.
    """
    
    board_list = []
    for i in range(len(board)):
        small_board_list = []
        for j in range(len(board[0])):
            small_board_list.append(board[i][j])
        board_list.append(small_board_list)
    
    for i in range(len(board_list)):
        for j in range(len(board_list[0])):
            if board_list[i][j] == "*":
                board_list[i][j] = "*"
            elif board_list[i][j] == ".":
                adjacent = 0
                try:
                    if board_list[i][j+1] == "*": # over 1
                        adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i][j-1] == "*": # back 1
                        if (j - 1) < 0:
                            adjacent += 0 
                        else:
                            adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i-1][j] == "*": # up 1
                        if (i - 1) < 0:
                            adjacent += 0 
                        else:
                            adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i+1][j] == "*": # down 1
                        adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i+1][j+1] == "*": # down 1 over 1
                        adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i+1][j-1] == "*": # down 1 back 1
                        if (j - 1) < 0:
                            adjacent += 0 
                        else:
                            adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i-1][j-1] == "*": # up 1 back 1
                        if (j - 1) < 0 or (i - 1) < 0:
                            adjacent += 0 
                        else:
                            adjacent += 1
                except IndexError:
                    adjacent += 0
                try:
                    if board_list[i-1][j+1] == "*": # up 1 over 1
                        if (i - 1) < 0:
                            adjacent += 0 
                        else:
                            adjacent += 1
                except IndexError:
                    adjacent += 0
                board_list[i][j] = str(adjacent)
    
    final_board_list = []
    for i in range(len(board_list)):
        final_board_list.append(''.join(board_list[i]))
        
    return final_board_list
                

def main():
    """ Tester function. """
    print()
    print("Testing solve_board")
    print()
    solved = solve_board(["..",
                          ".*",
                          ".."])
    pretty_print(solved)
    print()

    solved = solve_board(["*.*.*",
                          "..*..",
                          "*****",
                          ".....",
                          "..**."])
    pretty_print(solved)
    print()


if __name__ == "__main__":
    main()
