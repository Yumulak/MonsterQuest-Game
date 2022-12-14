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


orc = Orc("Orc", 200)
elf = Elf("Elf", 100)
human = Human("Human", 150)


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


golem = Golem("Golem", 300, 100, "at least four horses tall")
basilisk = Wyvern("Basilisk", 250, 150, "at least three horses tall")
gryphon = Gryphon("Gryphon", 200, 200, "at least two of those caravans tall")
wolfman = Werewolf("Wolfman", 150, 250, "at least two horses tall")

monsterNames = [wolfman.name, basilisk.name, gryphon.name, golem.name]

fighter = "drunken fighter"
fighterHp = 100

fightRounds = [123]
