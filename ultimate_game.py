import os
import random
from model import TicTacToeModel
import copy

players = dict()
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
DRAW = 'D'
PLAYER_X_VAL = -1
PLAYER_O_VAL = 1
EMPTY_VAL = 0
DRAW_VAL = 2
players[PLAYER_X_VAL] = PLAYER_X
players[PLAYER_O_VAL] = PLAYER_O
players[EMPTY_VAL] = EMPTY
players[DRAW_VAL] = DRAW
HORIZONTAL_SEPARATOR = ' | '
VERTICAL_SEPARATOR = '---------------'
GAME_STATE_X = -1
GAME_STATE_O = 1
GAME_STATE_DRAW = 2
GAME_STATE_NOT_ENDED = 0


class Game():

    def __init__(self):
        self.resetBoard()
        self.trainingHistory = []
        self.convenient_indexer = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def resetBoard(self):
# =============================================================================
#         initializes board states and clears board at the start of each new game
# =============================================================================
        self.miniBoard1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard2 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard3 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard4 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard5 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard6 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard7 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard8 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.miniBoard9 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.fullBoard = [self.miniBoard1, self.miniBoard2, self.miniBoard3,
                          self.miniBoard4, self.miniBoard5, self.miniBoard6,
                          self.miniBoard7, self.miniBoard8, self.miniBoard9]
        self.macroBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.macroBoardHistory = []
        self.fullBoardHistory = []

    def printBoard(self):
# =============================================================================
#         prints current board to screen
# =============================================================================
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard1[0][0])] + ' || ' + players[(self.miniBoard1[0][1])] + ' || ' + players[(
            self.miniBoard1[0][2])] + ' |   | '
              + players[(self.miniBoard2[0][0])] + ' || ' + players[(self.miniBoard2[0][1])] + ' || ' + players[(
            self.miniBoard2[0][2])] + ' |   | '
              + players[(self.miniBoard3[0][0])] + ' || ' + players[(self.miniBoard3[0][1])] + ' || ' + players[(
            self.miniBoard3[0][2])] + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard1[1][0])] + ' || ' + players[(self.miniBoard1[1][1])] + ' || ' + players[(
            self.miniBoard1[1][2])] + ' |   | '
              + players[(self.miniBoard2[1][0])] + ' || ' + players[(self.miniBoard2[1][1])] + ' || ' + players[(
            self.miniBoard2[1][2])] + ' |   | '
              + players[(self.miniBoard3[1][0])] + ' || ' + players[(self.miniBoard3[1][1])] + ' || ' + players[(
            self.miniBoard3[1][2])] + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard1[2][0])] + ' || ' + players[(self.miniBoard1[2][1])] + ' || ' + players[(
            self.miniBoard1[2][2])] + ' |   | '
              + players[(self.miniBoard2[2][0])] + ' || ' + players[(self.miniBoard2[2][1])] + ' || ' + players[(
            self.miniBoard2[2][2])] + ' |   | '
              + players[(self.miniBoard3[2][0])] + ' || ' + players[(self.miniBoard3[2][1])] + ' || ' + players[(
            self.miniBoard3[2][2])] + ' |')
        print('----------------  ----------------  ----------------')
        # Second row of boards
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard4[0][0])] + ' || ' + players[(self.miniBoard4[0][1])] + ' || ' + players[(
            self.miniBoard4[0][2])] + ' |   | '
              + players[(self.miniBoard5[0][0])] + ' || ' + players[(self.miniBoard5[0][1])] + ' || ' + players[(
            self.miniBoard5[0][2])] + ' |   | '
              + players[(self.miniBoard6[0][0])] + ' || ' + players[(self.miniBoard6[0][1])] + ' || ' + players[(
            self.miniBoard6[0][2])] + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard4[1][0])] + ' || ' + players[(self.miniBoard4[1][1])] + ' || ' + players[(
            self.miniBoard4[1][2])] + ' |   | '
              + players[(self.miniBoard5[1][0])] + ' || ' + players[(self.miniBoard5[1][1])] + ' || ' + players[(
            self.miniBoard5[1][2])] + ' |   | '
              + players[(self.miniBoard6[1][0])] + ' || ' + players[(self.miniBoard6[1][1])] + ' || ' + players[(
            self.miniBoard6[1][2])] + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard4[2][0])] + ' || ' + players[(self.miniBoard4[2][1])] + ' || ' + players[(
            self.miniBoard4[2][2])] + ' |   | '
              + players[(self.miniBoard5[2][0])] + ' || ' + players[(self.miniBoard5[2][1])] + ' || ' + players[(
            self.miniBoard5[2][2])] + ' |   | '
              + players[(self.miniBoard6[2][0])] + ' || ' + players[(self.miniBoard6[2][1])] + ' || ' + players[(
            self.miniBoard6[2][2])] + ' |')
        print('----------------  ----------------  ----------------')
        # Third row of boards and overall board
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard7[0][0])] + ' || ' + players[(self.miniBoard7[0][1])] + ' || ' + players[(
            self.miniBoard7[0][2])] + ' |   | '
              + players[(self.miniBoard8[0][0])] + ' || ' + players[(self.miniBoard8[0][1])] + ' || ' + players[(
            self.miniBoard8[0][2])] + ' |   | '
              + players[(self.miniBoard9[0][0])] + ' || ' + players[(self.miniBoard9[0][1])] + ' || ' + players[(
            self.miniBoard9[0][2])] + ' |   | '
              + players[(self.macroBoard[0][0])] + ' || ' + players[(self.macroBoard[0][1])] + ' || ' + players[(
            self.macroBoard[0][2])] + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard7[1][0])] + ' || ' + players[(self.miniBoard7[1][1])] + ' || ' + players[(
            self.miniBoard7[1][2])] + ' |   | '
              + players[(self.miniBoard8[1][0])] + ' || ' + players[(self.miniBoard8[1][1])] + ' || ' + players[(
            self.miniBoard8[1][2])] + ' |   | '
              + players[(self.miniBoard9[1][0])] + ' || ' + players[(self.miniBoard9[1][1])] + ' || ' + players[(
            self.miniBoard9[1][2])] + ' |   | '
              + players[(self.macroBoard[1][0])] + ' || ' + players[(self.macroBoard[1][1])] + ' || ' + players[(
            self.macroBoard[1][2])] + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + players[(self.miniBoard7[2][0])] + ' || ' + players[(self.miniBoard7[2][1])] + ' || ' + players[(
            self.miniBoard7[2][2])] + ' |   | '
              + players[(self.miniBoard8[2][0])] + ' || ' + players[(self.miniBoard8[2][1])] + ' || ' + players[(
            self.miniBoard8[2][2])] + ' |   | '
              + players[(self.miniBoard9[2][0])] + ' || ' + players[(self.miniBoard9[2][1])] + ' || ' + players[(
            self.miniBoard9[2][2])] + ' |   | '
              + players[(self.macroBoard[2][0])] + ' || ' + players[(self.macroBoard[2][1])] + ' || ' + players[(
            self.macroBoard[2][2])] + ' |')
        print('----------------  ----------------  ----------------')

    def check_current_state(self, board_number):
