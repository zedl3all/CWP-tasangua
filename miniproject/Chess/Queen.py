from .Abs_Piece import Piece

class Queen(Piece):

    def move_check(self, board_size:list, King: object, otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""

        #* ขึ้นลง
        for i in range(1,  max(board_size)):
            if King.y == self.y+i and King.x == self.x:
                return self._path_clear(King, otherPiece)
            if King.y == self.y-i and King.x == self.x:
                return self._path_clear(King, otherPiece)

        for i in range(1,  max(board_size)):
        
            #* ซ้ายขวา
            if King.x == self.x+i and King.y == self.y:
                return self._path_clear(King, otherPiece)
            if King.x == self.x-i and King.y == self.y:
                return self._path_clear(King, otherPiece)

            #* ทแยงซ้ายล่าง i=x+1, j=y-1 x=ตำแหน่งใดๆ
            if King.x == self.x+i and King.y == self.y-i:
                # print("Pos Q", self.x+i, self.y-i)
                return self._path_clear(King, otherPiece)
            
            #* ทแยงขวาบน i=x-1, j=y+1 x=ตำแหน่งใดๆ
            if King.x == self.x-i and King.y == self.y+i:
                return self._path_clear(King, otherPiece)

            #* ทแยงขวาล่าง i=x+1, j=y+1 x=ตำแหน่งใดๆ
            if King.x == self.x+i and King.y == self.y+i:
                return self._path_clear(King, otherPiece)

            #* ทแยงซ้ายบน i=x-1, j=y-1 x=ตำแหน่งใดๆ
            if King.x == self.x-i and King.y == self.y-i:
                return self._path_clear(King, otherPiece)

        return False
