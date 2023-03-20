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