# =============================================================================
#         examines state of specific boards
# =============================================================================
        # Check if draw
        board = []
        if board_number < 10:
            board = self.fullBoard[board_number - 1]
        elif board_number == 10:
            board = self.macroBoard

        # Check horizontals
        if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not 0):
            return board[0][0], "Done"
        if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not 0):
            return board[1][0], "Done"
        if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not 0):
            return board[2][0], "Done"

        # Check verticals
        if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not 0):
            return board[0][0], "Done"
        if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not 0):
            return board[0][1], "Done"
        if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not 0):
            return board[0][2], "Done"

        # Check diagonals
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not 0):
            return board[1][1], "Done"
        if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] is not 0):
            return board[1][1], "Done"
        if len(self.getAvailableMoves(board_number)) == 0:
            return None, "Draw"

        return None, "Not Done"

    def getGameResult(self):
# =============================================================================
#         examines state of the macro board
# =============================================================================
        for i in range(len(self.macroBoard)):
            for j in range(len(self.macroBoard[i])):
                if self.macroBoard[i][j] == EMPTY_VAL:
                    return GAME_STATE_NOT_ENDED

        # Rows
        for i in range(len(self.macroBoard)):
            candidate = self.macroBoard[i][0]
            for j in range(len(self.macroBoard[i])):
                if candidate != self.macroBoard[i][j]:
                    candidate = 0
            if candidate != 0:
                return candidate

        # Columns
        for i in range(len(self.macroBoard)):
            candidate = self.macroBoard[0][i]
            for j in range(len(self.macroBoard[i])):
                if candidate != self.macroBoard[j][i]:
                    candidate = 0
            if candidate != 0:
                return candidate

        # First diagonal
        candidate = self.macroBoard[0][0]
        for i in range(len(self.macroBoard)):
            if candidate != self.macroBoard[i][i]:
                candidate = 0
        if candidate != 0:
            return candidate

        # Second diagonal
        candidate = self.macroBoard[0][2]
        for i in range(len(self.macroBoard)):
            if candidate != self.macroBoard[i][len(self.macroBoard[i]) - i - 1]:
                candidate = 0
        if candidate != 0:
            return candidate

        return GAME_STATE_DRAW

    def getAvailableMoves(self, board_restriction):
        # =============================================================================
        #         looks at specific board for available moves
        # =============================================================================
        availableMoves = []
