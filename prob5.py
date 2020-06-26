
"""
Solution to the Rectangle Type problem from the CSC 121 Final Exam.

Author: Dominic Flocco 
"""

class Rectangle:
    
    def __init__(self, x, y, w, h):
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        
    def __str__(self):
        
        return (str(self.x) + " " + str(self.y)
                + " " + str(self.w) + " " + str(self.h))
    
    def area(self):
        area = self.w * self.h
        
        return area

    def contains(self, x_cord, y_cord):
        
        x_max = self.x + self.w
        x_min = self.x 
        y_max = self.y
        y_min = self.y - self.h
        
        if (x_cord <= x_max and x_cord >= x_min
            and y_cord <= y_max and y_cord >= y_min):
            return True
        else:
            return False
        
    def intersection(self, rectangle):
        
        new_r = rectangle
        old_r = self
        
        
    
        if abs(old_r.x + old_r.w) >= abs(new_r.x + new_r.w) and abs(old_r.y - old_r.h) <= abs(new_r.y):
            # top right corner of new_r in center of old_r
            width = abs((new_r.x + new_r.w) - old_r.x)
            height = abs(new_r.y - (old_r.y - old_r.h))
            x_cord = old_r.x
            y_cord = new_r.y
        
        elif abs(old_r.x + old_r.w) <= abs(new_r.x + new_r.w) and abs((old_r.y - old_r.h)) >= abs((new_r.y)):
            # top left corner of new_r in center of old_r
            width = abs((old_r.x + old_r.w) - new_r.x)
            height = abs(new_r.y - (old_r.y - old_r.h))
            x_cord = new_r.x
            y_cord = new_r.y
            
        elif abs(old_r.x + old_r.w) <= abs(new_r.x + new_r.w) and abs(old_r.y) >= abs(new_r.y - new_r.h):
            # bottom left corner of new_r in center of old_r
            width = abs((old_r.x + old_r.w) - new_r.x)
            height = abs((new_r.y - new_r.h) - old_r.y)
            x_cord = new_r.x
            y_cord = old_r.y
            
        elif abs(old_r.x + old_r.w) >= abs(new_r.x + new_r.w) and abs(old_r.y) <= abs(new_r.y - new_r.h):
            # bottom right corner of new_r in center or old_r  
            width = abs((new_r.x + new_r.w) - old_r.w)
            height = abs(old_r.y - (new_r.y - new_r.h))
            x_cord = old_r.x
            y_cord = old_r.y
        else:
            width = 0
            height = 0
            x_cord = 0
            y_cord = 0
        return Rectangle(x_cord, y_cord, width, height)
        
        
        
def main():
    """ Tester function. """
    rectangle1 = Rectangle(3, 2, 7, 5)
    print(rectangle1)                            # 1 7 4 7

    print(rectangle1.area())                     # 28
    print(rectangle1.contains(2, 6))             # True
    print(rectangle1.contains(1, 4))             # True
    print(rectangle1.contains(2, 9))             # False

    rectangle2 = Rectangle(6, -1, 5, 4)
    intersect = rectangle1.intersection(rectangle2)
    print(intersect)                             # 1 4 2 4
    print(intersect.area())                      # 8
    intersect = rectangle2.intersection(rectangle1)
    print(intersect)                             # 1 4 2 4

    # feel free to add more test cases here


if __name__ == "__main__":
    main()
