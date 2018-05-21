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

    #alpha: current best score on the path to the root by maximizer (us)
    #beta: current best score on path to root by minimizer (opponent)
    def get_alpha_beta_move(self, board):
     #   v= self.max_value(board,-10000000, +10000000,1)
     #   return v
        player = self.player_number
        if(player == 1):
            rival = 2
        else:
            rival = 1
        v = self.search_board(board, -10000000, +10000000, 2, player, rival)
        return v

    def search_board(self,board, alpha, beta, depth, player, rival):
        print("Depth: {}").format(depth)
        values = [];
        v = -10000000
        moves = self.validMoves(board)
        print("valid moves: {}").format(moves)
        print("pre value array:{}").format(values)
        for row, col in moves:
            #makes move in col for current player
            board[row][col] = player
            print("Search Board: ")
            print(board)
            result = self.min_value(board, alpha, beta, depth-1, player, rival)
            print("result:{}").format(result)
            v = max(v, result)
            print("v: {}").format(v)
            print("After search board: ")
            print(board)
            board[row][col] = 0
            values.append(v)
            print("New Value array:{}").format(values)
        print("Player: {}").format(self.player_number)
        maxval = max(values)
        maxindex = values.index(maxval)
        print(values)
        print("Maxindex: {}").format(maxindex)
        return maxindex
      #  return [maxindex, maxval]

    def max_value(self,board,alpha, beta, depth, player, rival):
        valid_moves = self.validMoves(board)
    #    print("max_value valid moves: {}").format(valid_moves)
    #    print(self.evaluation_function(board))
        if(depth == 0 or not valid_moves):
            return self.evaluation_function(board)
        v = -10000000
        for row, col in valid_moves:
          #  print(self.player_number)
            board[row][col] = player
            print("Maxboard")
            print(board)
            result = self.min_value(board,alpha,beta,depth-1, player, rival)
            v = max(v, result)
            board[row][col] = 0
            if v >= beta:
                print("if v{} >= {}").format(v, alpha)
                return v
            alpha = max(alpha, v)
            print("alpha = max({},{})").format(alpha,v)
            print("Max alpha: {}, Max beta: {}, Max (v): {}").format(alpha,beta,v)
        return v
    def min_value(self,board,alpha,beta,depth, player, rival):
        valid_moves = self.validMoves(board)
        print("min_value valid moves: {}").format(valid_moves)
    #    print("Min valid moves:")
    #    print(valid_moves)
        print(self.evaluation_function(board))
        if(depth == 0 or not valid_moves):
            return self.evaluation_function(board)
        v = +10000000
        for row,col in valid_moves:
            board[row][col] = rival
            print("Minboard")
            print(board)
            result = self.max_value(board, alpha, beta, depth-1, player, rival)
            v = min (v, result)
            board[row][col] = 0
            if v<= alpha:
                print("if v{} <= {}").format(v, alpha)
                return v
            beta = min(beta,v)
            print("alpha = min({},{})").format(alpha,v)
            print("Min alpha: {}, Min beta: {}, Min (v): {}").format(alpha,beta,v)
        return v


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

    def evaluation_function(self, board):
        utility_num = 0
        if(self.player_number == 2):
            rival = 1
        else:
            rival = 2

        utility_num = self.count_values( board,4,self.player_number)*1000
        utility_num += self.count_values( board,3,self.player_number)*100
        utility_num += self.count_values( board,2,self.player_number)*10

#        utility_num -= self.count_values( board, 4, rival)*600
        utility_num -= self.count_values( board,3, rival)*100
        utility_num -= self.count_values( board,2, rival)*10
        return (utility_num)

    def validMoves(self,board):
        moves = []
        for col in range(7):
            for row in range(5,0,-1):
                if board[row][col] == 0:
                    moves.append([row,col])
                    break
        return moves

    #count_values checks the amount of #4's #3's #2's in a row
    #for the entire board
    def count_values(self, board, num, player_num):
        player_win_str = 0
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

#def alpha_beta_prune(self, board, depth):
#
#    def ab(self, board, alpha, beta, depth):
#        values = [];
#        v = -1000000
#        for row, col in validMoves(board):
#            board[row][col] = 1
#            v = max(v, min_value(self, board, alpha, beta, depth-1))
#            values.append(v)
#            board[row][col] = 0
#        maxVal = max(values)
#        deepindex = values.index(maxVal)
#        return [deepindex, maxVal]
#
#
#
#    def max_value(self, board, alpha, beta, depth):
#        valid_moves = validMoves(board)
#        if(depth == 0 or not valid_moves):
#            return evaluation_function(self, board)
#        v = -1000000
#        for row, col in valid_moves:
#            board[row][col] = 1
#            v = max(v, min_value(self, board, alpha, beta, depth-1))
#            board[row][col] = 0
#            if v >= beta:
#                return v
#            alpha = max(alpha,v)
#        return v
#
#    def min_value(self, board, alpha, beta, depth):
#        valid_moves = validMoves(board)
#        if(depth == 0 or not valid_moves):
#            return evaluation_function(self, board)
#        v = +1000000
#        for row, col in valid_moves:
#            board[row][col] = 2
#            v = min( v, max_value(self, board, alpha, beta, depth-1))
#            board[row][col] = 0
#
#            if v<= alpha:
#                return v
#            beta = min(beta,v)
#        return v
#    return ab(self, board, -100000, 100000, depth)
#
#def getMove(self,board):
#    depth = 3
#    value = alpha_beta_prune(self, board, depth)
#    return value[0]
   
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
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))
            
        return move