#        print(board_restriction)
        try:
            if board_restriction < 10:
                board = self.fullBoard[board_restriction - 1]
                for i in range(3):
                    for j in range(3):
                        if (board[i][j]) == EMPTY_VAL:
                            availableMoves.append([i, j])
            elif board_restriction == 10:
                board = self.macroBoard
                for i in range(3):
                    for j in range(3):
                        if (board[i][j]) == EMPTY_VAL:
                            availableMoves.append([i, j])
            elif board_restriction == 11:
                board = self.fullBoard
                for i in range(9):
                    for j in range(3):
                        for k in range(3):
                            if (board[i][j][k]) == EMPTY_VAL:
                                availableMoves.append([i, j, k])
        except TypeError:
            print(board_restriction)
            raise TypeError

        return availableMoves

    def confirmBoard(self, board_num):
# =============================================================================
#         determines if a board is complete or if can be played on
# =============================================================================
        for i in range(3):
            for j in range(3):
                if self.convenient_indexer[i][j] == board_num:
                    if self.macroBoard[i][j] != 0:
                        #   Player may choose any available board to play on if current is finished
#                        availableBoards = self.getAvailableMoves(10)
#                        choice = random.randint(0, availableBoards.__len__() - 1)
                        board_num = 11
                        return board_num #self.convenient_indexer[availableBoards[choice][0]][availableBoards[choice][1]]
                    else:
                        return board_num
        if board_num == 11:
            return board_num

    def addToHistory(self, fullBoard):
# =============================================================================
#         adds to the board history
# =============================================================================
        self.fullBoardHistory.append(fullBoard)

    def printHistory(self):
# =============================================================================
#         prints the board history
# =============================================================================
        print(self.fullBoardHistory)

    def move(self, position, player, board_restriction):
# =============================================================================
#         marks player moves in the correct positions on the different boards
# =============================================================================
        try:
            self.fullBoard[board_restriction - 1][position[0]][position[1]] = player
        except TypeError:
            print('board restriction is ' + str(board_restriction))
            print('position is '+ str(position))
            
            raise TypeError
            
        winner, done = self.check_current_state(board_restriction)
        if (done == "Done"):
            for x in range(3):
                for y in range(3):
                    if self.convenient_indexer[x][y] == board_restriction:
                        self.macroBoard[x][y] = player
                        self.addToHistory(copy.deepcopy(self.fullBoard))
        if (done == "Draw"):
            for x in range(3):
                for y in range(3):
                    if self.convenient_indexer[x][y] == board_restriction:
                        self.macroBoard[x][y] = DRAW_VAL
                        self.addToHistory(copy.deepcopy(self.fullBoard))

    def fullSimulate(self, playerToMove):
        # =============================================================================
        #         simulates game with players moving randomly, using full ultimate board
        # =============================================================================
        board_num = random.randint(1,9)
        done = "Not Done"
        winner = None
        while (done == "Not Done"):
            board_num = self.confirmBoard(board_num)
            if board_num == 11:
                availableBoards = self.getAvailableMoves(10)
                availableBoardNums = []
                for board in availableBoards:
                    availableBoardNums.append(self.convenient_indexer[board[0]][board[1]])
                allAvailableMoves = []
                for boardNum in availableBoardNums:
                    allAvailableMoves.append([boardNum, self.getAvailableMoves(boardNum)])
                try:
                    selectedMove = allAvailableMoves[random.randrange(0, len(allAvailableMoves))]
                    board_num = selectedMove[0]
                    a = selectedMove
                    selectedMove.remove(selectedMove[0])
                    selectedMove = selectedMove[0][random.randrange(0, len(selectedMove))]
                    self.move(selectedMove, playerToMove, board_num)
                except ValueError:
                    self.printBoard()
                    print("available moves are " + str(allAvailableMoves))
                    print("board num is " + str(board_num))
                    raise ValueError
                except TypeError:
                    self.printBoard()
                    print(allAvailableMoves)
                    print('selected move is ' + str(a))
                    
                
                
            else:
                allAvailableMoves = self.getAvailableMoves(board_num)
                try:
                    selectedMove = allAvailableMoves[random.randrange(0, len(allAvailableMoves))]
                    self.move(selectedMove, playerToMove, board_num)
                except ValueError:
                    self.printBoard()
                    print("available moves are " + str(allAvailableMoves))
                    print("board num is " + str(board_num))
                    raise ValueError
            
            
            board_num = self.convenient_indexer[selectedMove[0]][selectedMove[1]]
            winner, done = self.check_current_state(10)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
        # Get the history and build the training set
        for historyItem in self.fullBoardHistory:
            self.trainingHistory.append((self.getGameResult(), copy.deepcopy(historyItem)))

    def fullSimulateNeuralNetwork(self, nnPlayer, model):
        # =============================================================================
        #         simulates game with a player moving from learning experience, using full ultimate board
        # =============================================================================
        playerToMove = PLAYER_X_VAL
        state = "Not Done"
        board_index = 11
        while (state == "Not Done"):
            board_index = self.confirmBoard(board_index)
            if board_index == 11:
                availableBoards = self.getAvailableMoves(10)
                availableBoardNums = []
                for board in availableBoards:
                    availableBoardNums.append(self.convenient_indexer[board[0]][board[1]])
                allAvailableMoves = []
                for boardNum in availableBoardNums:
                    allAvailableMoves.append([boardNum, self.getAvailableMoves(boardNum)])
                if playerToMove == nnPlayer:
                    maxValue = 0
                    bestMove = allAvailableMoves[0]
                    for boardNum in allAvailableMoves:
                        for availableMove in boardNum[1]:
                            # get a copy of a board
                            boardCopy = copy.deepcopy(self.fullBoard)
