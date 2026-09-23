import re
from Chess import Bishop, King, Pawn, Queen, Rook

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
    output.append(temp)

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
                Output.setdefault(j, []).append([i, index])

    return Output

def CreateObjectFromPosition(Position: dict) -> list:
    """Create Object Piece From Positon"""

    Output = list()

    for key, value in Position.items():
        for pos in value:
            match key:
                case 'R':
                    Output.append(Rook(pos[0],pos[1]))
                case 'P':
                    Output.append(Pawn(pos[0],pos[1]))
                case 'Q':
                    Output.append(Queen(pos[0],pos[1]))
                case 'B':
                    Output.append(Bishop(pos[0],pos[1]))
                case 'K':
                    Output.append(King(pos[0],pos[1]))

    return Output

def checkmate(StrBoard: str):

    ListBoard = Convert2List(StrBoard) #?[['Q', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', 'K']]
    board_size = [len(ListBoard),len(ListBoard[0])] #?[4, 4]

    if not(CheckBoardSize(ListBoard)):
        print("Error")
        return
    
    if not(CheckKing(StrBoard)):
        print("Error")
        return

    Position = Find_Position(ListBoard) #?{'Q': [[0, 0]], 'K': [[3, 3]]}
    Obj_Pos = CreateObjectFromPosition(Position) #?[Obj.Queen, Obj.King]

    king = None

    for i in Obj_Pos:
        if(isinstance(i,King)):
            king = i
            break

    if king:
        Obj_Pos.remove(king)
    else:
        print("Error")
        return

    Output = False

    for piece in Obj_Pos:
        if(piece.move_check(board_size, king, Position)):
            Output=True

    if Output:
        print("Success")
    else:
        print("Fail")
