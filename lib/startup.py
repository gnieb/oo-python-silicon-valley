from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:
    all = []
    def __init__(self, name, founder, domain ):
        self._name = name
        self.founder = founder
        self._domain = domain
        Startup.all.append(self)

    def pivot(self, domain, name):
        self._name = name
        self._domain = domain


# given a string of a **founder's name**, returns the **first startup instance** whose founder's name matches
    @classmethod
    def find_by_founder(cls, founder_name):
        startup_list = []
        for s in cls.all:
            if s.founder == founder_name:
                startup_list.append(s)
        return startup_list[0]
    
    def sign_contract(self, venture_capitalist_object, type, investment):
        FundingRound(self, venture_capitalist_object, type, investment)

    @property
    def num_funding_rounds(self):
        return len([s for s in FundingRound.all if s._startup == self])

    @property
    def total_funds(self):
        total_funding = 0
        for s in FundingRound.all:
            if s._startup == self:
                total_funding += s.investment
        return total_funding
    
    @property
    def investors(self):
        return list({s._venture_capitalist for s in FundingRound.all })