#                            print('availableMove is ' + str(availableMove))
                            boardCopy[boardNum[0] - 1][availableMove[0]][availableMove[1]] = nnPlayer
                            if nnPlayer == PLAYER_X_VAL:
                                value = model.predict(boardCopy, 0)
                            else:
                                value = model.predict(boardCopy, 2)
                            if value > maxValue:
                                maxValue = value
                                bestMove = [boardNum[0], availableMove]
                    selectedMove = bestMove[1]
                    board_index = bestMove[0]
                else:
                    availableBoards = self.getAvailableMoves(10)
                    availableBoardNums = []
                    for board in availableBoards:
                        availableBoardNums.append(self.convenient_indexer[board[0]][board[1]])
                    choice = random.randint(0, availableBoardNums.__len__()-1)
                    board_index = availableBoardNums[choice]
                    selectedMove = random.choice(self.getAvailableMoves(board_index))

            else:
                allAvailableMoves = self.getAvailableMoves(board_index)
                if playerToMove == nnPlayer:
                    maxValue = 0
                    bestMove = allAvailableMoves[0]
                    for availableMove in allAvailableMoves:
                        # get a copy of a board
                        boardCopy = copy.deepcopy(self.fullBoard)
                        boardCopy[board_index - 1][availableMove[0]][availableMove[1]] = nnPlayer
                        if nnPlayer == PLAYER_X_VAL:
                            value = model.predict(boardCopy, 0)
                        else:
                            value = model.predict(boardCopy, 2)
                        if value > maxValue:
                            maxValue = value
                            bestMove = availableMove
                    selectedMove = bestMove
                else:
                    selectedMove = allAvailableMoves[random.randrange(0, len(allAvailableMoves))]
                    
#            if type(selectedMove) == int or type(selectedMove) == str:
#                for x in range(3):
#                    for y in range(3):
#                        if self.convenient_indexer[x][y] == selectedMove:
#                            selectedMove = [x,y]
            self.move(selectedMove, playerToMove, board_index)
            board_index = self.convenient_indexer[selectedMove[0]][selectedMove[1]]
            winner, state = self.check_current_state(10)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL

    def getRowAndColumn(self, block_number):
# =============================================================================
#         converts human block input to the row and column positions
# =============================================================================
        block_choice = 'invalid'
        while block_choice == 'invalid':
            if block_number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                block_choice = 'valid'
            else:
                block_number = int(input('Choice was invalid--Please choose a number between 1 and 9: '))
        if str(block_number) in '123':
            row = 0
        elif str(block_number) in '456':
            row = 1
        elif str(block_number) in '789':
            row = 2
        else:
            block_number = int(input('Choice was invalid--Please choose a number between 1 and 9: '))

        if str(block_number) in '147':
            column = 0
        elif str(block_number) in '258':
            column = 1
        elif str(block_number) in '369':
            column = 2
        return row, column

    def chooseBoard(self):
