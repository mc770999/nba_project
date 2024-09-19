from dataclasses import dataclass

@dataclass
class Teem:
   name : str
   # :C, PF, SF, SG, PG
   position_C : int
   position_SF : int
   position_PF : int
   position_SG : int
   position_PG : int

   id: int = None