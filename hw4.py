 
"""
This program displays functions assigned in Homework 4.

Author: Dominic Flocco and Oguzhan Colkesen

Time Spent : 2 hrs
"""

from csc121 import image

def gradient_blend():
    """
    Produces a blended collage of rick.jpg and ilsa.jpg.
    """
    rick_red = image.get_channel('rick.jpg', 'red')
    rick_green = image.get_channel('rick.jpg', 'green')
    rick_blue = image.get_channel('rick.jpg', 'blue')
    
    ilsa_red = image.get_channel('ilsa.jpg', 'red')
    ilsa_green = image.get_channel('ilsa.jpg', 'green')
    ilsa_blue = image.get_channel('ilsa.jpg', 'blue')
    
    height = len(ilsa_red)
    width = len(ilsa_red[0])
    
    # We only modify the top left corner of Rick's image - this is the area
    # where we'll paste pixels from Ilsa over Rick. The rest of Rick remains
    # unchanged. This is why the loop below only ranges over the width and 
    # height of Ilsa, rather than Rick.
    for row in range(height):
        for col in range(width):
            distance_y_axis = col / width
            distance_x_axis = row / height
            coefficient = max(distance_y_axis, distance_x_axis)
            rick_red[row][col] = int((coefficient * rick_red[row][col]) +
                                     ((1 - coefficient) * ilsa_red[row][col]))
            rick_green[row][col] = int((coefficient * rick_green[row][col]) +
                                       ((1 - coefficient) * ilsa_green[row][col]))
            rick_blue[row][col] = int((coefficient * rick_blue[row][col]) +
                                      ((1 - coefficient) * ilsa_blue[row][col]))
            
    image.write_jpg(rick_red, rick_green, rick_blue, 'blended.jpg')
    
def mirror():
    """
    Produces a new image that mirrors the left side onto the right side.
    """
    file_name = input("Enter file name here: ")
    
    image_red = image.get_channel(file_name, 'red')
    image_green = image.get_channel(file_name, 'green')
    image_blue = image.get_channel(file_name, 'blue')
    
    width = len(image_red[0])
    height = len(image_red)
    
    index = width // 2 
    
    for i in range(height):
        for j in range(index):
            image_red[i][- (j+1)] = image_red[i][j]
            image_green[i][- (j+1)] = image_green[i][j]
            image_blue[i][- (j+1)] = image_blue[i][j] 
            
    image.write_jpg(image_red, image_green, image_blue, 'mirrored.jpg')
    
            
def pencil_sketch():
    """
    Produces a new image that appears to sketched by a pencil.
    """
    file_name = input("Enter file name here: ")
    
    image_red = image.get_channel(file_name, 'red')
    image_green = image.get_channel(file_name, 'green')
    image_blue = image.get_channel(file_name, 'blue')
    
    width = len(image_red[0])
    height = len(image_red)
    
    for row in range (height-1):
        for col in range (width-1):
            grayscale_original = (image_red[row][col] +
                                  image_green[row][col] + image_green[row][col]) // 3
            grayscale_right = (image_red[row][col+1] +
                               image_green[row][col+1] + image_green[row][col+1]) // 3
            grayscale_bottom = (image_red[row+1][col] +
                                image_green[row+1][col] + image_green[row+1][col]) // 3
            
            grayscale_difference_1 = abs(grayscale_right - grayscale_original)
            grayscale_difference_2 = abs(grayscale_bottom - grayscale_original)
            
            if grayscale_difference_1 > 8 and grayscale_difference_2 > 8:
                image_red[row][col] = 0
                image_green[row][col] = 0
                image_blue[row][col] = 0
            else:
                image_red[row][col] = 255
                image_green[row][col] = 255
                image_blue[row][col] = 255
           
           
    
    image.write_jpg(image_red, image_green, image_blue, 'sketched.jpg')

def tile_image():
    """
    Produces a scrambled image in the style of a 3 x 3 sliding tile
    """
    file_name = input("Enter file name here: ")
    
    image_red = image.get_channel(file_name, 'red')
    image_green = image.get_channel(file_name, 'green')
    image_blue = image.get_channel(file_name, 'blue')
    
    width = len(image_red[0])
    height = len(image_red)
    
    square_width = width // 3
    square_height = height // 3
    
    for row in range(height):
        for col in range(width):
            if row < square_height:
                if col < square_width:
                    image_red[2*square_height + row][2*square_width + col] = image_red[row][col]
                    image_green[2*square_height + row][2*square_width + col] = image_green[row][col]
                    image_blue[2*square_height + row][2*square_width + col] = image_blue[row][col]
                elif col >= square_width and col < 2 * square_width:
                    image_red[row][col - square_width] = image_red[row][col + square_width]
                    image_green[row][col - square_width] = image_green[row][col + square_width]
                    image_blue[row][col - square_width] = image_blue[row][col + square_width]
                elif col >= 2 * square_width:
                    image_red[row][col] = image_red[row + square_height][col - 2 * square_width]
                    image_green[row][col] = image_green[row + square_height][col - 2 * square_width]
                    image_blue[row][col] = image_blue[row + square_height][col - 2 * square_width]
                    
            elif row >= square_height and row < 2*square_height:
                if col < square_width:
                    image_red[row][col] = image_red[row][col + square_width]
                    image_green[row][col] = image_green[row][col + square_width]
                    image_blue[row][col] = image_blue[row][col + square_width]
                elif col >= square_width and col < 2 * square_width:
                    image_red[row][col] = image_red[row + square_height][col]
                    image_green[row][col] = image_green[row + square_height][col]
                    image_blue[row][col] = image_blue[row + square_height][col]
                    
                    
            elif row >= 2*square_height:
                if col < square_width:
                    image_red[row][square_width + col]= image_red[row][col]
                    image_green[row][square_width + col] = image_green[row][col]
                    image_blue[row][square_width + col] = image_blue[row][col]
                elif col >= 2 * square_width:
                    image_red[row][col - 2 * square_width] = 255
                    image_green[row][col - 2 * square_width] = 255
                    image_blue[row][col - 2 * square_width] = 255
    
    image.write_jpg(image_red, image_green, image_blue, 'tiled.jpg')    
    