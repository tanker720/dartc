class Critter(object):
    """Питомец, которого мы заслужили"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "замечательно"
        elif 5 <= unhappiness <= 10:
            m = "пойдет"
        elif 11 <= unhappiness <= 15:
            m = "такое себе"
        else:
            m = "лучше меня не трогать"
        return m

    def talk(self):
        print("Мое имя", self.name, ", и мое состояние сейчас - ", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        print("Ням-ням, спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Играть - всегда весело")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как  вы назовете свою зверюшку?")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
        ("""
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствии зверушки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Извините. Такого пункта в меню не существует")
main()
input("\n\nНажмите Enter, чтобы выйти.")
