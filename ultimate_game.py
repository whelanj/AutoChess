# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:05:34 2020

@author: jwhel
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


class Game:

    def __init__(self):
        self.resetBoard()
        self.trainingHistory = []

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
        self.fullBoard = [[self.miniBoard1,self.miniBoard2,self.miniBoard3],
                          [self.miniBoard4,self.miniBoard5,self.miniBoard6],
                          [self.miniBoard7,self.miniBoard8,self.miniBoard9]]
        self.macroBoard = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.macroBoardHistory = []
#havent upgraded this function
    def printBoard(self):
        print(VERTICAL_SEPARATOR)
        for i in range(len(self.macroBoard)):
            print(' ', end='')
            for j in range(len(self.macroBoard[i])):
                if PLAYER_X_VAL == self.macroBoard[i][j]:
                    print(PLAYER_X, end='')
                elif PLAYER_O_VAL == self.macroBoard[i][j]:
                    print(PLAYER_O, end='')
                elif EMPTY_VAL == self.macroBoard[i][j]:
                    print(EMPTY, end='')
                print(HORIZONTAL_SEPARATOR, end='')
            print(os.linesep)
            print(VERTICAL_SEPARATOR)

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
    
    def getAvailableMoves(self):
# =============================================================================
#         only looks at the macro board
# =============================================================================
        availableMoves = []
        for i in range(len(self.macroBoard)):
            for j in range(len(self.macroBoard[i])):
                if (self.macroBoard[i][j]) == EMPTY_VAL:
                    availableMoves.append([i, j])
        return availableMoves
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
#havent upgraded this function
    def addToHistory(self, board):
        self.macroBoardHistory.append(board)
#havent upgraded this function
    def printHistory(self):
        print(self.macroBoardHistory)

    def move(self, position, player):
        availableMoves = self.getAvailableMoves()
        for i in range(len(availableMoves)):
            if position[0] == availableMoves[i][0] and position[1] == availableMoves[i][1]:
                self.macroBoard[position[0]][position[1]] = player
                self.addToHistory(copy.deepcopy(self.macroBoard))
    
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
                if position[0] == allAvailableMoves[i][0] == restriction[0] and position[1] == allAvailableMoves[i][1] == restriction[1] and position[2] == allAvailableMoves[i][2] and position[3] == allAvailableMoves[i][3]:
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
                if position[0] == allAvailableMoves[i][0] and position[1] == allAvailableMoves[i][1] and position[2] == allAvailableMoves[i][2] and position[3] == allAvailableMoves[i][3]:
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
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            allAvailableMoves = self.getAllAvailableMoves()
            selectedMove = allAvailableMoves[random.randrange(0, len(allAvailableMoves))]
            self.move(selectedMove, playerToMove)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
        # Get the history and build the training set
        for historyItem in self.macroBoardHistory:
            self.trainingHistory.append((self.getGameResult(), copy.deepcopy(historyItem)))

    def simulateNeuralNetwork(self, nnPlayer, model):
# =============================================================================
#         simulates game with players moving randomly, using macro board
# =============================================================================
        playerToMove = PLAYER_X_VAL
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            availableMoves = self.getAvailableMoves()
            if playerToMove == nnPlayer:
                maxValue = 0
                bestMove = availableMoves[0]
                for availableMove in availableMoves:
                    # get a copy of a board
                    boardCopy = copy.deepcopy(self.macroBoard)
                    boardCopy[availableMove[0]][availableMove[1]] = nnPlayer
                    if nnPlayer == PLAYER_X_VAL:
                        value = model.predict(boardCopy, 0)
                    else:
                        value = model.predict(boardCopy, 2)
                    if value > maxValue:
                        maxValue = value
                        bestMove = availableMove
                selectedMove = bestMove
            else:
                selectedMove = availableMoves[random.randrange(0, len(availableMoves))]
            self.move(selectedMove, playerToMove)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
    def fullSimulateNeuralNetwork(self, nnPlayer, model):
