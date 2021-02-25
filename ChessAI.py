import random

pieceScore = {"K":0,"Q":10,"R":5,"B":3,"N":3,"p":1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

def findRandomMove(validMoves):
    return random.choice(validMoves)

# def findBestMove(gs, validMoves):
#     turnMultiplier = 1 if gs.whiteToMove else -1
#     opponentMinMaxScore = CHECKMATE
#     bestPlayerMove = None
#     random.shuffle(validMoves)
#     for playerMove in validMoves:
#         gs.makeMove(playerMove)
#         opponentsMoves = gs.getValidMoves()
#         if gs.stalemate:
#             opponentsMoves = STALEMATE
#         elif gs.checkmate:
#             opponentMaxScore = -CHECKMATE
#         else:
#             opponentMaxScore = -CHECKMATE
#             for opponentsMove in opponentsMoves:
#                 gs.makeMove(opponentsMove)
#                 gs.getValidMoves()
#                 if gs.checkmate:
#                     score = CHECKMATE
#                 elif gs.stalemate:
#                     score = STALEMATE
#                 else: 
#                     score = -turnMultiplier * scoreMaterial(gs.board)
#                 if score > opponentMaxScore:
#                     opponentMaxScore = score
#                 gs.undoMove()    
#             if opponentMaxScore < opponentMinMaxScore:
#                 opponentMinMaxScore = opponentMaxScore
#                 bestPlayerMove = playerMove
#             gs.undoMove()
#     return bestPlayerMove

# helper method
def findBestMoveMinMax(gs, validMoves):
    global nextMove
    nextMove = None
    findMoveMinMax(gs, validMoves, DEPTH, gs.whiteToMove)
    return nextMove

def findMoveMinMax(gs, validMoves, depth, whiteToMove):
    global nextMove
    if depth == 0:
        return scoreMaterial(gs.board)

    if whiteToMove:
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth - 1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return maxScore
    else:
        minScore = CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getValidMoves()
            score = findMoveMinMax(gs, nextMoves, depth - 1, True)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minScore        
                
# positive score is good for white, negative score is good for black
def scoreBoard(gs):
    if gs.checkmate:
        if gs.whiteToMove:
            return -CHECKMATE #black wins
        else:
            return CHECKMATE #white wins
    elif gs.stalemate:
        return STALEMATE


    score = 0
    for row in gs.board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]] 
    return score                   







# Score based on material

def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]] 
    return score                   
