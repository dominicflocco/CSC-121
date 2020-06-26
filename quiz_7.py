
"""
Solutions to the programming problems from quiz #7.

Author: Dominic Flocco 
"""


def count_cheeseburgers(filename):
    """Returns the number of lines in the file that start with the word
    cheeseburger.

    Parameters:
        filename - the name of the file to be read (a string)

    Returns:
        The number of lines in the specified file that begin with the word
        cheeseburger.
    """

    words = []
    with open(filename, "r") as input_file:
        for line in input_file:
            fields = line.split()
            words.append(fields) 
        
        
    cheeseburger_count = 0
    
    for i in range(len(words)):
        if words[i][0] == "cheeseburger":
            cheeseburger_count += 1
    
    return cheeseburger_count   


def min_cost_palindrome(string_to_change, o_cost, x_cost):
    """Returns the minimum cost of transforming str into a palindrome

    This function accepts a string consisting of only xs, os and ?s and
    reports the minimum cost of transforming this string into a palindrome
    by replacing every occurrence of a ? with either an x or an o. If the
    input string cannot be transformed into a palindrome, then a value of
    -1 is returned.

    Args:
        string_to_change - string whose transformation cost we're computing
        o_cost - the cost of replacing a ? with an o (an int)
        x_cost - the code of replacing a ? with an x (an int)

    Returns:
        The minimum cost of transforming the input string into a palindrome
        given o_cost and x_cost. If it is not possible to transform s into
        a palindrome, then a value of -1 is returned.
    """
    
    if "?" not in string_to_change:  
        if string_to_change[::-1] == string_to_change:
            return 0
        else:
            return -1

    index_list = []
    
    occurence = string_to_change.count("?")
    index = -1
    for char in range(occurence):
        index = string_to_change.find("?", index + 1)
        index_list.append(index)
    cost = 0
    
    if o_cost < x_cost:
        new_string = string_to_change.replace("?", "o")
        if new_string == new_string[::-1]:
            cost += occurence * o_cost
        new_string = string_to_change.replace("?", "o", 1)
        new_string = new_string.replace("?", "x", 2)
        if new_string == new_string[::-1]:
            cost += (o_cost + x_cost)
        new_string = string_to_change.replace("?", "x", 1)
        new_string = new_string.replace("?", "o", 2)
        if new_string == new_string[::-1]:
            cost += (o_cost + x_cost)
        new_string = string_to_change.replace("?", "x")
        if new_string == new_string[::-1]:
            cost += occurence * x_cost
            
    if x_cost < o_cost:
        new_string = string_to_change.replace("?", "x")
        if new_string == new_string[::-1]:
            cost += occurence * x_cost
            new_string = string_to_change.replace("?", "x", 1)
            new_string = new_string.replace("?", "o", 2)
        elif new_string == new_string[::-1]:
            cost += (o_cost + x_cost)
            new_string = string_to_change.replace("?", "o", 1)
            new_string = new_string.replace("?", "x", 2)
        elif new_string == new_string[::-1]:
            cost += (o_cost + x_cost)
            new_string = string_to_change.replace("?", "o")
        elif new_string == new_string[::-1]:
            cost += occurence * o_cost   
    return cost
    
    
def main():
    
    """ Tester function """
    # Testing count_cheeseburgers
    # You might want to add more test cases to file1.txt
    print()
    print("Testing count_cheeseburgers")
    print(count_cheeseburgers('file1.txt'))  # should print 3
    # feel free to modify the given file1.txt to test other cases

    # Testing min_cost_palindrome
    print()
    print("Testing min_cost_palindrome")
    print(min_cost_palindrome("oxo?xox?", 3, 5))  # should print 8
    print(min_cost_palindrome("x??x", 9, 4))  # should print 8
    print(min_cost_palindrome("ooooxxxx", 12, 34))  # should print -1
    print(min_cost_palindrome("oxoxooxxxxooxoxo", 7, 4))  # should print 0
    # Feel free to add more test cases here


if __name__ == "__main__":
    main()
