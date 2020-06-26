"""
Solutions to the programming problems from quiz #3.

Author: Dominic Flocco 
"""
import turtle


def print_multiplication_table():
    """
    Prints out the multiplication table for 13, up to 13 x 20.
    """
    for i in range(1,21):
        print("13 times", i, "=", i*13)
    


def steer_turtle():
    """
    Utilizes user-input directions to sketch a figure.
    """
    # The following lines prompt the user to enter a list of step sizes and
    # a list of angles to turn by, storing the results in variables named
    # steps and angles respectively. You should not modify these lines.
    steps = eval(input("Enter the step sizes to take (as a list): "))
    angles = eval(input("Enter the angles to turn by (as a list): "))
    
    
    for i in range(len(steps)):
        turtle.forward(steps[i])
        turtle.right(angles[i])
        

    turtle.done()


def shuffle():
    """
    Performs a perfect shuffle of a user-supplied list.
    """
    # Prompts the user to enter a list, storing the result in deck. You may
    # assume that the list will be of even length.
    deck = eval(input("Enter list: "))

    half_deck = len(deck) // 2
    
    first_half_deck = deck[:half_deck]
    second_half_deck = deck[half_deck:]
    
    shuffled_deck = []
    
    for i in range(len(first_half_deck)):
        shuffled_deck.append(first_half_deck[i])
        shuffled_deck.append(second_half_deck[i])
        
    print(shuffled_deck)
    