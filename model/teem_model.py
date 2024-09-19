from dataclasses import dataclass

@dataclass
class Teem:
   name : str
   # :C, PF, SF, SG, PG
   player_1 : int
   player_2 : int
   player_3 : int
   player_4 : int
   player_5 : int

   id: int = None