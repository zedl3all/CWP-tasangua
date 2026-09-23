from .Abs_Piece import Piece

class Bishop(Piece):

    def move_check(self, board_size:list, King: object) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        for i in range(1, max(board_size)):
            # ทแยงซ้ายบน
            if King.x == self.x - i and King.y == self.y - i:
                return True

            # ทแยงขวาบน
            if King.x == self.x - i and King.y == self.y + i:
                return True

            # ทแยงซ้ายล่าง
            if King.x == self.x + i and King.y == self.y - i:
                return True

            # ทแยงขวาล่าง
            if King.x == self.x + i and King.y == self.y + i:
                return True

        return False
