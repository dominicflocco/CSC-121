"""
Implimentation of a Connect-4 Player Class

Authors: Elizabeth Opp and Dominic Flocco

Time Spent: 3 hours

"""
import random

class Player:
    
    def __init__(self, side, ply, is_random):
        """
        Function __init__() takes three parameters and uses these to build
        the Player class. The first parameter, self, defines which player, X or O,
        will be the player considered throughout the rest of the function.
        Parameter ply determines the number of plays to be made. Parameter
        is_random randomizes how ties should be won.
        """
        
        self.side = side
        self.ply = ply
        self.is_random = is_random
        
    def __str__(self):
        """
        This function, __str__(), returns a string stating the results from
        parameters given to function __init__(). As example, a string returned
        will read "Player for O, ply = 2, breaks ties randomly" if parameters
        given in __init__() are as follows: O, 2, True.
        """
        
        is_random_print = ""
        if self.is_random == True:
            is_random_print = "randomly"
        else:
            is_random_print = "deterministically"

        return "Player for " + self.side + ", ply = " + str(self.ply) + ", breaks ties " + is_random_print
        
    def opponent(self):
        """
        This function, opponent(), returns the opponent player. For example,
        if self is player X, this function will return player O as opponent.
        """
        
        if self.side == 'X':
            return 'O'
        else:
            return 'X'
        
    def evaluate_board(self, board):
        """
        This function evaluate_board() gets results from win_for() in connect4.py
        and returns a score to each player, X and O, after they make a move. A move
        that results in neither a win or loss then score 50 is returned, if a move
        results in a win that returns score 100, and if the opponent wins that
        returns a score of 0. This function is vital for score_columns() as it returns
        the scores that will populate the future scores_list.
        """
    
        win_score = 100
        win_or_loss_score = 50
        lose_score = 0
        
        if board.win_for(self.opponent()):
            return lose_score
        if board.win_for(self.side):
            return win_score
        if not board.win_for(self.side) or not board.win_for(self.opponent()):
            return win_or_loss_score
                
    def score_columns(self, board):
        """
        This function score_columns() takes in board and self as parameters and goes
        through each position in the board to determine the score of each position of
        self on the input board. This function determines each score by calling on
        previous function evaluate_board() to determine each position's score. This
        function returns the score_list, a list with the scores from each of self's
        positions on the board.
        """
        
        b = board

        score_list = []
        for col in range(b.width):
            score_list.append(50)
        
        eval_num = self.evaluate_board(b)
        full_score = -1
        
        for col in range(b.width):
            if eval_num == 100 or eval_num == 0 or b.is_full():
                score_list[col] = eval_num
            elif not b.allows_move(col):
                score_list[col] = full_score
            elif self.ply == 0:
                score_list[col] = 50
            else:
                b.add_move(col, self.side)
                #creates new player
                p_new = Player(self.opponent(), self.ply - 1, self.is_random)
                new_score = p_new.score_columns(b)
                score_list[col] = 100 - max(new_score)
                b.delete_move(col)
                
        return score_list    
                
        
    def best_move(self, scores):
        """
        This function best_move() takes two parameters, self, the player who is being
        considered, and scores, the score_list from score_columns(). Then, the largest
        value in the list is considered to determine which player is the winner. If
        scores are equal, random.choice(tie_list) is called to randomly determine
        the winner.
        """
    
        max_val = max(scores)
        
        tie_list = []
        for i in range(len(scores)):
            if scores[i] == max_val:
                tie_list.append(i)
        if self.is_random:
            return random.choice(tie_list)
        else:
            return tie_list[0]
        
            
    def next_move(self, board):
        """
        This function next_move() takes in parameters self, the player being
        considered, and board, the board from connect4.py, to determine where
        the next bext move is for the player in consideration. This next best
        move will be returned in the form of an integer.
        """
        
        return self.best_move(self.score_columns(board))
        
        
    