from abc import ABC, abstractmethod

class Piece(ABC):
    """Class แม่ของเบี้ย"""
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    @abstractmethod
    def move_check(self, target_x: int, target_y: int, board) -> bool:
        """ตรวจสอบว่าเดินแล้วโดน King ไหม"""
        pass