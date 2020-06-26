
"""
Solutions to the programming problems from quiz #10.

Author: Dominic Flocco
"""
import math


def radical_sum(num, level):
    """ Returns the value of the radical sum of num, nested to the given level.

    We assume that num >= 0 and level >= 0.

    Parameters:
        num - the integer whose radical sum we wish to compute.
        level - the number of levels of nesting in the radical sum.

    Returns:
        The value of sqrt(num + sqrt(num + sqrt(num + ...))), nested level
        times.
    """
    if level == 0:
        return 0
    
    return ((radical_sum(num, level - 1) + num) ** 0.5)


def simplify(phrase):
    """Returns a straightforward version of the input phrase.

    For example, 'the cat the dog worried' --> 'the dog that worried the cat'

    Parameters:
        phrase - a string containing a nested phrase.

    Returns:
        A string containing a more straightforward rewrite of the given
        phrase.
    """
    
    num_actors = 0
    
    if phrase == "":
        return 0
    
    phrase_list = phrase.split()

    for word in phrase_list:
        if word == "the":
            num_actors += 1
           
    index = (2 * num_actors) - 1
    actor = phrase_list[index]
    verb = phrase_list[index + 1]
        
    del phrase_list[index]
    del phrase_list[index - 1]
    del phrase_list[index + 1]
        
    phrase_string = ""
    for word in phrase_list:
        phrase_string += word
        phrase_string += " "
    
        
    return "the" + actor + "that" + verb + simplify(phase_string)
    
    

def main():
    """ Tester function. """
    print()
    print("Testing radical_sum")
    print(radical_sum(2, 2))   # 1.8477...
    print(radical_sum(2, 0))   # 0.0
    print(radical_sum(4, 5))   # 2.5607...
    print(radical_sum(2, 20))  # 2.0

    print()
    print("Testing simplify")
    print(simplify("the roach the pirate killed"))
    print(simplify("the rat the cat the dog worried killed"))
    print(simplify("the dog"))
    print(simplify("the rat the cat the dog the boy the girl saw owned " +
                   "chased bit"))
    print()


if __name__ == "__main__":
    main()
