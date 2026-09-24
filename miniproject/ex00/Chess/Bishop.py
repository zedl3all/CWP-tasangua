from .Abs_Piece import Piece

class Bishop(Piece):

    def move_check(self, board_size:list, King: object, otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""

        for i in range(1, max(board_size)):
            # ทแยงซ้ายบน
            if King.x == self.x - i and King.y == self.y - i:
                return self._path_clear(King, otherPiece)

            # ทแยงขวาบน
            if King.x == self.x - i and King.y == self.y + i:
                return self._path_clear(King, otherPiece)

            # ทแยงซ้ายล่าง
            if King.x == self.x + i and King.y == self.y - i:
                return self._path_clear(King, otherPiece)

            # ทแยงขวาล่าง
            if King.x == self.x + i and King.y == self.y + i:
                return self._path_clear(King, otherPiece)

        return False
