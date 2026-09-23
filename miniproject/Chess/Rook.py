from .Abs_Piece import Piece

class Rook(Piece):

    def move_check(self, board_size:list, King: object,  otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        
        for i in otherPiece.values():
            other_position = i[0]
            
            #* กันชนแนวตั้ง
            if other_position[0] == King.x:
                if min(King.y, self.y) < other_position[1] < max(King.y, self.y):
                    return False
            #* กันชนแนวนอน
            if other_position[1] == King.y:
                if min(King.x, self.x) < other_position[0] < max(King.x, self.x):
                    return False
            
        
        #* ขึ้นลง
        for i in range(1, max(board_size)):
            if King.y == self.y+i and King.x == self.x:
                return True
            if King.y == self.y-i and King.x == self.x:
                return True

        for i in range(1, max(board_size)):

            #* ซ้ายขวา
            if King.x == self.x+i and King.y == self.y:
                return True
            if King.x == self.x-i and King.y == self.y:
                return True
        
        return False