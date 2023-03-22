class FundingRound:
    all = []
    def __init__(self, startup_object, venture_capitalist_object, type, investment ):
        self._startup = startup_object
        self._venture_capitalist = venture_capitalist_object
        self.type = type
        self.investment = abs(investment)
        FundingRound.all.append(self)
