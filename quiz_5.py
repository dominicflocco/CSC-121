
"""
Solutions to the programming problems from quiz #5.

Author: Dominic Flocco 
"""


def print_latin_square():
    """
    Prints a Latin Square of the specified order.
    """
    order = int(input("Enter the order of the Latin Square: "))

    for i in range(order):
        row = i
        for j in range(order):
            print(row, end=' ')
            row += 1
            if row == (order):
                row = 0
        print()
    

def count_visible():
    """
    Computes the number of visible trophies on a shelf, given their heights
    in order.
    """
    heights = eval(input("Enter trophy heights: "))
    
    num_visible = 0
    max_height = 0
    
    for i in range(len(heights)):
        height = heights[i]
        if height > max_height:
            num_visible += 1
            max_height = height
            
    print(num_visible)
    
    
    
    
