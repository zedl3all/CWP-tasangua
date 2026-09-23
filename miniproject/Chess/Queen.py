from .Abs_Piece import Piece

class Queen(Piece):

    def move_check(self, board_size:list, King: object) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        #* รูป + เหมือน Rook
        if King.x == self.x or King.y == self.y:
            return True
        
        for i in range(1, (board_size[0]-self.x)):

            #* 0,0 อยู่ซ้ายบน
            #* ทแยงซ้ายล่าง i=x+1, j=y-1 x=ตำแหน่งใดๆ
            if King.x == self.x+i and King.y == self.y-i:
                # print("Pos Q", self.x+i, self.y-i)
                return True
            
            #* ทแยงขวาบน i=x-1, j=y+1 x=ตำแหน่งใดๆ
            if King.x == self.x-i and King.y == self.y+i:
                return True

            #* ทแยงขวาล่าง i=x+1, j=y+1 x=ตำแหน่งใดๆ
            if King.x == self.x+i and King.y == self.y+i:
                return True

            #* ทแยงซ้ายบน i=x-1, j=y-1 x=ตำแหน่งใดๆ
            if King.x == self.x-i and King.y == self.y-i:
                return True

        return False