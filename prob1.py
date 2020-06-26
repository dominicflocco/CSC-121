
"""
Solution to the Rabbit Numbers problem from the CSC 121 Final Exam.

Author: Dominic Flocco 
"""

def count_rabbits(low, high):
    """ Returns the number of rabbit numbers in the range [low, high].

    A number n is considered a rabbit number if S(n) * S(n) == S(n*n).

    Parameters:
        low: the lower-bound of the range that we are searching for rabbit
             numbers
        high: the upper-bound of the range that we searching

    Returns:
        An integer denoting the number of rabbit numbers n found such that
        low <= n <= high.
    """
    rabit_numbers = 0
    
    num_list = []
    for i in range(low, high + 1):
        num_list.append(str(i))
        
    squared_list = []
    for i in range(low, high + 1):
        squared_list.append(str(i ** 2))
    
    
    for i in range(len(num_list)):
        first_term = 0
        second_term = 0
        for val in range(len(num_list[i])):
            first_term += int(num_list[i][val-1])
        for val in range(len(squared_list[i])):
            second_term += int(squared_list[i][val-1])
        right_side = second_term # S(r ^ 2)
        left_side = first_term ** 2 # S(r) * S(r)

        if left_side == right_side:
            rabit_numbers += 1
            
    return rabit_numbers    
           
        

def main():
    """ Tester function """
    print(count_rabbits(311, 311))   # prints 1
    print(count_rabbits(484, 484))   # prints 0
    print(count_rabbits(1, 10))      # prints 4
    print(count_rabbits(1, 100000))  # prints 253


if __name__ == "__main__":
    main()
