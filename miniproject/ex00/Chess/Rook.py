from .Abs_Piece import Piece

class Rook(Piece):

    def move_check(self, board_size:list, King: object,  otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""

        #* ขึ้นลง
        for i in range(1, max(board_size)):
            if King.y == self.y+i and King.x == self.x:
                return self._path_clear(King, otherPiece)
            if King.y == self.y-i and King.x == self.x:
                return self._path_clear(King, otherPiece)

        for i in range(1, max(board_size)):

            #* ซ้ายขวา
            if King.x == self.x+i and King.y == self.y:
                return self._path_clear(King, otherPiece)
            if King.x == self.x-i and King.y == self.y:
                return self._path_clear(King, otherPiece)
        
        return False
