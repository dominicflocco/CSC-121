
"""
Solutions to the programming problems from quiz #11.

Author: Dominic Flocco 
"""
import turtle


def draw_ruler(height, width, level):
    """ Draws a fractal ruler of the desired height, width and level.

    Parameters:
        height - the height of the ruler (i.e., the height of the vertical ruler
                 "edge")
        width - the width of the ruler (i.e., the length of the middle tick).
        level - the recursive level of the ruler.

    Returns:
        None.
    """
    
    t = turtle
    if level == 0:
        return
    
    initial_pos = t.pos()
    t.forward(height / 2)
    draw_ruler(height / 2, width / 2, level - 1)
    t.left(90)
    t.forward(width)
    t.backward(width)
    t.right(90)
    t.forward(height / 2)
    t.goto(initial_pos)

    draw_ruler(height / 2, width / 2, level - 1)

def main():
    """ Tester function. """
    turtle.speed('fastest')
    draw_ruler(256, 128, 6)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
