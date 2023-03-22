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