
"""
Solutions to the programming problems from quiz #1.

Author: Dominic Flocco 
"""

def lorentz_factor():
    """
    Determines the Lorentz factor for an object given its speed as a fraction
    of the speed of light.
    """
    # The following line prompts the user to enter a value for the velocity of
    # the moving object, and stores the input as a float in the variable
    # named speed. You do not have to understand how it works (for now)
    # and you should not modify this line. Just use the variable speed in
    # your solution below.
    speed = float(input("Enter object velocity (as a fraction of c): "))
    lorentz_factor_ = (1 / ((1 - ((speed) ** 2))** 0.5))
    print("Lorentz factor: ", lorentz_factor_)
    
       
def fight_song():
    """
    Prints out the lyrics to an admittedly uninspiring Wildcats fight song.
    """
    chorus()
    print("")
    chorus()
    verse()
    chorus()
    print("")
    chorus()
    verse()
    chorus()
    print("")
    chorus()
def chorus():
    print("Go, team go!")
    print("We can do it.")
    
def verse():
    print("We're the 'cats,")
    print("We'll leave it at that.")
    

