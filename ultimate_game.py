# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:05:34 2020
@author: nleach
"""

import os
import random
from model import TicTacToeModel
import copy

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
PLAYER_X_VAL = -1
PLAYER_O_VAL = 1
EMPTY_VAL = 0
HORIZONTAL_SEPARATOR = ' | '
VERTICAL_SEPARATOR = '---------------'
GAME_STATE_X = -1
GAME_STATE_O = 1
GAME_STATE_DRAW = 0
GAME_STATE_NOT_ENDED = 2


class Game():

    def __init__(self):
        self.resetBoard()
        self.trainingHistory = []
        self.convenient_indexer = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def resetBoard(self):
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
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard1[0][0]) + ' || ' + str(self.miniBoard1[0][1]) + ' || ' + str(self.miniBoard1[0][2]) + ' |   | '
              + str(self.miniBoard2[0][0]) + ' || ' + str(self.miniBoard2[0][1]) + ' || ' + str(self.miniBoard2[0][2]) + ' |   | '
              + str(self.miniBoard3[0][0]) + ' || ' + str(self.miniBoard3[0][1]) + ' || ' + str(self.miniBoard3[0][2]) + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard1[1][0]) + ' || ' + str(self.miniBoard1[1][1]) + ' || ' + str(self.miniBoard1[1][2]) + ' |   | '
              + str(self.miniBoard2[1][0]) + ' || ' + str(self.miniBoard2[1][1]) + ' || ' + str(self.miniBoard2[1][2]) + ' |   | '
              + str(self.miniBoard3[1][0]) + ' || ' + str(self.miniBoard3[1][1]) + ' || ' + str(self.miniBoard3[1][2]) + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard1[0][0]) + ' || ' + str(self.miniBoard1[2][1]) + ' || ' + str(self.miniBoard1[2][2]) + ' |   | '
              + str(self.miniBoard2[0][0]) + ' || ' + str(self.miniBoard2[2][1]) + ' || ' + str(self.miniBoard2[2][2]) + ' |   | '
              + str(self.miniBoard3[0][0]) + ' || ' + str(self.miniBoard3[2][1]) + ' || ' + str(self.miniBoard3[2][2]) + ' |')
        print('----------------  ----------------  ----------------')
        # Second row of boards
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard4[0][0]) + ' || ' + str(self.miniBoard4[0][1]) + ' || ' + str(self.miniBoard4[0][2]) + ' |   | '
              + str(self.miniBoard5[0][0]) + ' || ' + str(self.miniBoard5[0][1]) + ' || ' + str(self.miniBoard5[0][2]) + ' |   | '
              + str(self.miniBoard6[0][0]) + ' || ' + str(self.miniBoard6[0][1]) + ' || ' + str(self.miniBoard6[0][2]) + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard4[1][0]) + ' || ' + str(self.miniBoard4[1][1]) + ' || ' + str(self.miniBoard4[1][2]) + ' |   | '
              + str(self.miniBoard5[1][0]) + ' || ' + str(self.miniBoard5[1][1]) + ' || ' + str(self.miniBoard5[1][2]) + ' |   | '
              + str(self.miniBoard6[1][0]) + ' || ' + str(self.miniBoard6[1][1]) + ' || ' + str(self.miniBoard6[1][2]) + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard4[2][0]) + ' || ' + str(self.miniBoard4[2][1]) + ' || ' + str(self.miniBoard4[2][2]) + ' |   | '
              + str(self.miniBoard5[2][0]) + ' || ' + str(self.miniBoard5[2][1]) + ' || ' + str(self.miniBoard5[2][2]) + ' |   | '
              + str(self.miniBoard6[2][0]) + ' || ' + str(self.miniBoard6[2][1]) + ' || ' + str(self.miniBoard6[2][2]) + ' |')
        print('----------------  ----------------  ----------------')
        # Third row of boards and overall board
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard7[0][0]) + ' || ' + str(self.miniBoard7[0][1]) + ' || ' + str(self.miniBoard7[0][2]) + ' |   | '
              + str(self.miniBoard8[0][0]) + ' || ' + str(self.miniBoard8[0][1]) + ' || ' + str(self.miniBoard8[0][2]) + ' |   | '
              + str(self.miniBoard9[0][0]) + ' || ' + str(self.miniBoard9[0][1]) + ' || ' + str(self.miniBoard9[0][2]) + ' |   | '
              + str(self.macroBoard[0][0]) + ' || ' + str(self.macroBoard[0][1]) + ' || ' + str(self.macroBoard[0][2]) + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard7[1][0]) + ' || ' + str(self.miniBoard7[1][1]) + ' || ' + str(self.miniBoard7[1][2]) + ' |   | '
              + str(self.miniBoard8[1][0]) + ' || ' + str(self.miniBoard8[1][1]) + ' || ' + str(self.miniBoard8[1][2]) + ' |   | '
              + str(self.miniBoard9[1][0]) + ' || ' + str(self.miniBoard9[1][1]) + ' || ' + str(self.miniBoard9[1][2]) + ' |   | '
              + str(self.macroBoard[1][0]) + ' || ' + str(self.macroBoard[1][1]) + ' || ' + str(self.macroBoard[1][2]) + ' |')
        print('----------------  ----------------  ----------------')
        print('| ' + str(self.miniBoard7[2][0]) + ' || ' + str(self.miniBoard7[2][1]) + ' || ' + str(self.miniBoard7[2][2]) + ' |   | '
              + str(self.miniBoard8[2][0]) + ' || ' + str(self.miniBoard8[2][1]) + ' || ' + str(self.miniBoard8[2][2]) + ' |   | '
              + str(self.miniBoard9[2][0]) + ' || ' + str(self.miniBoard9[2][1]) + ' || ' + str(self.miniBoard9[2][2]) + ' |   | '
              + str(self.macroBoard[2][0]) + ' || ' + str(self.macroBoard[2][1]) + ' || ' + str(self.macroBoard[2][2]) + ' |')
        print('----------------  ----------------  ----------------')

    def check_current_state(self, board_number):
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
    '''
    def getMiniGameResult(self, miniBoard):
        # =============================================================================
        #         checks results for a specified miniBoard
        # =============================================================================
        for i in range(len(miniBoard)):
            for j in range(len(miniBoard[i])):
                if miniBoard[i][j] == EMPTY_VAL:
                    return GAME_STATE_NOT_ENDED

        # Rows
        for i in range(len(miniBoard)):
            candidate = miniBoard[i][0]
            for j in range(len(miniBoard[i])):
                if candidate != miniBoard[i][j]:
                    candidate = 0
            if candidate != 0:
                return candidate

        # Columns
        for i in range(len(miniBoard)):
            candidate = miniBoard[0][i]
            for j in range(len(miniBoard[i])):
                if candidate != miniBoard[j][i]:
                    candidate = 0
            if candidate != 0:
                return candidate

        # First diagonal
        candidate = miniBoard[0][0]
        for i in range(len(miniBoard)):
            if candidate != miniBoard[i][i]:
                candidate = 0
        if candidate != 0:
            return candidate

        # Second diagonal
        candidate = miniBoard[0][2]
        for i in range(len(miniBoard)):
            if candidate != miniBoard[i][len(miniBoard[i]) - i - 1]:
                candidate = 0
        if candidate != 0:
            return candidate

        return GAME_STATE_DRAW
    '''

    def getAvailableMoves(self, board_restriction):
        # =============================================================================
        #         looks at specific board
        # =============================================================================
        availableMoves = []
        if board_restriction < 10:
            board = self.fullBoard[board_restriction - 1]
        elif board_restriction == 10:
            board = self.macroBoard
        for i in range(3):
            for j in range(3):
                if (board[i][j]) == EMPTY_VAL:
                    availableMoves.append([i, j])

        return availableMoves

    def confirmBoard(self, board_num):
        for i in range(3):
            for j in range(3):
                if self.convenient_indexer[i][j] == board_num:
                    if self.macroBoard[i][j] is not 0:
                        #   Player may choose any available board to play on if current is finished
                        availableBoards = self.getAvailableMoves(10)
                        choice = random.randint(0, availableBoards.__len__() - 1)
                        # for availableBoard in availableBoards:
                        # Potential function to determine optimal board, else just choose first available
                        return self.convenient_indexer[availableBoards[choice][0]][availableBoards[choice][1]]
                    else:
                        return board_num

    '''
    def getAllAvailableMoves(self):
        # =============================================================================
        #         looks for all available moves in the full board
        # =============================================================================
        allAvailableMoves = []
        for i in range(len(self.fullBoard)):
            for j in range(len(self.fullBoard[i])):
                for k in range(len(self.fullBoard[j])):
                    for l in range(len(self.fullBoard[k])):
                        if (self.fullBoard[i][j][k][l]) == EMPTY_VAL:
                            allAvailableMoves.append([i, j, k, l])
        return allAvailableMoves
    '''
    # havent upgraded this function
    def addToHistory(self, fullBoard):
        self.fullBoardHistory.append(fullBoard)

    # havent upgraded this function
    def printHistory(self):
        print(self.fullBoardHistory)

    def move(self, position, player, board_restriction):
        self.fullBoard[board_restriction - 1][position[0]][position[1]] = player
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
                        self.macroBoard[x][y] = 2
                        self.addToHistory(copy.deepcopy(self.fullBoard))



    '''
    def miniMove(self, position, player, restriction):
        # =============================================================================
        #         move function in the full board
        #        restrictions come in the form of a list with two elements (0,0), which tells you
        #        which mini board you can play on and are determined by opponents previous
        #        play. Example opponent plays top left corner, restriction is (0,0) for
        #        miniBoard1, or they play top right corner, restriction is (0,2) for
        #        miniBoard3
        #
        #        this function records moves on the full board and the correct miniboard
        #        it also checks to see if a move leads to a corresponding win of a miniboard
        #        which is then recorded on the macroboard
        # =============================================================================
        allAvailableMoves = self.getAllAvailableMoves()
        if restriction[0] == 0:
            if restriction[1] == 0:
                if self.getMiniGameResult(self.miniBoard1) != GAME_STATE_NOT_ENDED:
                    restriction = None
            if restriction[1] == 1:
                if self.getMiniGameResult(self.miniBoard2) != GAME_STATE_NOT_ENDED:
                    restriction = None
            if restriction[1] == 2:
                if self.getMiniGameResult(self.miniBoard3) != GAME_STATE_NOT_ENDED:
                    restriction = None
        if restriction[0] == 1:
            if restriction[1] == 0:
                if self.getMiniGameResult(self.miniBoard4) != GAME_STATE_NOT_ENDED:
                    restriction = None
            if restriction[1] == 1:
                if self.getMiniGameResult(self.miniBoard5) != GAME_STATE_NOT_ENDED:
                    restriction = None
            if restriction[1] == 2:
                if self.getMiniGameResult(self.miniBoard6) != GAME_STATE_NOT_ENDED:
                    restriction = None
        if restriction[0] == 2:
            if restriction[1] == 0:
                if self.getMiniGameResult(self.miniBoard7) != GAME_STATE_NOT_ENDED:
                    restriction = None
            if restriction[1] == 1:
                if self.getMiniGameResult(self.miniBoard8) != GAME_STATE_NOT_ENDED:
                    restriction = None
            if restriction[1] == 2:
                if self.getMiniGameResult(self.miniBoard9) != GAME_STATE_NOT_ENDED:
                    restriction = None

        for i in range(len(allAvailableMoves)):
            if restriction != None:
                if position[0] == allAvailableMoves[i][0] == restriction[0] and position[1] == allAvailableMoves[i][
                    1] == restriction[1] and position[2] == allAvailableMoves[i][2] and position[3] == \
                        allAvailableMoves[i][3]:
                    self.fullBoard[position[0]][position[1]][position[2]][position[3]] = player
                    if restriction[0] == 0:
                        if restriction[1] == 0:
                            self.miniBoard1[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard1) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard1)
                        if restriction[1] == 1:
                            self.miniBoard2[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard2) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard2)
                        if restriction[1] == 2:
                            self.miniBoard3[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard3) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard3)
                    if restriction[0] == 1:
                        if restriction[1] == 0:
                            self.miniBoard4[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard4) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard4)
                        if restriction[1] == 1:
                            self.miniBoard5[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard5) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard5)
                        if restriction[1] == 2:
                            self.miniBoard6[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard6) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard6)
                    if restriction[0] == 2:
                        if restriction[1] == 0:
                            self.miniBoard7[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard7) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard7)
                        if restriction[1] == 1:
                            self.miniBoard8[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard8) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard8)
                        if restriction[1] == 2:
                            self.miniBoard9[position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard9) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard9)
            else:
                if position[0] == allAvailableMoves[i][0] and position[1] == allAvailableMoves[i][1] and position[2] == \
                        allAvailableMoves[i][2] and position[3] == allAvailableMoves[i][3]:
                    self.fullBoard[position[0]][position[1]][position[2]][position[3]] = player
                    if restriction[0] == 0:
                        if restriction[1] == 0:
                            self.miniBoard1[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard1) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard1)
                        if restriction[1] == 1:
                            self.miniBoard2[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard2) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard2)
                        if restriction[1] == 2:
                            self.miniBoard3[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard3) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard3)
                    if restriction[0] == 1:
                        if restriction[1] == 0:
                            self.miniBoard4[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard4) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard4)
                        if restriction[1] == 1:
                            self.miniBoard5[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard5) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard5)
                        if restriction[1] == 2:
                            self.miniBoard6[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard6) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard6)
                    if restriction[0] == 2:
                        if restriction[1] == 0:
                            self.miniBoard7[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard7) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard7)
                        if restriction[1] == 1:
                            self.miniBoard8[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard8) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard8)
                        if restriction[1] == 2:
                            self.miniBoard9[position[0]][position[1]][position[2]][position[3]] = player
                            if self.getMiniGameState(self.miniBoard9) in [GAME_STATE_X, GAME_STATE_O, GAME_STATE_DRAW]:
                                self.macroBoard[position[0]][position[1]] = self.miniGameState(self.miniBoard9)
                self.addToHistory(copy.deepcopy(self.fullBoard))
    '''
    def simulate(self, playerToMove):
        # =============================================================================
        #         simulates game with players moving randomly, using macro board
        # =============================================================================
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            availableMoves = self.getAvailableMoves()
            selectedMove = availableMoves[random.randrange(0, len(availableMoves))]
            self.move(selectedMove, playerToMove)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
        # Get the history and build the training set
        for historyItem in self.macroBoardHistory:
            self.trainingHistory.append((self.getGameResult(), copy.deepcopy(historyItem)))

    def fullSimulate(self, playerToMove):
        # =============================================================================
        #         simulates game with players moving randomly, using full ultimate board
        # =============================================================================
        board_num = 1
        done = "Not Done"
        winner = None
        while (done == "Not Done"):
            board_num = self.confirmBoard(board_num)
            allAvailableMoves = self.getAvailableMoves(board_num)
            selectedMove = allAvailableMoves[random.randrange(0, len(allAvailableMoves))]
            self.move(selectedMove, playerToMove, board_num)
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
        #         simulates game with players moving from learning experience, using full ultimate board
        # =============================================================================
        playerToMove = PLAYER_X_VAL
        state = "Not Done"
        board_index = 1
        while (state == "Not Done"):
            board_index = self.confirmBoard(board_index)
            allAvailableMoves = self.getAvailableMoves(board_index)
            if playerToMove == nnPlayer:
                maxValue = 0
                bestMove = allAvailableMoves[0]
                for availableMove in allAvailableMoves:
                    # get a copy of a board
                    boardCopy = copy.deepcopy(self.fullBoard)
                    boardCopy[board_index-1][availableMove[0]][availableMove[1]] = nnPlayer
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
            self.move(selectedMove, playerToMove, board_index)
            board_index = self.convenient_indexer[selectedMove[0]][selectedMove[1]]
            winner, state = self.check_current_state(10)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
                
    def getRowAndColumn(self, block_number):
        block_choice = 'invalid'
        while block_choice == 'invalid':
            if block_number in [1,2,3,4,5,6,7,8,9]:
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
        return row,column
    def chooseBoard(self):
        board_choice = 'invalid'
        while board_choice == 'invalid':
            board_index = int(input('Choose a board index 1-9: '))
            if board_index in [1,2,3,4,5,6,7,8,9]:
                board_choice = 'valid'
            else:
                board_index = int(input('Please a valid board index 1-9: '))
        return board_index
    def personVsAIgame(self, nnPlayer, model):
        # =============================================================================
        #         real human can play a game against the AI, using full ultimate board
        # =============================================================================
        playerToMove = PLAYER_X_VAL
        state = "Not Done"
        board_index = self.chooseBoard()
        while (state == "Not Done"):
            board_index = self.confirmBoard(board_index)
            allAvailableMoves = self.getAvailableMoves(board_index)
            if playerToMove == nnPlayer:
                maxValue = 0
                bestMove = allAvailableMoves[0]
                for availableMove in allAvailableMoves:
                    # get a copy of a board
                    boardCopy = copy.deepcopy(self.fullBoard)
                    boardCopy[board_index-1][availableMove[0]][availableMove[1]] = nnPlayer
                    if nnPlayer == PLAYER_X_VAL:
                        value = model.predict(boardCopy, 0)
                    else:
                        value = model.predict(boardCopy, 2)
                    if value > maxValue:
                        maxValue = value
                        bestMove = availableMove
                selectedMove = bestMove
                self.printBoard()
                print("NN playing best move: {}".format(selectedMove))
            else:
                print("Puny human dares to play against the mighty AI!")
#                self.printBoard()
                print('You must play on board {}'.format(board_index))
                moveValidity = 'invalid'
                while moveValidity == 'invalid':
                    selectedRow, selectedColumn = self.getRowAndColumn(int(input('Please choose an empty block to play in: ')))
                    selectedMove = [selectedRow,selectedColumn]
                    if selectedMove in allAvailableMoves:
                        moveValidity = 'valid'
                    else:
                        print('Your move choice was invalid, please choose again.')
                print("Human playing move: {}".format(selectedMove))
            self.printBoard()
            self.move(selectedMove, playerToMove, board_index)
            self.printBoard()
            board_index = self.convenient_indexer[selectedMove[0]][selectedMove[1]]
            winner, state = self.check_current_state(10)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
    #    skipped this function
    def getTrainingHistory(self):
        return self.trainingHistory

    def simulateManyGames(self, playerToMove, numberOfGames):
        # =============================================================================
        #         simulates many games with only random players and just macro board
        # =============================================================================
        playerXWins = 0
        playerOWins = 0
        draws = 0
        for i in range(numberOfGames):
            self.resetBoard()
            self.simulate(playerToMove)
            if self.getGameResult() == PLAYER_X_VAL:
                playerXWins = playerXWins + 1
            elif self.getGameResult() == PLAYER_O_VAL:
                playerOWins = playerOWins + 1
            else:
                draws = draws + 1
        totalWins = playerXWins + playerOWins + draws
        print('X Wins: ' + str(int(playerXWins * 100 / totalWins)) + '%')
        print('O Wins: ' + str(int(playerOWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')

    def fullSimulateManyGames(self, playerToMove, numberOfGames):
        # =============================================================================
        #         simulates many games with only random players and the full board
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
            else:
                draws = draws + 1
        totalWins = playerXWins + playerOWins + draws
        print('X Wins: ' + str(int(playerXWins * 100 / totalWins)) + '%')
        print('O Wins: ' + str(int(playerOWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')
        print("Full sim complete")


    def simulateManyNeuralNetworkGames(self, nnPlayer, numberOfGames, model):
        # =============================================================================
        #         simulates many games with only random players and the full board
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
        while person != 'No':
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
    game.fullSimulateManyGames(1, 100)
    ticTacToeModel = TicTacToeModel(9, 3, 100, 32)
    ticTacToeModel.train(game.getTrainingHistory())
    print("Simulating with Neural Network as X Player:")
    game.simulateManyNeuralNetworkGames(PLAYER_X_VAL, 100, ticTacToeModel)
    print("Simulating with Neural Network as O Player:")
    game.simulateManyNeuralNetworkGames(PLAYER_O_VAL, 100, ticTacToeModel)
    game.simulatePvCgame(PLAYER_O_VAL, ticTacToeModel)