# =============================================================================
#         allows the human to choose a board when needed
# =============================================================================
        board_choice = 'invalid'
        availableBoards = self.getAvailableMoves(10)
        availableBoardNums = []
        for board in availableBoards:
            availableBoardNums.append(self.convenient_indexer[board[0]][board[1]])
        while board_choice == 'invalid':
            board_index = int(input('Choose a board index 1-9: '))
            if board_index in availableBoardNums:
                board_choice = 'valid'
            else:
                board_index = int(input('Please a valid board index 1-9: '))
        return board_index

    def personVsAIgame(self, nnPlayer, model):
        # =============================================================================
        #         real human can play a game against the AI, using the full ultimate board
        # =============================================================================
        playerToMove = PLAYER_X_VAL
        state = "Not Done"
        board_index = 11
        while (state == "Not Done"):
           board_index = self.confirmBoard(board_index)
           if board_index == 11:
                availableBoards = self.getAvailableMoves(10)
                availableBoardNums = []
                for board in availableBoards:
                    availableBoardNums.append(self.convenient_indexer[board[0]][board[1]])
                allAvailableMoves = []
                for boardNum in availableBoardNums:
                    allAvailableMoves.append([boardNum, self.getAvailableMoves(boardNum)])
                if playerToMove == nnPlayer:
                    maxValue = 0
                    bestMove = allAvailableMoves[0]
                    for boardNum in allAvailableMoves:
                        for availableMove in boardNum[1]:
                            # get a copy of a board
                            boardCopy = copy.deepcopy(self.fullBoard)
#                            print('availableMove is ' + str(availableMove))
                            boardCopy[boardNum[0] - 1][availableMove[0]][availableMove[1]] = nnPlayer
                            if nnPlayer == PLAYER_X_VAL:
                                value = model.predict(boardCopy, 0)
                            else:
                                value = model.predict(boardCopy, 2)
                            if value > maxValue:
                                maxValue = value
                                bestMove = [boardNum[0], availableMove]
                    selectedMove = bestMove[1]
                    board_index = bestMove[0]
                    print("Your robotic opponent plays on board {0} in block {1}".format(board_index,self.convenient_indexer[selectedMove[0]][selectedMove[1]]))
                else:
                    board_index = self.chooseBoard()
                    allAvailableMoves = self.getAvailableMoves(board_index)
                    print("Puny human dares to play against the mighty AI!")
                    print('You must play on board {}'.format(board_index))
                    moveValidity = 'invalid'
                    while moveValidity == 'invalid':
                        selectedRow, selectedColumn = self.getRowAndColumn(
                            int(input('Please choose an empty block to play in: ')))
                        selectedMove = [selectedRow, selectedColumn]
                        if selectedMove in allAvailableMoves:
                            moveValidity = 'valid'
                        else:
                            print('Your move choice was invalid, please choose again.')
                    print("Human playing move: {}".format(selectedMove))
           else:
                allAvailableMoves = self.getAvailableMoves(board_index)
                if playerToMove == nnPlayer:
                    maxValue = 0
                    bestMove = allAvailableMoves[0]
                    for availableMove in allAvailableMoves:
                        # get a copy of a board
                        boardCopy = copy.deepcopy(self.fullBoard)
                        boardCopy[board_index - 1][availableMove[0]][availableMove[1]] = nnPlayer
                        if nnPlayer == PLAYER_X_VAL:
                            value = model.predict(boardCopy, 0)
                        else:
                            value = model.predict(boardCopy, 8)
                        if value > maxValue:
                            maxValue = value
                            bestMove = availableMove
                    selectedMove = bestMove
                    print("Your robotic opponent plays on board {0} in block {1}".format(board_index,self.convenient_indexer[selectedMove[0]][selectedMove[1]]))
                else:
                    print("Puny human dares to play against the mighty AI!")
                    print('You must play on board {}'.format(board_index))
                    moveValidity = 'invalid'
                    while moveValidity == 'invalid':
                        selectedRow, selectedColumn = self.getRowAndColumn(
                            int(input('Please choose an empty block to play in: ')))
                        selectedMove = [selectedRow, selectedColumn]
                        if selectedMove in allAvailableMoves:
                            moveValidity = 'valid'
                        else:
                            print('Your move choice was invalid, please choose again.')
                    print("Human playing on board {0} in block {1}".format(board_index, self.convenient_indexer[selectedMove[0]][selectedMove[1]]))
           self.move(selectedMove, playerToMove, board_index)
           self.printBoard()
           board_index = self.convenient_indexer[selectedMove[0]][selectedMove[1]]
           winner, state = self.check_current_state(10)
           if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
           else:
                playerToMove = PLAYER_X_VAL


    def getTrainingHistory(self):
