
"""
Solution to the Magic Square problem from the CSC 121 Final Exam.

Author: Dominic Flocco 
"""

def is_magic_square(square):
    """Returns whether the supplied nested list is a magic square

    Args:
        square - a nested list of integers, with the same number of rows as
                 columns

    Returns:
        True if and only if 'square' is magic, and False otherwise.
    """
    
    top_bottom = 0
    bottom_top = 0
    
    for row in range(len(square)):
        top_bottom += square[row][row]
    for row in range(len(square)):
        bottom_top += square[(len(square) - 1) - row][row]
    
    row_sum_list = []
    
    for row in range(len(square)):
        row_sum = 0
        for col in range(len(square)):
            row_sum += square[row][col]
        row_sum_list.append(row_sum)
        
    col_sum_list = []
    
    for col in range(len(square[0])):
        col_sum = 0
        for row in range(len(square)):
            col_sum += square[row][col]
        col_sum_list.append(col_sum)   
    
    max_col_sum = max(col_sum_list)
    min_col_sum = min(col_sum_list)
    max_row_sum = max(row_sum_list)
    min_row_sum = min(row_sum_list)    
    
    if (top_bottom == bottom_top == max_col_sum == min_col_sum
        == max_row_sum == min_row_sum):
        return True
    else:
        return False
    
def main():
    """ Tester function """
    print(is_magic_square([[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 8]]))      # should print True
    print(is_magic_square([[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 9]]))      # should print False
    print(is_magic_square([[9, 6, 3, 16],
                           [4, 15, 10, 5],
                           [14, 1, 8, 11],
                           [7, 12, 13, 2]])) # should print True

    # feel free to add more test cases here!


if __name__ == "__main__":
    main()
