import re

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

def checkmate(board: str):
    pass

board = """\
R...
.K..
..P.
....\
"""

new_board = Convert2List(board)

print(CheckKing(board))