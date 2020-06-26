
"""
Solution to the Zookeeper problem from the CSC 121 Final Exam.

Author: Dominic Flocco
"""

def tabulate_animals(filename):
    """Returns the census result from analyzing the data in the given file.

    Animals are grouped by their species (while ignoring capitalization),
    with distinctions between subspecies ignored. For example, Siberian
    Tiger, South China Tiger and Tiger are all counted as "tiger".

    Parameters:
        filename - the name of a text file, where each line represents
                   one individual animal in Dinah's zoo

    Returns:
        A list of strings in the format 'animal count', sorted
        alphabetically. If the given file cannot be read, then the empty
        list is returned.
    """
    text_list = []
   
    with open(filename, "r") as input_file:
        text = input_file.readlines()
        for i in range(len(text)):
            words = text[i].split()
            text_list.append(words)
            
    animal_list = []
    
    for i in range(len(text_list)):
        animal_list.append(text_list[i][-1])
    
    for i in range(len(animal_list)):
        animal_list[i] = animal_list[i].lower()

    animal_list.sort()

    count_animals = []
    single_animal_list = []
    for name in animal_list:
        animal = ""
        animal = name
        if animal not in single_animal_list:
            single_animal_list.append(name)
            
    for name in single_animal_list:
        animal_count = animal_list.count(name)
        count_animals.append(name + " " + str(animal_count))
    
    return count_animals


def main():
    """ Tester function """
    # The following should print ['bear 2', 'elephant 2', 'tiger 4']
    print(tabulate_animals('animals-1.txt'))

    # The following should print ['bird-of-paradise 12']
    print(tabulate_animals('animals-2.txt'))

    # feel free to add more test cases here!


if __name__ == "__main__":
    main()
