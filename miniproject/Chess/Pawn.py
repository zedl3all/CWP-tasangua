from .Abs_Piece import Piece

class Pawn(Piece):

    def move_check(self, board_size:list, King: object) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        next_row = self.x - 1
        left_column = self.y - 1
        right_column = self.y + 1

        if King.x == next_row: 
            if King.y == left_column:
                return True

            if King.y == right_column:
                return True

        return False