# =============================================================================
#         retrieves the training history
# =============================================================================
        return self.trainingHistory

    def fullSimulateManyGames(self, playerToMove, numberOfGames):
        # =============================================================================
        #         simulates many games with only players moving randomly using
        #       using the full ultimate board        
        # =============================================================================
        playerXWins = 0
        playerOWins = 0
        draws = 0
        for i in range(numberOfGames):
            self.resetBoard()
            self.fullSimulate(playerToMove)
            if self.getGameResult() == PLAYER_X_VAL:
                playerXWins = playerXWins + 1
            elif self.getGameResult() == PLAYER_O_VAL:
                playerOWins = playerOWins + 1
            elif self.getGameResult() == DRAW_VAL:
                draws = draws + 1
        totalWins = playerXWins + playerOWins + draws
        print('X Wins: ' + str(int(playerXWins * 100 / totalWins)) + '%')
        print('O Wins: ' + str(int(playerOWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')
        print("Full sim complete")

    def simulateManyNeuralNetworkGames(self, nnPlayer, numberOfGames, model):
        # =============================================================================
        #         simulates many games with the neural network player against a player making random moves
        # =============================================================================
        nnPlayerWins = 0
        randomPlayerWins = 0
        draws = 0
        print("NN player")
        print(nnPlayer)
        for i in range(numberOfGames):
            self.resetBoard()
            self.fullSimulateNeuralNetwork(nnPlayer, model)
            winner, done = self.check_current_state(10)
            if winner == nnPlayer:
                nnPlayerWins = nnPlayerWins + 1
            elif done == "Draw":
                draws = draws + 1
            else:
                randomPlayerWins = randomPlayerWins + 1
        totalWins = nnPlayerWins + randomPlayerWins + draws
        print(nnPlayerWins)
        print(randomPlayerWins)
        print('NN Wins: ' + str(int(nnPlayerWins * 100 / totalWins)) + '%')
        print('Random Wins: ' + str(int(randomPlayerWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')
        print("NN Sim complete")

    def simulatePvCgame(self, nnPlayer, model):
        # =============================================================================
        #         simulates a game between person and computer
        # =============================================================================
        nnPlayerWins = 0
        humanPlayerWins = 0
        draws = 0
        print('----------------------------------------------------------------------------')
        print("NN player value: {}".format(nnPlayer))

        person = input('Do you want to play? ')
        while person != 'No' or person != 'no':
            self.resetBoard()
            self.personVsAIgame(nnPlayer, model)
            self.printBoard()
            if self.getGameResult() == nnPlayer:
                nnPlayerWins = nnPlayerWins + 1
            elif self.getGameResult() == GAME_STATE_DRAW:
                draws = draws + 1
            else:
                humanPlayerWins = humanPlayerWins + 1
            person = input('Do you want to play again?: say "No" if not ')
        totalWins = nnPlayerWins + humanPlayerWins + draws
        if nnPlayer == PLAYER_X_VAL:
            xPlayerWins = nnPlayerWins
            oPlayerWins = humanPlayerWins
        else:
            xPlayerWins = humanPlayerWins
            oPlayerWins = nnPlayerWins
        print("NN player value: {}".format(nnPlayer))
        print('X Wins: ' + str(int(xPlayerWins * 100 / totalWins)) + '%')
        print('O Wins: ' + str(int(oPlayerWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')
        print("This duel of Man vs. Machine has ended.")


if __name__ == "__main__":
    game = Game()
    game.fullSimulateManyGames(-1, 2000)
    ticTacToeModel = TicTacToeModel(81, 9, 100, 32)
    ticTacToeModel.train(game.getTrainingHistory())
    print("Simulating with Neural Network as X Player:")
    game.simulateManyNeuralNetworkGames(PLAYER_X_VAL, 10, ticTacToeModel)
    print("Simulating with Neural Network as O Player:")
    game.simulateManyNeuralNetworkGames(PLAYER_O_VAL, 10, ticTacToeModel)
    game.simulatePvCgame(PLAYER_O_VAL, ticTacToeModel)
