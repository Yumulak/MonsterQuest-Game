class weapon:
    def __init__(self, dmg):
        self.dmg = 0


class swordAndShield(weapon):
    def __init__(self, dmg):
        super().__init__(dmg)
        self.dmg = 100


class spear(weapon):
    def __init__(self, dmg):
        super().__init__(dmg)
        self.dmg = 120


class bow(weapon):
    def __init__(self, dmg):
        super().__init__(dmg)
        self.dmg = 90


class sorcery(weapon):
    def __init__(self, dmg):
        super().__init__(dmg)
        self.dmg = 130


class axe(weapon):
    def __init__(self, dmg):
        super().__init__(dmg)
        self.dmg = 110
