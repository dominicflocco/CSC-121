
"""
Solutions to the programming problems from quiz #6.

Author: Dominic Flocco
"""


def simon_says(instructions):
    """
    Returns the instructions that would be obeyed in a game of Simon Says.

    Parameters:
        instructions - a list of strings, where each element is an instruction
                       issued by Simon.

    Returns:
        A list of strings, containing the instructions that were obeyed.
    """

    obeyed = []
    
    
    for phrase in instructions:
        if "Simon says" == phrase[:10]:
            obeyed.append(phrase[11:])
        
    return obeyed
            
            


def min_tiles_to_change(room):
    """
    Returns the minimal number of tiles that need to be changed to make the
    given room as colorful as possible.

    The goal is to achieve a tile configuration where no two adjacent tiles are
    the same color.

    Parameters:
        room - a string containing the colors of the tiles in the room. The i^th
               character of room (one of 'R', 'G', 'B', or 'Y') is the color of
               the i^th tile.

    Returns:
        The minimum number of tiles that need to be changed so that no two
        neighboring tiles are the same color.
    """


    tiles = 0
    
    tile_list = []
    
    for char in room:
        tile_list.append(char)
        
    len_list = len(tile_list)
    
    middle = 1
    
    for color in tile_list:
        if middle <= len(tile_list):
            if len(tile_list) % 2 != 0:
                if middle < (len(tile_list) - 1):
                    if tile_list[middle] == tile_list[middle + 1] or tile_list[middle] == tile_list[middle - 1]:
                        middle += 2
                        tiles += 1
                    else:
                        middle += 1

            else:
                 if middle < (len(tile_list) - 1):
                    if tile_list[middle] == tile_list[middle + 1] or tile_list[middle] == tile_list[middle - 1]:
                        middle += 2
                        tiles += 1
                        
                 if middle == (len(tile_list) - 1):
                    if tile_list[middle] == tile_list[middle -1]:
                        middle += 1
                        tiles += 1
                    else:
                        middle += 1
            
    return tiles


def main():
    """ Tester function. """
    # Test cases for Simon Says
    print("\nTesting Simon Says")
    obeyed = simon_says(["Simon says smile", "Clap your hands",
                         "Simon says jump", "Nod your head"])
    print("Test case 1:", obeyed)

    obeyed = simon_says(["simon says wave", "Simon say jump",
                         "Simon says twist and shout"])
    print("Test case 2:", obeyed)

    obeyed = simon_says(["simon says wave", "simon says jump",
                         "simon says clap"])
    print("Test case 3:", obeyed)

    obeyed = simon_says(["Jump", "Simon says wave"])
    print("Test case 4:", obeyed)
    print()

    # feel free to add more test cases for Simon Says here

    # Test cases for Colorful Tiles
    print("Testing Colorful Tiles")
    tiles = min_tiles_to_change("RRRRRR")
    print("Test case 1:", tiles)

    tiles = min_tiles_to_change("BBBYYYYYY")
    print("Test case 2:", tiles)

    tiles = min_tiles_to_change("BRYGYBGRYR")
    print("Test case 3:", tiles)
    tiles = min_tiles_to_change("RBBBYYYR")
    print("Test case 1:", tiles)
    
    
    print()

    # feel free to add more test cases for Colorful Tiles here


if __name__ == "__main__":
    main()
