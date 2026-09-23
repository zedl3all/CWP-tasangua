import re
from Chess.Rook import Rook

def Convert2List(board: str) -> list:
    """Convert Str board to List"""
    output = list()
    temp = list()

    for i in board:
        if i != "\n":
            temp.append(i)
        else:
            output.append(temp)
            temp = list()

    return output

def CheckKing(board: str) -> bool:
    """Check King Is 0 or more than 1"""

    if len(re.findall("k", board, re.IGNORECASE)) != 1:
        return False

    return True

def CheckBoardSize(board: list) -> bool:
    """Check BoardSize is Valid?"""
    size = None
    for i in board:
        if size is None:
            size = len(i)

        if (len(i) != size):
            return False

    return True

def Find_Position(board: list) -> dict:
    """Find Position of Piece"""

    Output = dict()
    for index, value in enumerate(board):
        for i,j in enumerate(value):
            if j != ".":
                #? หากหมากมีอยู่แล้วใน dict ก็จะ append list เข้าไปเพิ่ม
                #? หากไม่เคยมีก็สร้างแล้วใส่ค่า
                Output.setdefault(j, []).append([index, i])

    return Output

def checkmate(StrBoard: str):

    ListBoard = Convert2List(StrBoard)

    if not(CheckBoardSize(ListBoard)):
        print("Error")
        return
    
    if not(CheckKing(StrBoard)):
        print("Error")
        return

    Position = Find_Position(ListBoard)

    pass

board = """\
R...
.K..
..P.
....\
"""

new_board = Convert2List(board)

Find_Position(new_board)