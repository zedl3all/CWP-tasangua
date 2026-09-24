from .Abs_Piece import Piece

class Pawn(Piece):

    def move_check(self, board_size:list, King: object, otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        next_row = self.y - 1
        left_column = self.x - 1
        right_column = self.x + 1

        if King.y == next_row:
            if King.x == left_column:
                return True

            if King.x == right_column:
                return True

        return False
