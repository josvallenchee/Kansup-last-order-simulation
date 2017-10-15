class KantinAde():
    def __init__(self,food,price):
        self.food = food
        self.price = price

    def print_info_ade(self):
        print(self.food, " ", "Price(Rp):", self.price)

class SotoLamongan(KantinAde):
    def __init__(self,food,price):
        super().__init__(food,price)

    def print_info_lamongan(self):
        print(self.food, " ", "Price(Rp):", self.price)

class HajiBebek(KantinAde):
    def __init__(self,food,price):
        super().__init__(food,price)

    def print_info_haji(self):
        print(self.food, " ", "Price(Rp):", self.price)

class KantinIndomie(KantinAde):
    def __init__(self,food,price):
        super().__init__(food,price)

    def print_info_indomie(self):
        print(self.food, " ", "Price(Rp):", self.price)