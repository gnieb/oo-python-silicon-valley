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
    

    def offer_contract(self, startup_object, type, investment):
        return FundingRound(startup_object, self, type, investment)

    @property
    def funding_rounds(self):
        return len([f for f in FundingRound.all])
    
    @ property
    def portfolio(self):
        return list({s for s in FundingRound.all})
    
    @property
    def biggest_investment(self):
        investments = [f.investment for f in FundingRound.all]
        investments.sort(reverse = True)
        return investments[0]
    
    def invested(self, domain):
        
        invested_in_domain = 0
        for f in FundingRound.all:
            if f._startup._domain == domain:
                invested_in_domain += f.investment
            return invested_in_domain