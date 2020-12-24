from Assets.asset import Asset


class Car(Asset):
    def __init__(self, ival, rate):
        self._ival = ival
        self._rate = rate
        super(Car, self).__init__(ival, rate)


    def annualDepRate(self):
        return self._rate


class Civic(Car):
    def __init__(self, ival, rate=.15):
        self._ival = ival
        self._rate = rate
        super(Civic, self).__init__(ival, rate)

    def toString(self):
        return 'Civic'


class Lexus(Car):
    def __init__(self, ival, rate=.20):
        self._ival = ival
        self._rate = rate
        super(Lexus, self).__init__(ival, rate)

    def toString(self):
        return 'Lexus'


class Lamborghini(Car):
    def __init__(self, ival, rate=.25):
        self._ival = ival
        self._rate = rate
        super(Lamborghini, self).__init__(ival, rate)

    def toString(self):
        return 'Lamborghini'