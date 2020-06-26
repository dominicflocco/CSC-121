
"""
Recursive implementations of some useful utility functions.

Author: Dominic and Betty
"""

def cube_sum(n):
    """ Returns the value of the sum 1^3 + 2^3 + ... + n^3.

    We assume n >= 1.

    Parameters:
        n - the last term in the summation.

    Returns:
        The value of 1^3 + 2^3 + ... + n^3 as an integer.
    """
    
    if n == 1:
        return 1
    
    return (n**3) + cube_sum(n-1)


def scrabble_score(word):
    """ Returns the Scrabble score of the given word.

    Parameters:
        word - the word to be scored (a string consisting of only lower-case
               letters).

    Returns:
        The value of word in Scrabble (as an integer).
    """
    TILE_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                   "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                   "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                   "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                   "y": 4, "z": 10}
    if word == "":
        return 0
    
    first = word[0]
    rest = word[1:]
    
    return TILE_SCORES[first] + scrabble_score(rest)
        


def is_palindrome(s):
    """ Returns True iff s is a palindrome.

    Parameters:
        s - the string to be checked.

    Returns:
        True iff s is a palindrome.
    """
    
    if s == "":
        return True
    
    first = s[0]
    last = s[-1]
    
    if first == last:
        if is_palindrome(s[1:-1:-1]) == is_palindrome(s[1:-1]):
            return True
    else:
        return False

    

def list_find(lst, val):
    """ Returns True iff val appears at least once in lst.

    Parameters:
        lst - a list of elements.
        val - the element we are searching for.

    Returns:
        True iff val appear somewhere in lst.
    """
    if lst == []:
        return False
    
    first = lst[0]
    to_return = list_find(lst[1:], val)
    
    if first == val:
        return True
    else:
        return to_return


def compute_gpa(grades):
    """Returns the GPA given a list of letter grades.

    Parameters:
        grades - a list of strings, where each string represents a valid
                 letter grade.

    Returns:
        The GPA corresponding to the given list of grades.
    """
    GRADES_TO_POINTS = {"A": 4.0, "A-": 3.7,
                        "B+": 3.3, "B": 3.0, "B-": 2.7,
                        "C+": 2.3, "C": 2.0, "C-": 1.7,
                        "D+": 1.3, "D": 1.0, "F": 0.0}
    if grades == []:
        return 0
    
    
    first = grades[0]
    rest = grades[1:]
    sum_of_the_rest = compute_gpa(grades[1:])
    
    return ((GRADES_TO_POINTS[first]) + (sum_of_the_rest) * (len(rest)))/len(grades) 
    
def main():
    """ Tester function """
    print()
    print("Testing cube_sum:")
    print(cube_sum(6)) # 441

    print()
    print("Testing scrabble_score")
    print(scrabble_score("art")) # 3
    print(scrabble_score("hello")) # 8
    print(scrabble_score("world")) # 9

    print()
    print("Testing is_palindrome:")
    print(is_palindrome("abba")) # True
    print(is_palindrome("aba")) # True
    print(is_palindrome("racecar")) # True
    print(is_palindrome("road")) # False

    print()
    print("Testing list_find")
    print(list_find(["a", "b", "c"], "a")) # True
    print(list_find(["a", "b", "c"], "x")) # False

    print()
    print("Testing compute_gpa")
    print(compute_gpa(["A", "B-", "C+", "B+", "A", "A"])) # 3.383
    print(compute_gpa(["A-", "B+", "B", "A", "A", "B+", "C-"])) # 3.286
    print(compute_gpa(["A"] * 32)) # :-)


if __name__ == "__main__":
    main()