# =============================================================================
#         simulates game with players moving from learning experience, using full ultimate board
# =============================================================================
        playerToMove = PLAYER_X_VAL
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            allAvailableMoves = self.getAllAvailableMoves()
            if playerToMove == nnPlayer:
                maxValue = 0
                bestMove = allAvailableMoves[0]
                for availableMove in allAvailableMoves:
                    # get a copy of a board
                    boardCopy = copy.deepcopy(self.fullBoard)
                    boardCopy[availableMove[0]][availableMove[1]][availableMove[2]][availableMove[3]] = nnPlayer
                    if nnPlayer == PLAYER_X_VAL:
                        value = model.predict(boardCopy, 0)
                    else:
                        value = model.predict(boardCopy, 2)
                    if value > maxValue:
                        maxValue = value
                        bestMove = availableMove
                selectedMove = bestMove
            else:
                selectedMove = allAvailableMoves[random.randrange(0, len(availableMoves))]
            self.move(selectedMove, playerToMove)
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
            else: draws = draws + 1
        totalWins = playerXWins + playerOWins + draws
        print ('X Wins: ' + str(int(playerXWins * 100/totalWins)) + '%')
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
            else: draws = draws + 1
        totalWins = playerXWins + playerOWins + draws
        print ('X Wins: ' + str(int(playerXWins * 100/totalWins)) + '%')
        print('O Wins: ' + str(int(playerOWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')


    def simulateManyNeuralNetworkGames(self, nnPlayer, numberOfGames, model):
# =============================================================================
#         simulates many games with only random players and just the macro board
# =============================================================================
        nnPlayerWins = 0
        randomPlayerWins = 0
        draws = 0
        print ("NN player")
        print (nnPlayer)
        for i in range(numberOfGames):
            self.resetBoard()
            self.simulateNeuralNetwork(nnPlayer, model)
            if self.getGameResult() == nnPlayer:
                nnPlayerWins = nnPlayerWins + 1
            elif self.getGameResult() == GAME_STATE_DRAW:
                draws = draws + 1
            else: randomPlayerWins = randomPlayerWins + 1
        totalWins = nnPlayerWins + randomPlayerWins + draws
        print ('X Wins: ' + str(int(nnPlayerWins * 100/totalWins)) + '%')
        print('O Wins: ' + str(int(randomPlayerWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')
    def simulateManyNeuralNetworkGames(self, nnPlayer, numberOfGames, model):
# =============================================================================
#         simulates many games with only random players and the full board
# =============================================================================
        nnPlayerWins = 0
        randomPlayerWins = 0
        draws = 0
        print ("NN player")
        print (nnPlayer)
        for i in range(numberOfGames):
            self.resetBoard()
            self.fullSimulateNeuralNetwork(nnPlayer, model)
            if self.getGameResult() == nnPlayer:
                nnPlayerWins = nnPlayerWins + 1
            elif self.getGameResult() == GAME_STATE_DRAW:
                draws = draws + 1
            else: randomPlayerWins = randomPlayerWins + 1
        totalWins = nnPlayerWins + randomPlayerWins + draws
        print ('X Wins: ' + str(int(nnPlayerWins * 100/totalWins)) + '%')
        print('O Wins: ' + str(int(randomPlayerWins * 100 / totalWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totalWins)) + '%')

if __name__ == "__main__":
    game = Game()
    game.fullSimulateManyGames(1, 10000)
    ticTacToeModel = TicTacToeModel(9, 3, 100, 32)
    ticTacToeModel.train(game.getTrainingHistory())
    print ("Simulating with Neural Network as X Player:")
    game.fullSimulateManyNeuralNetworkGames(PLAYER_X_VAL, 10000, ticTacToeModel)
    print("Simulating with Neural Network as O Player:")
    game.fullSimulateManyNeuralNetworkGames(PLAYER_O_VAL, 10000, ticTacToeModel)