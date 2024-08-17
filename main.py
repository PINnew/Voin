class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f'{self.name} лёг спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} сел кушать')
        self.power += 1

    def hit(self):
        print(f'{self.name} бьёт')
        self.endurance -= 6

    def walk(self):
        print(f'{self.name} гуляет')

    def info(self):
        print(f'имя война - {self.name}')
        print(f'цвет волос война - {self.hair_color}')
        print(f'сила война - {self.power}')
        print(f'выносливость война - {self.endurance}')

war1 = Warrior('Игорь', 76, 54, 'коричневый')
war2 = Warrior('Макс', 50, 50, 'белый')

print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)




