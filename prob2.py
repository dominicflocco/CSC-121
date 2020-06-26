
"""
Solution to the Pikachu problem from the CSC 121 Final Exam.

Author: Dominic Flocco 
"""

def is_speakable(word):
    """Returns whether the given string is speakable by Pikachu.

    Pikachu can only speak words that can be formed by some concatentation of
    one or more copies of the syllables "pi", "ka", and "chu".

    Args:
        word - the string that Pikachu is trying to say.

    Returns:
        A boolean value that is True iff Pikachu can say the given string,
        and False otherwise.
    """
    word = word.strip("pi")
    word = word.strip("ka")
    word = word.strip("chu")
    
    if word == "":
        return True
    else:
        return False
        

    

def main():
    """ Tester function. """
    print(is_speakable("pikapi"))    # True
    print(is_speakable("pikachu"))   # True
    print(is_speakable("pipikachu")) # True
    print(is_speakable("pikaqiu"))   # False

    # feel free to add more test cases here!


if __name__ == "__main__":
    main()
