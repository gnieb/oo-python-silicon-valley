from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:
    
    all = []
    
    def __init__(self, name, number,):
        self.name = name
        self.total_worth = number
        VentureCapitalist.all.append(self)
   
    @classmethod
    def tres_commas_club(cls):
        return [v for v in cls.all if v.total_worth > 1000000000 ]
