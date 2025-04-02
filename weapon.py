
class Weapon():
    def __init__(self, name, range, power, rate, damage):
        self.name = name
        self.range = range
        self.power = power
        self.rate = rate
        self.damage = damage

class Rifle(Weapon):
    def __init__(self):
        super().__init__(
            "Submachine",
            20,
            150,
            0.7,
            50)

class Submachine(Weapon):
    def __init__(self):
        super().__init__(
            "Submachine",
            10,
            200,
            0.3,
            75)
        
class SniperRifle(Weapon):
    def __init__(self):
        super().__init__(
            "Rifle",
            40,
            1000,
            1,
            150)