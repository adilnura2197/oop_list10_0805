class Computer:
    def __init__(self, model, narx):
        self.model = model
        self.narx = narx

    def info(self):
        print(f"{self.model} - narxi: {self.narx} so'm")


class Store:
    def __init__(self, nomi, kompyuterlar=[]):
        self.nomi = nomi
        self.kompyuterlar = kompyuterlar

    def kompyuter_qoshish(self, kompyuter):
        self.kompyuterlar.append(kompyuter)
        print(f"Yangi kompyuter qo'shildi: {kompyuter.model}")

    def store_info(self):
        print(f"Do'kon: {self.nomi}")

        for kompyuter in self.kompyuterlar:
            kompyuter.info()


c1 = Computer("HP", 7000000)
c2 = Computer("Dell", 8500000)

roy = [c1, c2]

s1 = Store("IT Market", roy)
s1.store_info()

c3 = Computer("Lenovo", 9200000)
s1.kompyuter_qoshish(c3)
