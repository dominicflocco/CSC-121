
"""
Solution to the Backspace problem from the CSC 121 Final Exam.

Author: Dominic Flocco 
"""

def expand_backspaces(text):
    """Returns the string produced by expanding backspaces in text.

    A backspace in the given text is indicated by the < character. To expand
    a backspace, we delete both the < character, as well as the first
    non-backspace character that precedes it (if it exists), from our string.

    Parameters:
        text - a string containing backspaces to be expanded

    Returns:
        A new version of text where all backspace occurrences have been
        expanded.
    """
    occurences = text.count("<") * 2
    if occurences >= len(text):
        return ""
                
    text_list = []
    for char in text:
        text_list.append(char)
    
    while "<" in text_list:
        index = text_list.index("<")
        text_list.remove(text_list[index - 1])
        text_list.remove("<")
        
    return "".join(text_list)
  
def main():
    """ Tester function """
    print(expand_backspaces('a<bc<'))                   # b
    print(expand_backspaces('davidon<<z<sompq<<<m<n'))  # davidson
    print(expand_backspaces('ab<<<'))                   # empty string

    # feel free to add more test cases here!


if __name__ == "__main__":
    main()
