
"""
Solutions to the programming problems from quiz #8.

Author: Dominic
"""


def scrabble_score_file(filename):
    """Returns the average Scrabble score of the words in a given file

    This function opens the supplied file and computes the average
    Scrabble score of every word in the file. A "word" is defined to
    be a non-empty sequence of characters that contains no spaces.
    When scoring words, only lower-case letters of the alphabet are
    scored; all other characters receive a score of 0. If the given
    file does not exist or cannot be opened, then a value of -1.0 is
    returned.

    Args:
        filename - a string containing the name of the file to be scored

    Returns:
        The average Scrabble score of all the words in the file
    """
    TILE_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                   "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                   "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                   "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                   "y": 4, "z": 10}
    try:
        with open(filename, "r") as input_file:
            text = input_file.read()
        words = text.split()
    except FileNotFoundError:
        return -1.0
    
    total_score = 0 
    for i in range(len(words)):
        word_score = 0
        for j in range(len(words[i])):
            if words[i][j] not in TILE_SCORES:
                word_score += 0
            else:
                word_score += TILE_SCORES[words[i][j]]
        total_score += word_score
        
    return total_score / len(words)

def compute_mode(scores):
    """ Returns the mode(s) of the supplied data.

    In case the mode is not unique, then the list of modes returned is in
    ascending order.

    Parameters:
        scores - a list of integers denoting the data whose mode we wish to
                 compute.

    Returns:
        A list of integers denoting the mode(s) of the data (sorted in
        ascending order).
    """
    scores_dict = {}
    
    for id in scores:
        if id in scores_dict:
            scores_dict[id] += 1
        else:
            scores_dict[id] = 1
    
    mode_list = []

    mode1 = max(scores_dict)
    max_appearence = scores_dict.get(mode1)
    
    appearance_list = []
    
    for i in scores_dict:
        appearance_list.append(scores_dict[i])
    
    max_appearence = max(appearance_list)
    for i in scores_dict:
        if scores_dict[i] not in mode_list:
            if scores_dict[i] == max_appearence:
                mode_list.append(i)
    
    mode_list.sort()
    
    return mode_list


def main():
    """ Tester function """
    # Testing scrabble_score_file
    print()
    print("Testing scrabble_score_file")
    print(scrabble_score_file("hello.txt")) # should print 4.0
    print(scrabble_score_file("one-word.txt")) # should print 5.0
    print(scrabble_score_file("non-existent-file")) # should print -1.0
    print(scrabble_score_file("moby-dick.txt")) # should print 7.4415...

    # Testing compute_mode
    print()
    print("Testing compute_mode")
    print(compute_mode([65, 70, 88, 70]))
    print(compute_mode([88, 70, 65, 70, 88]))
    print(compute_mode([92, 56, 14, 73, 22, 38, 93, 45, 55]))
    # Feel free to add more test cases here


if __name__ == "__main__":
    main()
