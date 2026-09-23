from .Abs_Piece import Piece

class Rook(Piece):

    def move_check(self, board_size:list, King: object) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        #* ขึ้นลง
        for i in range(1,  max(board_size)):
            if King.y == self.y+i and King.x == self.x:
                return True
            if King.y == i-self.y and King.x == self.x:
                return True

        for i in range(1,  max(board_size)):

            #* ซ้ายขวา
            if King.x == self.x+i and King.y == self.y:
                return True
            if King.x == i-self.x and King.y == self.y:
                return True
        
        return False