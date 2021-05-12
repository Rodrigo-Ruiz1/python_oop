class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness):
        self.fullness -= hunger
        self.happiness -= mopiness

cujo = Pet("Cujo")
cujo.eat_food()
print(cujo.fullness)
# 80
print(cujo.happiness)
# 50

benji = Pet("Benji")
benji.get_love()
print(cujo.fullness)
# 50
print(benji.happiness)
# 80