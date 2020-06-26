
"""
Solutions to the programming problems from quiz #4.

Author: Dominic Flocco
"""

def draw_staircase():
    """Prints a staircase composed of `*' signs with user-specified dimensions.

    Here's an example:

    height = 5, width = 3
    * * *
    . . * * *
    . . . . * * *
    . . . . . . * * *
    . . . . . . . . * * *
    """
    height = int(input("Enter the height of the staircase: "))
    width = int(input("Enter the width of the staircase: "))

    for i in range(height):
        for k in range(i * (width - 1)):
            print(".", end=' ')
        for j in range(width):
            print("*", end=' ')
        
        print(" ")

def approximate_pi():
    """
    Computes an approximation to pi using the Leibniz formula.
    """
    num_terms = int(input("How many terms would you like to use? "))
    
    len_list = num_terms // 2
    pi_list_one = [1] 
    pi_list_two = [3]
    pi_list = []
    
    for i in range(len_list):
        pi_list_one.append(((i + 1) * 4) + 1)
        
    for i in range(len_list):
        pi_list_two.append(((i + 1) * 4) + 3)
        
    for i in range(len_list):
        pi_list.append((1/pi_list_one[i]) - (1/pi_list_two[i]))
    
    pi = 4 * (sum(pi_list))
    print(pi)
            
        
    
