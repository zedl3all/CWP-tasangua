from abc import ABC, abstractmethod

class Piece(ABC):
    """Class แม่ของเบี้ย"""
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    @abstractmethod
    def move_check(self, board_size:list, King: object, otherPiece: dict) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""

    def _path_clear(self, King: object, otherPiece: dict) -> bool:
        """ตรวจช่องระหว่างหมากตัวนี้กับ King ว่าไม่มีหมากตัวอื่นขวาง"""
        x_difference = King.x - self.x
        y_difference = King.y - self.y
        if x_difference > 0:
            x_step = 1
        elif x_difference < 0:
            x_step = -1
        else:
            x_step = 0
        
        if y_difference > 0:
            y_step = 1
        elif y_difference < 0:
            y_step = -1
        else:
            y_step = 0

        occupied = set()
        for symbol, positions in otherPiece.items():
            if symbol not in {"P", "B", "R", "Q", "K"}:
                continue
            for position in positions:
                occupied.add((position[0], position[1]))

        distance = max(abs(x_difference), abs(y_difference))
        for step in range(1, distance):
            x = self.x + x_step * step
            y = self.y + y_step * step
            if (x, y) in occupied:
                return False

        return True
