import numpy as np
import copy

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        print(self.player_number)
        self.player_string = 'Player {}:ai'.format(player_number)
        self.LIMIT = 6
        self.M = float('inf')
        self.d = dict()

    def evaluation_function(self, board):
            """
            Given the current stat of the board, return the scalar value that 
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
            # def utility(board,player_number):
            # return 1

            def diagonallr(board,player_number):
                cost = 0

                for i in range(7):
                    row1 = 0
                    col1 = i
                    while row1+2<=5 :
                        if (col1+2<=6) and (board[row1][col1]==board[row1+1][col1+1]==board[row1+2][col1+2]==player_number):
                            if((col1-1>=0 and row1-1>=0 and board[row1-1][col1-1]==0) and (col1+3<=6 and row1+3<=5 and board[row1+3][col1+3]==0)):
                                cost += 1*3
                            elif((col1-1>=0 and row1-1>=0 and board[row1-1][col1-1]==0) or (col1+3<=6 and row1+3<=5 and board[row1+3][col1+3]==0)):
                                cost += 1
                        row1 += 1
                        col1 += 1

                    row2 = 0
                    col2 = i
                    while row2+1<=5:
                        if (col2+1<=6) and (board[row2][col2]==board[row2+1][col2+1]==player_number):
                            if((col2-1>=0 and row2-1>=0 and board[row2-1][col2-1]==0) and (col2+2<=6 and row2+2<=5 and board[row2+2][col2+2]==0)):
                                cost += 0.01*3
                            elif((col2-1>=0 and row2-1>=0 and board[row2-1][col2-1]==0) or (col2+2<=6 and row2+2<=5 and board[row2+2][col2+2]==0)):
                                cost += 0.01
                        row2 += 1
                        col2 += 1

                    row3 = 0
                    col3 = i
                    while row3<=5:
                        if (col3<=6) and (board[row3][col3]==player_number):
                            if((col3-1>=0 and row3-1>=0 and board[row3-1][col3-1]==0) and (col3+1<=6 and row3+1<=5 and board[row3+1][col3+1]==0)):
                                cost += 0.0001*3
                            elif((col3-1>=0 and row3-1>=0 and board[row3-1][col3-1]==0) or (col3+1<=6 and row3+1<=5 and board[row3+1][col3+1]==0)):
                                cost += 0.0001
                        row3 += 1
                        col3 += 1

                    row4 = 0
                    col4 = i
                    while row4<=2:
                        if (col4+3<=6) and (board[row4][col4]==board[row4+1][col4+1]==board[row4+2][col4+2]==board[row4+3][col4+3]==player_number):
                                cost += 100

                        if (col4+3<=6) and ((board[row4][col4]==board[row4+2][col4+2]==board[row4+3][col4+3]==player_number and board[row4+1][col4+1]==0) or (board[row4][col4]==board[row4+1][col4+1]==board[row4+3][col4+3]==player_number and board[row4+2][col4+2]==0)):
                                cost += 50
                        row4 += 1
                        col4 += 1




                for i in range(1,6):
                    row1 = i
                    col1 = 0
                    while row1+2<=5:
                        if (col1+2<=6) and (board[row1][col1]==board[row1+1][col1+1]==board[row1+2][col1+2]==player_number):
                            if((col1-1>=0 and row1-1>=0 and board[row1-1][col1-1]==0) and (col1+3<=6 and row1+3<=5 and board[row1+3][col1+3]==0)):
                                cost += 1*3
                            elif((col1-1>=0 and row1-1>=0 and board[row1-1][col1-1]==0) or (col1+3<=6 and row1+3<=5 and board[row1+3][col1+3]==0)):
                                cost += 1
                            
                        row1 += 1
                        col1 += 1

                    row2 = i
                    col2 = 0
                    while row2+1<=5:
                        if  (col2+1<=6) and (board[row2][col2]==board[row2+1][col2+1]==player_number):
                            if((col2-1>=0 and row2-1>=0 and board[row2-1][col2-1]==0) and (col2+2<=6 and row2+2<=5 and board[row2+2][col2+2]==0)):
                                cost += 0.01*3
                            elif((col2-1>=0 and row2-1>=0 and board[row2-1][col2-1]==0) or (col2+2<=6 and row2+2<=5 and board[row2+2][col2+2]==0)):
                                cost += 0.01
                            
                        row2 += 1
                        col2 += 1

                    row3 = i
                    col3 = 0
                    while row3<=5:
                        if (col3<=6) and (board[row3][col3]==player_number):
                            if((col3-1>=0 and row3-1>=0 and board[row3-1][col3-1]==0) and (col3+1<=6 and row3+1<=5 and board[row3+1][col3+1]==0)):
                                cost += 0.0001*3
                            elif((col3-1>=0 and row3-1>=0 and board[row3-1][col3-1]==0) or (col3+1<=6 and row3+1<=5 and board[row3+1][col3+1]==0)):
                                cost += 0.0001
                        row3 += 1
                        col3 += 1

                    row4 = i
                    col4 = 0
                    while row4<=2:
                        if (col4+3<=6) and (board[row4][col4]==board[row4+1][col4+1]==board[row4+2][col4+2]==board[row4+3][col4+3]==player_number):
                                cost += 100

                        if (col4+3<=6) and ((board[row4][col4]==board[row4+2][col4+2]==board[row4+3][col4+3]==player_number and board[row4+1][col4+1]==0) or (board[row4][col4]==board[row4+1][col4+1]==board[row4+3][col4+3]==player_number and board[row4+2][col4+2]==0)):
                                cost += 50
                        row4 += 1
                        col4 += 1

                return cost

            def diagonalrl(board, player_number):
                cost = 0

                for i in range(7):
                    row1 = 0
                    col1 = i
                    while row1 + 2 <= 5:
                        if (col1 - 2 >= 0) and (board[row1][col1] == board[row1 + 1][col1 - 1] == board[row1 + 2][col1 - 2] == player_number):
                            if (col1 + 1 <= 6 and row1 - 1 >= 0 and board[row1 - 1][col1 + 1] == 0) and (col1 - 3 >= 0 and row1 + 3 <= 5 and board[row1 + 3][col1 - 3] == 0):
                                cost += 1*3
                            elif (col1 + 1 <= 6 and row1 - 1 >= 0 and board[row1 - 1][col1 + 1] == 0) or (col1 - 3 >= 0 and row1 + 3 <= 5 and board[row1 + 3][col1 - 3] == 0):
                                cost += 1
                            
                        row1 += 1
                        col1 -= 1

                    row2 = 0
                    col2 = i
                    while row2 + 1 <= 5:
                        if (col2 - 1 >= 0) and (board[row2][col2] == board[row2 + 1][col2 - 1] == player_number):
                            if (col2 + 1 <= 6 and row2 - 1 >= 0 and board[row2 - 1][col2 + 1] == 0) and (col2 - 2 >= 6 and row2 + 2 <= 5 and board[row2 + 2][col2 - 2] == 0):
                                cost += 0.01*3
                            elif (col2 + 1 <= 6 and row2 - 1 >= 0 and board[row2 - 1][col2 + 1] == 0) or (col2 - 2 >= 6 and row2 + 2 <= 5 and board[row2 + 2][col2 - 2] == 0):
                                cost += 0.01
                        row2 += 1
                        col2 -= 1

                    row3 = 0
                    col3 = i
                    while row3 <= 5:
                        if (col3 >= 0) and (board[row3][col3] == player_number):
                            if (col3 + 1 <= 6 and row3 - 1 >= 0 and board[row3 - 1][col3 + 1] == 0) and (col3 - 1 >= 6 and row3 + 1 <= 5 and board[row3 + 1][col3 - 1] == 0):
                                cost += 0.0001*3
                            elif (col3 + 1 <= 6 and row3 - 1 >= 0 and board[row3 - 1][col3 + 1] == 0) or (col3 - 1 >= 6 and row3 + 1 <= 5 and board[row3 + 1][col3 - 1] == 0):
                                cost += 0.0001
                        row3 += 1
                        col3 -= 1

                    row4 = 0
                    col4 = i
                    while row4 + 3 <= 5:
                        if (col4 - 3 >= 0) and (board[row4][col4] == board[row4 + 1][col4 - 1] == board[row4 + 2][col4 - 2] == board[row4 + 3][col4 - 3] == player_number):
                            cost += 100

                        if (col4 - 3 >= 0) and ((board[row4][col4] == board[row4 + 2][col4 - 2] == board[row4 + 3][col4 - 3] == player_number and board[row4 + 1][col4 - 1]==0) or (board[row4][col4] == board[row4 + 1][col4 - 1] == board[row4 + 3][col4 - 3] == player_number and board[row4 + 2][col4 - 2]==0)):
                            cost += 50
                        row4 += 1
                        col4 -= 1


                for i in range(1, 6):
                    row1 = i
                    col1 = 6
                    while row1 + 2 <= 5:
                        if (col1 - 2 >= 0) and (board[row1][col1] == board[row1 + 1][col1 - 1] == board[row1 + 2][col1 - 2] == player_number):
                            if (col1 + 1 <= 6 and row1 - 1 >= 0 and board[row1 - 1][col1 + 1] == 0) and (col1 - 3 >= 0 and row1 + 3 <= 5 and board[row1 + 3][col1 - 3] == 0):
                                cost += 1*3
                            elif (col1 + 1 <= 6 and row1 - 1 >= 0 and board[row1 - 1][col1 + 1] == 0) or (col1 - 3 >= 0 and row1 + 3 <= 5 and board[row1 + 3][col1 - 3] == 0):
                                cost += 1
                            
                        row1 += 1
                        col1 -= 1

                    row2 = i
                    col2 = 6
                    while row2 + 1 <= 5:
                        if (col2 - 1 >= 0) and (board[row2][col2] == board[row2 + 1][col2 - 1] == player_number):
                            if (col2 + 1 <= 6 and row2 - 1 >= 0 and board[row2 - 1][col2 + 1] == 0) and (col2 - 2 >= 6 and row2 + 2 <= 5 and board[row2 + 2][col2 - 2] == 0):
                                cost += 0.01*3
                            elif (col2 + 1 <= 6 and row2 - 1 >= 0 and board[row2 - 1][col2 + 1] == 0) or (col2 - 2 >= 6 and row2 + 2 <= 5 and board[row2 + 2][col2 - 2] == 0):
                                cost += 0.01
                        row2 += 1
                        col2 -= 1

                    row3 = i
                    col3 = 6
                    while row3 <= 5:
                        if (col3 >= 0) and (board[row3][col3] == player_number):
                            if (col3 + 1 <= 6 and row3 - 1 >= 0 and board[row3 - 1][col3 + 1] == 0) or (col3 - 1 >= 6 and row3 + 1 <= 5 and board[row3 + 1][col3 - 1] == 0):
                                cost += 0.0001*3
                            elif (col3 + 1 <= 6 and row3 - 1 >= 0 and board[row3 - 1][col3 + 1] == 0) or (col3 - 1 >= 6 and row3 + 1 <= 5 and board[row3 + 1][col3 - 1] == 0):
                                cost += 0.0001
                            
                        row3 += 1
                        col3 -= 1

                    row4 = 0
                    col4 = i
                    while row4 + 3 <= 5:
                        if (col4 - 3 >= 0) and (board[row4][col4] == board[row4 + 1][col4 - 1] == board[row4 + 2][col4 - 2] == board[row4 + 3][col4 - 3] == player_number):
                            cost += 100

                        if (col4 - 3 >= 0) and ((board[row4][col4] == board[row4 + 2][col4 - 2] == board[row4 + 3][col4 - 3] == player_number and board[row4 + 1][col4 - 1]==0) or (board[row4][col4] == board[row4 + 1][col4 - 1] == board[row4 + 3][col4 - 3] == player_number and board[row4 + 2][col4 - 2]==0)):
                            cost += 50
                        row4 += 1
                        col4 -= 1

                return cost

            def horizontal_evaluation(board,player):
                p1_c3=0
                for i in range(len(board)):
                    for j in range(1,len(board[0])-1):
                        if board[i][j-1]==board[i][j]==board[i][j+1]==player:
                            if (j-1>0 and board[i][j-2]==0) and (j+1<len(board[0])-1 and board[i][j+2]==0): 
                                p1_c3+=1+1
                            elif (j-1>0 and board[i][j-2]==0) or (j+1<len(board[0])-1 and board[i][j+2]==0): 
                                p1_c3+=1
                            
                
                p1_c2=0
                for i in range(len(board)):
                    for j in range(len(board[0])-1):
                        if board[i][j]==board[i][j+1]==player:
                            if (j>0 and board[i][j-1]==0) and (j+1<len(board[0])-1 and board[i][j+2]==0):
                                p1_c2+=1+1
                            elif (j>0 and board[i][j-1]==0) or (j+1<len(board[0])-1 and board[i][j+2]==0):
                                p1_c2+=1

                p1_c1=0
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j]==player:
                            if (j>0 and board[i][j-1]==0) and (j<6 and board[i][j+1]==0):
                                p1_c1+=1+1
                            elif (j>0 and board[i][j-1]==0) or (j<6 and board[i][j+1]==0):
                                p1_c1+=1
                            
                            

                p1_c4=0
                for i in range(len(board)):
                    for j in range(1,len(board[0])-2):
                        if board[i][j-1]==board[i][j]==board[i][j+1]==board[i][j+2]==player:
                            # if (j-1>0 and board[i][j-2]==0) or (j+1<len(board[0])-1 and board[i][j+2]==0): 
                            p1_c4+=1

                        if (board[i][j-1]==board[i][j+1]==board[i][j+2]==player and board[i][j]==0) or (board[i][j-1]==board[i][j]==board[i][j+2]==player and board[i][j+1]==0):
                            # if (j-1>0 and board[i][j-2]==0) or (j+1<len(board[0])-1 and board[i][j+2]==0): 
                            p1_c4+=0.5
                        
                    
                

                
                player_marks=1*(p1_c3)+0.01*(p1_c2)+0.0001*(p1_c1) + 100*(p1_c4)
                return player_marks

            def vertical_evaluation(board,player):
                p1_c3=0
                for j in range(len(board[0])):
                    for i in range(1,len(board)-1):
                        if board[i-1][j]==board[i][j]==board[i+1][j]==player:
                            if (i-1>0 and board[i-2][j]==0) and (i+1<len(board)-1 and board[i+2][j]==0):
                                p1_c3+=1+1
                            elif (i-1>0 and board[i-2][j]==0) or (i+1<len(board)-1 and board[i+2][j]==0):
                                p1_c3+=1
                            
                
                p1_c2=0
                for j in range(len(board[0])):
                    for i in range(len(board)-1):
                        if board[i][j]==board[i+1][j]==player:
                            if (i>0 and board[i-1][j]==0) and (i+1<len(board)-1 and board[i+2][j]==0):
                                p1_c2+=1+1
                            elif (i>0 and board[i-1][j]==0) or (i+1<len(board)-1 and board[i+2][j]==0):
                                p1_c2+=1


                p1_c1=0
                for j in range(len(board[0])):
                    for i in range(len(board)):
                        if board[i][j]==player:
                            if (i>0 and board[i-1][j]==0) and (i<len(board)-1 and board[i+1][j]==0):
                                p1_c1+=1+1
                            elif (i>0 and board[i-1][j]==0) or (i<len(board)-1 and board[i+1][j]==0):
                                p1_c1+=1
                            

                p1_c4=0
                for j in range(len(board[0])):
                    for i in range(1,len(board)-2):
                        if board[i-1][j]==board[i][j]==board[i+1][j]==board[i+2][j]==player:
                            # if (i-1>0 and board[i-2][j]==0) or (i+1<len(board)-1 and board[i+2][j]==0):
                            p1_c4+=1

                        if (board[i-1][j]==board[i+1][j]==board[i+2][j]==player and board[i][j]==0) or (board[i-1][j]==board[i][j]==board[i+2][j]==player and board[i+1][j]==0):
                            # if (i-1>0 and board[i-2][j]==0) or (i+1<len(board)-1 and board[i+2][j]==0):
                            p1_c4+=0.5

                
                player_marks=1*(p1_c3)+0.01*(p1_c2)+0.0001*(p1_c1) + 100*(p1_c4)
                return player_marks

            eval_value = diagonallr(board,1) + diagonalrl(board,1) + horizontal_evaluation(board,1) + vertical_evaluation(board,1) - (diagonallr(board,2) + diagonalrl(board,2) + horizontal_evaluation(board,2) + vertical_evaluation(board,2))
        
            return eval_value


    def get_alpha_beta_move(self, board):
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


       
        def generate_move(board, player_number):
            board_list = []
            visited_column = []
            length = 0
            for i in range(5, -1, -1):
                for j in sorted(range(7), key=lambda x: abs(x - 3)):
                    new_board = copy.deepcopy(board)
                    if length < 7 and (j not in visited_column) and new_board[i][j] == 0:
                        visited_column.append(j)
                        new_board[i][j] = player_number
                        board_list.append(new_board)
                        length += 1
            return board_list

        # def max_value(board,alpha,beta,depth):
        #     # LIMIT = 4
        #     if depth==self.LIMIT:
        #         utility = self.evaluation_function(board)
        #         # print(utility)
        #         self.d[utility] = board
        #         return utility

        #     # M = 1e9
        #     v = -self.M
        #     actions = generate_move(board,1)
        #     for a in actions:
        #         # v = max(v,self.min_value(a,alpha,beta))
        #         v1 = min_value(a,alpha,beta,depth+1)
        #         if v1>v:
        #             v = v1
        #             # board = board1
        #             # d[v] = a

        #         self.d[v]=a

        #         if v>=beta:
        #             return v
        #         alpha = max(alpha,v)
        #     return v

        def max_value(board, alpha, beta, depth):
            if depth == self.LIMIT:
                utility = self.evaluation_function(board)
                return utility, board

            v = -self.M
            best_board = board
            actions = generate_move(board, 1)
            # lst = []
            for a in actions:
                v1, board1 = min_value(a, alpha, beta, depth + 1)
                
                if v1 >= v:
                    v = v1
                    best_board = a
                # lst.append((v1,a))

                if v >= beta:
                    return v, best_board
                alpha = max(alpha, v)

            # print(lst,"max",depth)
            # print(v)
            # print(best_board)
            return v, best_board

        # def min_value(board,alpha,beta,depth):
        #     if depth==self.LIMIT:
        #         utility = self.evaluation_function(board)
        #         self.d[utility] = board
        #         return utility
            
        #     v = self.M
        #     actions = generate_move(board,2)
        #     for a in actions:
        #         # v,d = min(v,max_value(a,alpha,beta,d))
        #         v2 = max_value(a,alpha,beta,depth+1)
        #         if v2<v:
        #             v = v2

        #         self.d[v] = a

        #         if v<=alpha:
        #             return v
        #         beta = min(beta,v)

        #     return v

        def min_value(board, alpha, beta, depth):
            if depth == self.LIMIT:
                utility = self.evaluation_function(board)
                return utility, board

            v = self.M
            best_board = None
            actions = generate_move(board, 2)
            for a in actions:
                v1, board1 = max_value(a, alpha, beta, depth + 1)
                if v1 <= v:
                    v = v1
                    best_board = a

                if v <= alpha:
                    return v, best_board
                beta = min(beta, v)
            return v, best_board

        # d = dict()
        v,next_state = max_value(board,-self.M,self.M,1)
        # next_state = self.d[v]

        req_col_index = -1
        for i in range(6):
            for j in range(7):
                if(board[i][j]!=next_state[i][j]):
                    req_col_index = j
                    break
            if req_col_index!=-1:
                break
               
        return req_col_index
        
        # raise NotImplementedError('Whoops I don\'t know what to do')



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
        # raise NotImplementedError('Whoops I don\'t know what to do')
        def generate_move(board, player_number):
            board_list = []
            visited_column = []
            length = 0
            for i in range(5, -1, -1):
                for j in sorted(range(7), key=lambda x: abs(x - 3)):
                    new_board = copy.deepcopy(board)
                    if length < 7 and (j not in visited_column) and new_board[i][j] == 0:
                        visited_column.append(j)
                        new_board[i][j] = player_number
                        board_list.append(new_board)
                        length += 1
            return board_list

        def min_value1(board, alpha, beta, depth):
            if depth == self.LIMIT:
                utility = self.evaluation_function(board)
                return utility

            # v = self.M
            v = 0
            average = 0
            best_board = None
            actions = generate_move(board, 2)
            for a in actions:
                v1, board1 = max_value1(a, alpha, beta, depth + 1)
                if v1 <= v:
                    # v = v1
                    best_board = a
                v += v1
                average += v1
            
                # if v <= alpha:
                #     return v, best_board
                beta = min(beta, v)
            # v = v/7
            return average/7

        def max_value1(board, alpha, beta, depth):
            if depth == self.LIMIT:
                utility = self.evaluation_function(board)
                return utility, board

            v = -self.M
            best_board = board
            actions = generate_move(board, 1)
            # lst = []
            for a in actions:
                v1 = min_value1(a, alpha, beta, depth + 1)
                print(v1)
                if v1 >= v:
                    v = v1
                    best_board = a
                # lst.append((v1,a))

                # if v >= beta:
                #     return v, best_board
                alpha = max(alpha, v)

            # print(lst,"max",depth)
            # print(v)
            # print(best_board)
            return v, best_board

        

        # d = dict()
        v,next_state = max_value1(board,-self.M,self.M,1)
        # next_state = self.d[v]

        req_col_index = -1
        for i in range(6):
            for j in range(7):
                if(board[i][j]!=next_state[i][j]):
                    req_col_index = j
                    break
            if req_col_index!=-1:
                break
               
        return req_col_index

        
        


        


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


#  //////


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
        # def generate_move(board, player_number):
        #     board_list = []
        #     visited_column = []
        #     length = 0
        #     for i in range(5, -1, -1):
        #         for j in sorted(range(7), key=lambda x: abs(x - 3)):
        #             new_board = copy.deepcopy(board)
        #             if length < 7 and (j not in visited_column) and new_board[i][j] == 0:
        #                 visited_column.append(j)
        #                 new_board[i][j] = player_number
        #                 board_list.append(new_board)
        #                 length += 1
        #     return board_list
        
        # def max_value(board, alpha, beta, depth):
        #     if depth == self.LIMIT:
        #         utility = self.evaluation_function(board)
        #         return utility, board
            
        #     # pro=(1/6)
        #     v = -self.M
        #     best_board = None
        #     actions = generate_move(board, 1)
        #     lst = []
        #     for a in actions:
        #         v1 = min_value(a, alpha, beta, depth + 1)
        #         # v+=v1*pro
        #         if v1 > v:
        #             v = v1
        #             best_board = a
        #         # lst.append((v1,a))

        #         if v >= beta:
        #             return v, best_board
        #         alpha = max(alpha, v)

        #     # print(lst,"max")
        #     return v,best_board
        
        # def min_value(board, alpha, beta, depth):
        #     if depth == self.LIMIT:
        #         utility = self.evaluation_function(board)
        #         return utility

        #     pro=(1/7)
        #     v = 0
        #     best_board = None
        #     actions = generate_move(board, 2)
        #     for a in actions:
        #         v1, board1 = max_value(a, alpha, beta, depth + 1)
        #         v+=v1*pro
        #         # if v1 < v:
        #         #     # v = v1
        #         #     best_board = a

        #         # if v <= alpha
        #         #     return v, best_board
        #         # beta = min(beta, v)
        #     return v
        
        # # def chance(board):


        # # d = dict()
        # v,next_state = max_value(board,-self.M,self.M,1)
        # # next_state = self.d[v]


        # req_col_index = -1
        # for i in range(6):
        #     for j in range(7):
        #         if(board[i][j]!=next_state[i][j]):
        #             req_col_index = j
        #             break
        #     if req_col_index!=-1:
        #         break
               
        # return req_col_index

