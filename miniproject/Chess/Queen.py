from .Abs_Piece import Piece

class Queen(Piece):

    def move_check(self, target_x: int, target_y: int, board: list) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
