class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []
        self.moveFunctions = {"p":self.getPawnMoves,"R":self.getRookMoves,"N":self.getKnightMoves,"B":self.getBishopMoves,"Q":self.getQueenMoves,"K":self.getKingMoves}

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #switching turns (white to black)
    def getValidMoves(self):
        return self.getAllPossibleMoves()
    def getAllPossibleMoves(self):
        moves = [Move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn =='w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r,c,moves)
        return moves
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            if self.board[r-1][c]=="--":
                moves.append(Move((r,c),(r-1,c),self.board))
                if r == 6 and self.board[r-2][c]=="--":
                    moves.append(Move((r,c),(r-2,c),self.board))
            if c-1>=0:
                if self.board[r-1][c-1][0]=="b":
                    moves.append(Move((r,c),(r-1,c-1),self.board))
            if c+1<=7:
                if self.board[r-1][c+1][0]=="b":
                    moves.append(Move((r,c),(r-1,c+1),self.board))
        else:
            if self.board[r+1][c]=="--":
                moves.append(Move((r,c),(r+1,c),self.board))
                if r == 1 and self.board[r+2][c]=="--":
                    moves.append(Move((r,c),(r+2,c),self.board))
            if c-1>=0:
                if self.board[r+1][c-1][0]=="w":
                    moves.append(Move((r,c),(r+1,c-1),self.board))
            if c+1<=7:
                if self.board[r+1][c+1][0]=="w":
                    moves.append(Move((r,c),(r+1,c+1),self.board))
    def getRookMoves(self, r, c, moves):
        blockedN = False
        blockedE = False
        blockedS = False
        blockedW = False
        if self.whiteToMove:
            for i in range(1,8):
                if not (c+i>=7 or blockedE):
                    if self.board[r][c+i]=="--":
                        moves.append(Move((r,c),(r,c+i),self.board))
                    elif self.board[r][c+i][0]=="b":
                        moves.append(Move((r,c),(r,c+i),self.board))
                        blockedE = True
                    else:
                        blockedE = True
                if not(c-i<=0 or blockedW):
                    if self.board[r][c-i]=="--":
                        moves.append(Move((r,c),(r,c-i),self.board))
                    elif self.board[r][c-i][0]=="b":
                        moves.append(Move((r,c),(r,c-i),self.board))
                        blockedW = True
                    else:
                        blockedW = True
                if not(r+i>=7 or blockedS):
                    if self.board[r+i][c]=="--":
                        moves.append(Move((r,c),(r+i,c),self.board))
                    elif self.board[r+i][c][0]=="b":
                        moves.append(Move((r,c),(r+i,c),self.board))
                        blockedS = True
                    else:
                        blockedS = True
                if not(r-i<=0 or blockedN):
                    if self.board[r-i][c]=="--":
                        moves.append(Move((r,c),(r-i,c),self.board))
                    elif self.board[r-i][c][0]=="b":
                        moves.append(Move((r,c),(r-i,c),self.board))
                        blockedN = True
                    else:
                        blockedN = True
        else:
            for i in range(1,8):
                if not (c+i>=7 or blockedE):
                    if self.board[r][c+i]=="--":
                        moves.append(Move((r,c),(r,c+i),self.board))
                    elif self.board[r][c+i][0]=="w":
                        moves.append(Move((r,c),(r,c+i),self.board))
                        blockedE = True
                    else:
                        blockedE = True
                if not(c-i<=0 or blockedW):
                    if self.board[r][c-i]=="--":
                        moves.append(Move((r,c),(r,c-i),self.board))
                    elif self.board[r][c-i][0]=="w":
                        moves.append(Move((r,c),(r,c-i),self.board))
                        blockedW = True
                    else:
                        blockedW = True
                if not(r+i>=7 or blockedS):
                    if self.board[r+i][c]=="--":
                        moves.append(Move((r,c),(r+i,c),self.board))
                    elif self.board[r+i][c][0]=="w":
                        moves.append(Move((r,c),(r+i,c),self.board))
                        blockedS = True
                    else:
                        blockedS = True
                if not(r-i<=0 or blockedN):
                    if self.board[r-i][c]=="--":
                        moves.append(Move((r,c),(r-i,c),self.board))
                    elif self.board[r-i][c][0]=="w":
                        moves.append(Move((r,c),(r-i,c),self.board))
                        blockedN = True
                    else:
                        blockedN = True


    def getKnightMoves(self,r,c,moves):
        movelist = [(r-2,c-1),(r-2,c+1),(r+2,c-1),(r+2,c+1),(r+1,c+2),(r-1,c+2),(r-1,c-2),(r+1,c-2)]
        if self.whiteToMove:
            for move in movelist:
                if 7>=move[0]>=0 and 7>=move[1]>=0 and self.board[move[0]][move[1]][0]!="w":
                    moves.append(Move((r,c),move,self.board))
        else:
            for move in movelist:
                if 7>=move[0]>=0 and 7>=move[1]>=0 and self.board[move[0]][move[1]][0]!="b":
                    moves.append(Move((r,c),move,self.board))
    def getBishopMoves(self,r,c,moves):
        blockedSE = False
        blockedSW = False
        blockedNE = False
        blockedNW = False
        if self.whiteToMove:
            for i in range (1,8):
                if not(c+i>=7 or r + i >= 7) and not blockedSE:
                    if self.board[r+i][c+i]=="--":
                        moves.append(Move((r,c),(r+i,c+i),self.board))
                    elif self.board[r+i][c+i][0]=="b":
                        moves.append(Move((r,c),(r+i,c+i),self.board))
                        blockedSE = True
                    else:
                        blockedSE = True
                if not(c-i<=0 or r - i <= 0) and not blockedNW:
                    if self.board[r-i][c-i]=="--":
                        moves.append(Move((r,c),(r-i,c-i),self.board))
                    elif self.board[r-i][c-i][0]=="b":
                        moves.append(Move((r,c),(r-i,c-i),self.board))
                        blockedNW = True
                    else:
                        blockedNW = True
                if not(c+i>=7 or r-i<=0) and not blockedNE:
                    if self.board[r-i][c+i]=="--":
                        moves.append(Move((r,c),(r-i,c+i),self.board))
                    elif self.board[r-i][c+i][0]=="b":
                        moves.append(Move((r,c),(r-i,c+i),self.board))
                        blockedNE = True
                    else:
                        blockedNE = True
                if not(c-i<=0 or r+i>=7)and not blockedSW:
                    if self.board[r+i][c-i]=="--":
                        moves.append(Move((r,c),(r+i,c-i),self.board))
                    elif self.board[r+i][c-i][0]=="b":
                        moves.append(Move((r,c),(r+i,c-i),self.board))
                        blockedSW = True
                    else:
                        blockedSW = True
        else:
            for i in range (1,8):
                if not(c+i>=7 or r + i >= 7) and not blockedSE:
                    if self.board[r+i][c+i]=="--":
                        moves.append(Move((r,c),(r+i,c+i),self.board))
                    elif self.board[r+i][c+i][0]=="w":
                        moves.append(Move((r,c),(r+i,c+i),self.board))
                        blockedSE = True
                    else:
                        blockedSE = True
                if not(c-i<=0 or r - i <= 0) and not blockedNW:
                    if self.board[r-i][c-i]=="--":
                        moves.append(Move((r,c),(r-i,c-i),self.board))
                    elif self.board[r-i][c-i][0]=="w":
                        moves.append(Move((r,c),(r-i,c-i),self.board))
                        blockedNW = True
                    else:
                        blockedNW = True
                if not(c+i>=7 or r-i<=0) and not blockedNE:
                    if self.board[r-i][c+i]=="--":
                        moves.append(Move((r,c),(r-i,c+i),self.board))
                    elif self.board[r-i][c+i][0]=="w":
                        moves.append(Move((r,c),(r-i,c+i),self.board))
                        blockedNE = True
                    else:
                        blockedNE = True
                if not(c-i<=0 or r+i>=7)and not blockedSW:
                    if self.board[r+i][c-i]=="--":
                        moves.append(Move((r,c),(r+i,c-i),self.board))
                    elif self.board[r+i][c-i][0]=="w":
                        moves.append(Move((r,c),(r+i,c-i),self.board))
                        blockedSW = True
                    else:
                        blockedSW = True

    def getQueenMoves(self,r,c,moves):
        self.getBishopMoves(r,c,moves) # there might be a bug in the rook movement, I wasn't able to recreate it tho. i was able to capture my on piece as white capturing up -Archie
        self.getRookMoves(r,c,moves)
    def getKingMoves(self,r,c,moves):
        if self.whiteToMove:
            for i in range(-1,2):
                for j in range(-1,2):
                    if 7>=r+i>=0 and 7>=c+j>=0 and self.board[r+i][c+j][0]!="w":
                        moves.append(Move((r,c),(r+i,c+j),self.board))
        else:
            for i in range(-1,2):
                for j in range(-1,2):
                    if 7>=r+i>=0 and 7>=c+j>=0 and self.board[r+i][c+j][0]!="b":
                        moves.append(Move((r,c),(r+i,c+j),self.board))
                    

class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)
    
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]