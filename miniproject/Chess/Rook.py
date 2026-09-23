from .Abs_Piece import Piece

class Rook(Piece):

    def move_check(self, board_size:list, King: object) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        if King.x == self.x or King.y == self.y:
            return True
        return False