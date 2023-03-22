class FundingRound:
    
    all = []

    def __init__(self, s_inst, vc, type, investment):
        self._startup = s_inst
        self._vc = vc
        self.type = type
        self.invest = abs(investment)
        FundingRound.all.append(self)
