from dataclasses import dataclass 
import sys

@dataclass
class Integration:
   pass

@dataclass
class TranceFunction:
   num: list
   den: list
   def __post_init__(self):
      if len(self.num) > len(self.den):
         sys.exit("Полином не реализуем, степень числителя больше знаменателя")

@dataclass
class lpfunction:
   deg: int
   Tt: float
   def __post_init__(self):
      if not isinstance(self.deg, int) or self.Tt <= 0:
         sys.exit("lpf: deg - не целое число или T меньше или равно нулю")
      if self.deg < 1:
         sys.exit("deg меньше единицы или deg = 1 => Пропорциональное звено")