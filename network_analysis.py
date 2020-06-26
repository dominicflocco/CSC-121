"""

Authors: Dominic Flocco and Savanna Vest

Time spent: 3 hours

This code will return the name of the "most central" individual
from a set of people and their organizations involved in the
revolutionary movement in and around Boston in the 1770s. The
most central person is determined by calculating which individual
of the dataset was involved with the most organizations and networked
with the most people. We use lists of the given data to create matrices
to calculate who this individual is.

"""

def find_most_central(filename):
    """
    This function is our main function that calls the helper functions and
    specifically returns the helper function that returns the name of the
    most central person.

    Parameters:
        filename - accepts the name of a file input by the user

    Returns:
        the name of the most central person
        if an error occurs in opening a file, it returns an empty string
    """
    
    try:
        text = read_file(filename)
    except IOError:
        print("There was a problem reading the file. Try again!")
        return ""
    
    name_list = create_name_list(text)
    matrix_A = create_matrix_A(text)
    matrix_AT = create_matrix_AT(matrix_A)
    A_AT = multiply_matricies(matrix_AT, matrix_A)
    
    return calculate_centrality(A_AT, name_list)
    
    
def read_file(filename):
    """
    This function reads the file and formats the text as a list
    so that it is more easily usable in the code.

    Parameters:
        filename - accepts the name of a file input by the user
    Returns:
        text as a list
    """
    
    with open(filename, "r") as input_file:
        words = input_file.readlines()
    text = []
    for i in range(len(words)):
        text.append(words[i].split(","))
        
    return text

def create_name_list(text):
    """
    This function extracts the first position from each list in order
    to save the name of each revolutionary person in a new "name_list".

    Parameters:
        text - text as a list
        
    Returns:
        name_list - saves the names from "text" in alphabetical order
    """
    
    name_list = []
    
    for i in range(1, len(text)):
        name_list.append(text[i][0])
        

    return name_list
            
def create_matrix_A(text):
    """
    This function creates the first matrix of the data taken from "text".

    Parameters:
        text - text as a list
        
    Returns
        matrix_A - the data of each revolutionary person saved as a list
    """
    
    matrix_A = []
    
    for i in range(1, len(text)):
        A_small_list = []
        for j in range(1, len(text[1])):
            A_small_list.append(text[i][j])
        matrix_A.append(A_small_list)
    for i in range(len(matrix_A)):
        matrix_A[i][-1] = matrix_A[i][-1][0]
        
    return matrix_A

def create_matrix_AT(matrix_A):
    """
        This function transposes the data of matrix_A in order to create a
        new matrix--matrix_AT.
        
    Parameters:
        matrix_A - the data of each revolutionary person saved as a list
        
    Returns:
        matrix_AT - the transposed data of matrix_A as a new matrix
    """
    
    matrix_AT = []
    for j in range(len(matrix_A[0])):
        AT_small_list = []
        for i in range(len(matrix_A)):
            AT_small_list.append(matrix_A[i][j])
        matrix_AT.append(AT_small_list)
        
    return matrix_AT

def multiply_matricies(matrix_AT, matrix_A):
    """
    This function multiplies matrix_A by matrix_AT in order to create a new matrix
    that tells us how much each individual interacted with others in the same
    circles.

    Parameters:
        matrix_A - the data of each revolutionary person saved as a list
        matrix_AT - the transposed data of matrix_A as a new matrix
        
    Returns:
        A_AT - the product of matrix_A and matrix_AT
    """
            
    A_AT = []
    
    num_people = len(matrix_A)
    
    for k in range(num_people):
        A_AT_small_list = []
        for i in range(num_people):
            sum_entries = 0
            for j in range(len(matrix_AT)):
                sum_entries += (int(matrix_A[i][j]) * int(matrix_AT[j][k]))
            A_AT_small_list.append(sum_entries)
            
        A_AT.append(A_AT_small_list)
    print(A_AT)
    return A_AT

def calculate_centrality(A_AT, name_list):
    """
    This function sums up the rows of A_AT in order to find which one has the
    largest sum. The row with the largest sum lets us know which individual is
    the most central figure. From this calculation, we then pull the name of
    the most central figure from name_list.

    Parameters:
        A_AT - the product of matrix_A and matrix_AT
        name_list - saves the names from "text" in alphabetical order

    Returns:
        most_central - the name of the most central figure
    """

    centrality_list = []
    
    for i in range(len(A_AT)):
        centrality_sum = 0 
        for j in range(len(A_AT[0])):
            centrality_sum += A_AT[i][j]
        centrality_list.append(centrality_sum)
            
    index = centrality_list.index(max(centrality_list))
    
    most_central = name_list[index]
    
    return most_central