"""
Names: Dominic Flocco and Cynthia Fan

Time Spent: 3 hours

The following cracks an encryption in a given file and returns
deciphered text as a string.

"""


def crack_cipher(file_name):
    """
    This function returns the deciphered text as a string
    
    Parameters:
        file_name - represents the file being read
        
    Return:
        deciphered text as a string
    """
    
    
    
    return shifts(file_name)
    
    
    
def shifts(file_name):
    """
    This function creates a list and produces shifted versions of that list.
    
    The funtion first opens the file, reads it and creates a list of the
    characters in the text file. Afterwards, it produces 26 variations of
    this list shifted by proceeding integers from 0 to 26.
    
    Parameters:
        file_name - represents the file being read
        
    Return:
        produces and returns three variables. The fist is the text (file_name),
        the second is the list containing 26 shifts and the third containing the
        list of characters in the text.
    """
    
    characters = []
    
    with open(file_name, "r") as input_file:
        words = input_file.readlines()
    for word in words:
        for letters in word:
            characters.append(letters)
        
    letter_list = characters
    
    
    shift_list = []
    
    for j in range(0,25):
        single_shift = []
        for i in range(len(letter_list)):
            num_letter = ord(letter_list[i])
            if num_letter >= 97 and num_letter <= 122:
                num_letter += j
                if num_letter > 122:
                    single_shift.append(chr(97 + (num_letter- 123)))
                else:     
                    single_shift.append(chr(num_letter))
            else:
                single_shift.append(letter_list[i])
        shift_list.append(single_shift)
        
    return scoring(file_name, shift_list, letter_list)

    
def scoring(file_name, shift_list, letter_list):
    """
    This function calculates the englishness of each shift and assigns a score
    indicating the desired shift amount.
    
    The frequency of each letter is calculated by counting the amount of times
    a letter appears in the list and dividing if by the number of characters in
    the list. Once the frequency is calculated the difference between the frequency
    of this letter in english and the calculated frequency in the desired text. Then,
    the list of differences for each shift is summed up and the smallest difference
    is recorded and the shift that caused the smallest variation is recorded as score.
    
    Parameters:
        file_name - text being decoded
        shift_list - list of shifted values
        letter_list - list of letters in text
        
    Return:
        the decyphered text is returned as a string
        
    """
    
    score_list = []
    for i in range(len(shift_list)):
        single_score_list = []
        for j in range(0,25):
            single_score_list.append(shift_list[i].count(chr(97+j)))
        score_list.append(single_score_list)
        
    
    frequency = []
    for i in range(len(score_list)):
        single_frequency = []
        for j in range(0,25):
            single_frequency.append(100 *((score_list[i][j]) / len(letter_list)))
        frequency.append(single_frequency)
         
         
    ENGLISH_FREQ = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97,
0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.09, 5.99,
6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.06]
    

    difference_list = []
    
    for i in range(len(frequency)):
        shift_difference_list = []
        for j in range(len(frequency[0])):
            shift_difference_list.append(abs(frequency[i][j] - ENGLISH_FREQ[j]))
        difference_list.append(shift_difference_list)
   
    sum_list = []
    for i in range(len(difference_list)):
        sum_list.append(sum(difference_list[i]))
    
    minimum_sum = min(sum_list)
    score = sum_list.index(minimum_sum)
    
    deciphered_text = ''.join(shift_list[score])
    
    return deciphered_text
    
  

    
