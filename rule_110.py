"""
This code executes a the Cellular Automation Rule 110.

Authors: Dominic Flocco and Sam Cascio

Time Spent: 3.5 hours

"""


def print_table(list1):
    
    """This function joins the list of lists to create the Cellular Automation table"""
    
    for i in range(len(list1)):
        table = ''.join(list1[i])
        print(table)
        
def run_rule_110(width, height):
    
    """This function execute Rule 110"""
    
    initial_seed = int(input("Enter seed index: "))
    
    while initial_seed > width:
        print("Error: seed index out of bounds, please try again!")
        initial_seed = int(input("Enter seed index: "))
        
    while initial_seed >= 0:
        if initial_seed >= width:
            print("Error: seed index out of bounds, please try again!")
            initial_seed = int(input("Enter seed index: "))
        
        else:
            first_row = []
            
            for i in range(width):
                if i == initial_seed:
                    first_row.append("$")
                else:
                    first_row.append(" ")
                    
            cell_auto = []
            cell_auto.append(first_row)
            for j in range(height):
                width_list = []
                for i in range(width):
                    width_list.append(" ")
            
                cell_auto.append(width_list)
            
            
            for i in range(1, height + 1):
                for j in range(width):
                    if j == width - 1:
                        right = 0
                        left = width - 2
                    elif j > 0 and j < (width - 1):
                        left = j-1
                        right = j+1
                    elif j == 0:
                        right = 1
                        left = width - 1
                        
                    if cell_auto[i-1][j] == "$" and cell_auto[i-1][left] == "$" and cell_auto[i-1][right] == "$":
                        cell_auto[i][j] = " "
                    elif cell_auto[i-1][j] == "$" and cell_auto[i-1][left] == "$" and cell_auto[i-1][right] == " ":
                        cell_auto[i][j] = "$"
                    elif cell_auto[i-1][j] == "$" and cell_auto[i-1][left] == " " and cell_auto[i-1][right] == "$":
                        cell_auto[i][j] = "$"
                    elif cell_auto[i-1][j] == "$" and cell_auto[i-1][left] == " " and cell_auto[i-1][right] == " ":
                        cell_auto[i][j] = "$"
                    elif cell_auto[i-1][j] == " " and cell_auto[i-1][left] == "$" and cell_auto[i-1][right] == "$":
                        cell_auto[i][j] = "$"
                    elif cell_auto[i-1][j] == " " and cell_auto[i-1][left] == "$" and cell_auto[i-1][right] == " ":
                        cell_auto[i][j] = " "
                    elif cell_auto[i-1][j] == " " and cell_auto[i-1][left] == " " and cell_auto[i-1][right] == "$":
                        cell_auto[i][j] = "$"
                    elif cell_auto[i-1][j] == " " and cell_auto[i-1][left] == " " and cell_auto[i-1][right] == " ":
                        cell_auto[i][j] = " "
        
            print_table(cell_auto)
            initial_seed = int(input("Enter seed index: "))

        

    

            