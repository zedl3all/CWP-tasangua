from .Abs_Piece import Piece

class Bishop(Piece):

    def move_check(self, board_size:list, King: object, otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        
        for i in otherPiece.values():
            other_position = i[0]
            
            #* กันชนทแยง
            if min(King.y, self.y) < other_position[1] < max(King.y, self.y):
                if min(King.x, self.x) < other_position[0] < max(King.x, self.x):
                    return False
        
        
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
