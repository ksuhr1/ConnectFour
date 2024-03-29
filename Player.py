import numpy as np
from operator import itemgetter

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)


    """determines player and rival and passes alpha,beta,& depth
       to search_board """
    def get_alpha_beta_move(self, board):
        player = self.player_number
        if(player == 1):
            rival = 2
        else:
            rival = 1

        v = self.search_board(board, -10000000, +10000000, 4, player, rival)
        return v


    """
    this function iterates through all columns of the board 
    and saves a list of tupples (max value, min indes)
    which was returned from the min value function"""
    def search_board(self,board, alpha, beta, depth, player, rival):
        test = [];
        moves = self.validMoves(board)
        # print("valid moves: {}").format(moves)
        for row, col in moves:
            board[row][col] = player
            result = self.min_value(board, alpha, beta, depth-1, player, rival)
            alpha = max(alpha, result)
            board[row][col] = 0
            test.append((alpha, col))
            # print(test)

        #takes out max value with min index
        maxtest = (max(test, key = itemgetter(1))[0])
        for item in test:
            if maxtest in item:
                maxtest = item[1]
                break
        return(maxtest)

    """
    - returns the utility when at depth 0 or when not in a valid move
    - iterates through the valid moves dropping a player in that 
      position and recieves utility of that position
    - sets position in board back to 0 and returns updated or correct alpha"""
    def max_value(self,board,alpha, beta, depth, player, rival):
        valid_moves = self.validMoves(board)
        if(depth == 0 or not valid_moves):
            return self.evaluation_function(board)

        for row, col in valid_moves:
            board[row][col] = player
            result = self.min_value(board,alpha,beta,depth-1, player, rival)
            alpha = max(alpha, result)
            board[row][col] = 0
            if alpha >= beta:
                return alpha 
        return alpha

    """ 
    - similar to max_value but returns beta"""
    def min_value(self,board,alpha,beta,depth, player, rival):
        valid_moves = self.validMoves(board)
        if(depth == 0 or not valid_moves):
            return self.evaluation_function(board)
        for row,col in valid_moves:
            board[row][col] = rival       
            result = self.max_value(board, alpha, beta, depth-1, player, rival)
            beta = min(beta,result)
            board[row][col] = 0
            if beta<= alpha:
                return beta
        return beta

    """
    - calls expectimax passing the board, depth, and player"""
    def get_expectimax_move(self, board):
        player = self.player_number
        if(player == 1):
            rival = 2
        else:
            rival = 1
        v = self.expectimax(board, 4 , player, rival)
        return v

    """
    similar to search board function except gets utility
    of expected value from exp_value function"""
    def expectimax(self, board,depth, player, rival):
        test = [];
        moves = self.validMoves(board)
        v = -10000000
        # print("valid moves: {}").format(moves)
        for row, col in moves:
            board[row][col] = player
            result = self.exp_value(board, depth-1, player, rival)
            v = max(v, result)
            board[row][col] = 0
            test.append((v, col))
            #print(test)
        #take out max value with min index
        maxtest = (max(test, key = itemgetter(1))[0])
        for item in test:
            if maxtest in item:
                maxtest = item[1]
                break
        return(maxtest)

    """
        similar to max_value function except gets 
        utility from expected value function """
    def exp_max(self, board, depth, player, rival):
        valid_moves = self.validMoves(board)
        v = -10000000
        if(depth == 0 or not valid_moves):
            return self.evaluation_function(board)
        for row, col in valid_moves:
            board[row][col] = player
            result = self.exp_value(board, depth-1, player, rival)
            v = max(v, result)
            board[row][col] = 0
        return v

    """
        -gets the number of valid moves = num chances
        -returns expected value from recieving utility
         from exp_max function and dividing by num_chances"""
    def exp_value(self, board, depth, player, rival):
        valid_moves = self.validMoves(board)
        if(depth == 0 or not valid_moves):
            return self.evaluation_function(board)
        expectedVal = 0
        num_chances = len(valid_moves)
        print(num_chances)
        for row,col in valid_moves:
            board[row][col] = rival
            p = self.exp_max(board, depth-1, player, rival)
            expectedVal+= p
            v = expectedVal/num_chances
        return v 


    def evaluation_function(self, board):
        utility_num = 0
        if(self.player_number == 2):
            rival = 1
        else:
            rival = 2

        utility_num = self.count_values( board,4,self.player_number)*1000
        utility_num += self.count_values( board,3,self.player_number)*100
        utility_num += self.count_values( board,2,self.player_number)*10

        utility_num -= self.count_values( board, 4, rival)*900
        utility_num -= self.count_values( board,3, rival)*100
        utility_num -= self.count_values( board,2, rival)*10
        return (utility_num)

    def validMoves(self,board):
        moves = []
        for col in range(7):
            for row in range(5,-1,-1):
                if board[row][col] == 0:
                    moves.append([row,col])
                    break
        return moves

    """count_values checks the amount of #4's #3's #2's in a row
    for the entire board"""
    def count_values(self, board, num, player_num):
        player_win_str = 0
        player_win_str = '{0}'*num

        player_win_str = player_win_str.format(player_num)
        to_str = lambda a: ''.join(a.astype(str))

        def check_horizontal(b):
            value=0
            for row in b:
                if player_win_str in to_str(row):
                    value+=to_str(row).count(player_win_str)
            return value
        def check_verticle(b):
            return check_horizontal(b.T)
             
        def check_diagonal(b):
            value = 0
            for op in [None, np.fliplr]:
                op_board = op(b) if op else b
                 
                root_diag = np.diagonal(op_board, offset=0).astype(np.int)
                if player_win_str in to_str(root_diag):
                    value+=to_str(root_diag).count(player_win_str)
                for i in range(1, b.shape[1]-3):
                    for offset in [i, -i]:
                        diag = np.diagonal(op_board, offset=offset)
                        diag = to_str(diag.astype(np.int))
                        if player_win_str in diag:
                           value+=diag.count(player_win_str)
            return value

        totalval = check_horizontal(board) + check_verticle(board) + check_diagonal(board)
        return(totalval)

class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)



    def get_move(self, board):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))
        while move not in valid_cols:
            move = int(input('Enter your move: '))
            
        return move

