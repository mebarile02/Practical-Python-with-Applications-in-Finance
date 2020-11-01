from classFiles.asset import Asset


class HouseBase(Asset):
    def __init__(self, ival, rate):
        self._ival = ival
        self._rate = rate
        super(HouseBase, self).__init__(ival, rate)

    def annualDepRate(self):
        return self._rate


class PrimaryHome(HouseBase):
    def __init__(self, ival, rate=.03):
        self._ival = ival
        self._rate = rate
        super(PrimaryHome, self).__init__(ival, rate)


class VacationHome(HouseBase):
    def __init__(self, ival, rate=.02):
        self._ival = ival
        self._rate = rate
        super(VacationHome, self).__init__(ival, rate)
