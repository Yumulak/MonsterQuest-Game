class Character:
    def __init__(self, name, hp):
        self.hp = hp
        self.name = name


class Human(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.hp = 150
        self.name = "Human"


class Orc(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.hp = 200
        self.name = "Orc"


class Elf(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.hp = 100
        self.name = "Elf"


class Enemy:
    def __init__(self, name, hp, dmg, height):
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.height = height


class Wyvern(Enemy):
    def __init__(self, name, hp, dmg, height):
        super().__init__(name, hp, dmg, height)
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.height = height


class Gryphon(Enemy):
    def __init__(self, name, hp, dmg, height):
        super().__init__(name, hp, dmg, height)
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.height = height


class Werewolf(Enemy):
    def __init__(self, name, hp, dmg, height):
        super().__init__(name, hp, dmg, height)
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.height = height


class Golem(Enemy):
    def __init__(self, name, hp, dmg, height):
        super().__init__(name, hp, dmg, height)
        self.hp = hp
        self.dmg = dmg
        self.name = name
        self.height = height
        
