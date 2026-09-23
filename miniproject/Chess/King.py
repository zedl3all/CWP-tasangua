from .Abs_Piece import Piece

class King(Piece):

    def move_check(self, board_size:list, King: object, otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
