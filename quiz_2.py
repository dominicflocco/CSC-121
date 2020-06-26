"""
Solutions to the programming problems from quiz #2.

Author: Dominic Flocco 
"""

import math

def verify_ramanujan_theorem():
    """
    Verifies the validity of one of Ramanujan's theorems involving radicals.
    """
    left_side = ((math.sqrt(math.sqrt(5)) + 1))/((math.sqrt(math.sqrt(5)) - 1))
    right_side = 0.5 * (3.0 + math.sqrt(math.sqrt(5)) + (math.sqrt(5)) + (math.sqrt(math.sqrt(125))))
    
    print("The value of the left-hand side of Ramanujan's theorem:")
    print(left_side)
    print("The value of the right-hand side of Ramanujan's theorem:")
    print(right_side)

def print_surfin_bird():
    """
    Prints out the lyrics to the song Surfin' Bird by The Trashmen.
    """
    A_well_a = "A-well-a, bird, bird, bird, b-bird's the word"
    papa = "Papa-ooma-mow-mow, papa-ooma-mow-mow"
    ooma = "Ooma-mow-mow, papa-ooma-mow-mow"
    lyrics = [A_well_a, papa, ooma]
    
    
    print("A-well-a, everybody's heard about the bird")
    for verse in [1, 2, 3, 4, 5, 6, 7, 8]:
        print(lyrics[0])
    print("Surfin' bird")
    for verse in [1, 2, 3, 4, 5, 6]:
        print(lyrics[1])
        print(lyrics[2])
        

def compute_laundry_time():
    """
    Computes and prints out the minimum number of minutes required to
    do a user-specified number of loads of laundry.

    Assumptions: There is only 1 washer and 1 dryer. Washing takes 25 minutes,
    drying takes 25 minutes, and folding takes 10 minutes.
    """
    # The following line prompts the user to enter a value for the number of
    # loads that need laundering, and stores the input as an integer in the
    # variable named num_loads. You should not modify this line. Just use the
    # variable num_loads in your solution below.
    num_loads = int(input("Enter the number of loads: "))
    
    total_time = 60 + (((num_loads) - 1)*25)
    print(total_time)
