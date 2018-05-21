import numpy as np

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)


    #def minimax(self,board, depth):
     #   if depth == 0:
      #      return(self.evaluation_function(board))
       # alpha = np.inf


    def get_alpha_beta_move(self, board):
                

      # print(self.validMoves(board))
        
        
       get_utility = self.evaluation_function(board)
       max_val = max(get_utility)
       print(max_val)
       max_index = get_utility.index(max_val)
       print(max_index)
        #return maximum utility value
#        maximum_val = max(get_utility)
#        maximum_index = get_utility.index(maximum_val)
#        print("maximum_index: {}").format(maximum_index)
#        newBoard = board
#        for col in range (7):
#            for row in range(5,0,-1):
#                if newBoard[row][col]==0:
#                    newBoard[row][col] = maximum_index
#        print("newBoard")
#        print(newBoard)
#        get_minutility = self.evaluation_function(newBoard)
#        minimum_val = min(get_minutility)
#        minimum_index = get_minutility.index(minimum_val)
#        print("minimum_index:{}").format(minimum_index)
        
        return (max_index)
        
   # def minimax(board, depth):
    #    if depth == 0:
     #       print (self.evaluation_function(board))
      #  alpha = np.inf
       # print(alpha)
       # return(maximum_index)
        #alpha = np.inf
        #beta = -np.inf

        
        #v = max_value(self,alpha,beta)
        #return v
        #count_value(self,board,2,self.player_number)

   # def count_value(self, board, value,player_number):
    #    print value
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

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
    """Utility function defines the numeric value for a game that ends
        in terminal state s for a player p
        - Evaluation functions allow us to approzimate the true utility of a 
          state without doing a complete search"""        
        
#    def max_value(state,alpha,beta):
 #       v = -np.inf
  #      for child in state:
   #         v = max(v, value(child,alpha,beta))
    #        if v >= beta:
     #           return v
      #      alpha = max(alpha,v)
      #  return v


   # def min_value(state,alpha,beta):
    #    v = np.inf
     #   for child in state:
      #      v = min(v, value(child, alpha,beta))
       #     if v <= alpha:
        #        return v
         #   beta = min(beta,v)
       # return v

    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

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
        raise NotImplementedError('Whoops I don\'t know what to do')


    #count_values checks the amount of #4's #3's #2's in a row
    #for the entire board
    def count_values(self, board, num, player_num):
        player_win_str = '{0}'*num

        player_win_str = player_win_str.format(player_num)
        to_str = lambda a: ''.join(a.astype(str))
    
	def check_horizontal(b):
            value=0
            for row in b:
#                print(to_str(row))
                if player_win_str in to_str(row):
                    value+=to_str(row).count(player_win_str)
                  #  print("You won")
                  #  print("Number of two in a row: {} ").format(value)
                  #print(to_str(row))
            return value
           # print("Number of twins in a row: {} ").format(value)
            

        def check_verticle(b):
            return check_horizontal(b.T)
             
        def check_diagonal(b):
            value = 0
            for op in [None, np.fliplr]:
                op_board = op(b) if op else b
       	         
                root_diag = np.diagonal(op_board, offset=0).astype(np.int)
#                print("root_diag: {}").format(to_str(root_diag))
                if player_win_str in to_str(root_diag):
                    value+=to_str(root_diag).count(player_win_str)
             #   print("Diagnol-1 values: {}").format(value)
             
                for i in range(1, b.shape[1]-3):
                    for offset in [i, -i]:
                        diag = np.diagonal(op_board, offset=offset)
                        diag = to_str(diag.astype(np.int))
#                        print("diag: {} ").format(diag)
                        if player_win_str in diag:
                           value+=diag.count(player_win_str)
                        
            return value

        totalval = check_horizontal(board) + check_verticle(board) + check_diagonal(board)
        return(totalval)
#        print("Total count value: {}").format(totalval)
       # print("Horizontal frequency: {}").format(check_horizontal(board))
       # print("Vertical frequency: {}").format(check_verticle(board))
       # print("Diagnol frequency: {}").format(check_diagonal(board))
     #   checkh += check_verticle(board)
      #  checkh += check_diagonal(board)

      #  print(checkh)
       # if (check_horizontal(board) or 
        #        check_verticle(board) or
         #       check_diagonal(board)): 
          #          print("it won")
    
    def validMoves(self, board):
        boardCopy = board
        moves = []
        for col in range(7):
            for row in range(5,0,-1):
                if boardCopy[row][col] == 0:
                    moves.append([row,col])
                    break
        return moves

    def evaluation_function(self, board):

        """
        Given the current state of the board, return the scalar value that 
        represents the evaluation function for the current player
       
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
        The utility value for the current board

        """
        boardCopy = board  
        utility_list = []
        if(self.player_number == 2):
            rival = 1
        else:
            rival = 2


      #  valid = self.validMoves(board)
      #  print(valid)
      #  for row, col in valid:
      #      boardCopy[row][col] = self.player_number
      #      print(boardCopy)
            # self_count_values checks amount of values in a row for 
            #the entire board
            utility_num = self.count_values(board,4,self.player_number)*1000
            utility_num += self.count_values(board,3,self.player_number)*100
            utility_num += self.count_values(board,2,self.player_number)*10

            utility_num -=self.count_values(board,3, rival)*100
            utility_num -=self.count_values(board,2, rival)*10
            utility_list.append(utility_num)
            #replaces value you checked back to a 0
     #       boardCopy[row][col] = 0
     #       break
        return(utility_list)




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
       # print (self.validMoves( board))
        move = int(input('Enter your move: '))
        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))
            
        return move

    def validMoves(self, board):
        boardCopy = board
        moves = []
      #  if(self.player_number == 2):
        #    rival = 1
       # else:
        #    rival = 2
        for col in range(7):
            for row in range(5,0,-1):
                if boardCopy[row][col] == 0:
                    moves.append([row,col])
                    break
        return moves

