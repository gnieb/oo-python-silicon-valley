class FundingRound:
    
    all = []

    def __init__(self, s_inst, vc, type, investment):
        self.startup = s_inst
        self.vc = vc
        self.type = type
        self.invest = investment
        FundingRound.all.append(self)
