from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:
    
    all = []
    
    def __init__(self, name, founder, domain):
        self.name = name
        self._founder = founder
        self._domain = domain
        Startup.all.append(self)

    def pivot(self, name, domain):
        self.name = name
        self._domain = domain

    @classmethod
    def find_by_founder(cls, founder_name):
        return [s for s in cls.all if s._founder == founder_name ][0]
    
    @classmethod
    def domains(cls):
        return [s._domain for s in cls.all]
    
    def sign_contract(self, vc, type, amount):
        FundingRound(self, vc, type, amount)

    @property
    def fundingrounds(self):
        return [f for f in FundingRound.all if f._startup == self]

    @property
    def num_funding_rounds(self):
        return len(self.fundingrounds)
    
    @property
    def total_funds(self):
        total = 0
        for f in self.fundingrounds:
            total += f.invest
        return total
    
    @property
    def investors(self):
        return list({f._vc for f in self.fundingrounds })

    @property
    def big_investors(self):
        return list({f._vc for f in self.fundingrounds if f._vc.total_worth > 1000000000 })