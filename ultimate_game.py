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
                          [self.miniBoard7,self.miniBoard8,self.miniBoard9],]
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.boardHistory = []
#havent upgraded this function
    def printBoard(self):
        print(VERTICAL_SEPARATOR)
        for i in range(len(self.board)):
            print(' ', end='')
            for j in range(len(self.board[i])):
                if PLAYER_X_VAL == self.board[i][j]:
                    print(PLAYER_X, end='')
                elif PLAYER_O_VAL == self.board[i][j]:
                    print(PLAYER_O, end='')
                elif EMPTY_VAL == self.board[i][j]:
                    print(EMPTY, end='')
                print(HORIZONTAL_SEPARATOR, end='')
            print(os.linesep)
            print(VERTICAL_SEPARATOR)

    def getGameResult(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == EMPTY_VAL:
                    return GAME_STATE_NOT_ENDED

        # Rows
        for i in range(len(self.board)):
            candidate = self.board[i][0]
            for j in range(len(self.board[i])):
                if candidate != self.board[i][j]:
                    candidate = 0
            if candidate != 0:
                return candidate

        # Columns
        for i in range(len(self.board)):
            candidate = self.board[0][i]
            for j in range(len(self.board[i])):
                if candidate != self.board[j][i]:
                    candidate = 0
            if candidate != 0:
                return candidate

        # First diagonal
        candidate = self.board[0][0]
        for i in range(len(self.board)):
            if candidate != self.board[i][i]:
                candidate = 0
        if candidate != 0:
            return candidate

        # Second diagonal
        candidate = self.board[0][2]
        for i in range(len(self.board)):
            if candidate != self.board[i][len(self.board[i]) - i - 1]:
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
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j]) == EMPTY_VAL:
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
                    if (self.fullBoard[i][j][k]) == EMPTY_VAL:
                        allAvailableMoves.append([i, j, k])
        return allAvailableMoves
#havent upgraded this function
    def addToHistory(self, board):
        self.boardHistory.append(board)
#havent upgraded this function
    def printHistory(self):
        print(self.boardHistory)

    def move(self, position, player):
        availableMoves = self.getAvailableMoves()
        for i in range(len(availableMoves)):
            if position[0] == availableMoves[i][0] and position[1] == availableMoves[i][1]:
                self.board[position[0]][position[1]] = player
                self.addToHistory(copy.deepcopy(self.board))
    
    def miniMove(self, position, player):
# =============================================================================
#         move function in the full board
#        still working on this one
# =============================================================================
        allAvailableMoves = self.getAllAvailableMoves()
        for i in range(len(allAvailableMoves)):
            if position[0] == allAvailableMoves[i][0] and position[1] == allAvailableMoves[i][1]:
                self.board[position[0]][position[1]] = player
                self.addToHistory(copy.deepcopy(self.board))

    def simulate(self, playerToMove):
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            availableMoves = self.getAvailableMoves()
            selectedMove = availableMoves[random.randrange(0, len(availableMoves))]
            self.move(selectedMove, playerToMove)
            if playerToMove == PLAYER_X_VAL:
                playerToMove = PLAYER_O_VAL
            else:
                playerToMove = PLAYER_X_VAL
        # Get the history and build the training set
        for historyItem in self.boardHistory:
            self.trainingHistory.append((self.getGameResult(), copy.deepcopy(historyItem)))

    def simulateNeuralNetwork(self, nnPlayer, model):
        playerToMove = PLAYER_X_VAL
        while (self.getGameResult() == GAME_STATE_NOT_ENDED):
            availableMoves = self.getAvailableMoves()
            if playerToMove == nnPlayer:
                maxValue = 0
                bestMove = availableMoves[0]
                for availableMove in availableMoves:
                    # get a copy of a board
                    boardCopy = copy.deepcopy(self.board)
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

    def getTrainingHistory(self):
        return self.trainingHistory

    def simulateManyGames(self, playerToMove, numberOfGames):
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


    def simulateManyNeuralNetworkGames(self, nnPlayer, numberOfGames, model):
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

if __name__ == "__main__":
    game = Game()
    game.simulateManyGames(1, 10000)
    ticTacToeModel = TicTacToeModel(9, 3, 100, 32)
    ticTacToeModel.train(game.getTrainingHistory())
    print ("Simulating with Neural Network as X Player:")
    game.simulateManyNeuralNetworkGames(PLAYER_X_VAL, 10000, ticTacToeModel)
    print("Simulating with Neural Network as O Player:")
    game.simulateManyNeuralNetworkGames(PLAYER_O_VAL, 10000, ticTacToeModel)