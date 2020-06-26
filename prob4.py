
"""
Solution to the Deep Maximum problem from the CSC 121 Final Exam.

Author: Dominic Flocco 
"""


def deep_max(lst):
    """Returns the largest value that appears in the nested list lst

    This function computes the "deep maximum" of lst. If lst contains nested
    lists, then we also consider the elements inside those nested lists (and
    any nested lists inside those, etc.) when computing the maximum.

    Parameters:
        lst - the list whose maximal element we wish to compute

    Returns:
        The largest number that appears within lst or any nested substructure
        inside lst.
    """
    

    
    for i in range(len(lst)):
        if type(lst[i]) == type([]):
            lst = lst[i]
            return deep_max(lst)
    
    return max(lst)
    
            
    

def main():
    """ Tester function """
    print(deep_max([1, 2, 42, 3]))           # should print 42
    print(deep_max([1, 2, 3, [7, 42]]))      # should print 42
    print(deep_max([1, 2, [[3, [42]], 7]]))  # should print 42

    # feel free to add more test cases here!


if __name__ == "__main__":
    main()
