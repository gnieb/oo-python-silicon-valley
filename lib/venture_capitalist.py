from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:

    all = []

    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_comma_club(cls):
        return [vc for vc in VentureCapitalist.all if vc.total_worth > 1000000000]
    

    def offer_contract(self, su, type, amount):
        FundingRound(su, self, type, amount)
    
    @property
    def fundingrounds(self):
        return [f for f in FundingRound.all if f._vc == self]
    
    @property
    def portfolio(self):
        return list({f._startup for f in self.fundingrounds})


    @property
    def biggest_investment(self):
        biggest = 0 
        found_fr = ''
        for f in self.fundingrounds:
            if f.invest > biggest:
                biggest = f.invest
                found_fr = f

        return found_fr
    

    def invested(self, domain):
        total = 0
        for f in self.fundingrounds:
            if f._startup._domain == domain:
                total += f.invest
        return total

        