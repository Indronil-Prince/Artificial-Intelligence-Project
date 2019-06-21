import copy

def numOfValue(board, value):
    return board.count(value)

def InvertedBoard(board):
    invertedboard = []
    for i in board:
        if i == "1":
            invertedboard.append("2")
        elif i == "2":
            invertedboard.append("1")
        else:
            invertedboard.append("X")
    return invertedboard

def generateInvertedBoardList(pos_list):
    '''
    '''
    result = []
    for i in pos_list:
        result.append(InvertedBoard(i))
    return result