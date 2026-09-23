from .Abs_Piece import Piece

class Rook(Piece):

    def move_check(self, King: object) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
