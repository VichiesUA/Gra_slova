class Animals:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def get_name(self):
        print(f'Ім\'я собаки ==> {self.name}')

    def get_age(self):
        print(f'Вік собаки ==> {self.age}')

    def get_colour(self):
        print(f'Колір собаки ==> {self.colour}')


class Birds(Animals):
    def __init__(self, name, age, colour, speed):
        super().__init__(name, age, colour)
        self.speed = speed

    def get_name(self):
        print(f'Ім\'я пташки ==> {self.name}')

    def get_age(self):
        print(f'Вік пташки ==> {self.age}')

    def get_colour(self):
        print(f'Колір пташки ==> {self.colour}')

    def get_speed(self):
        print(f'Швидкість пташки ==> {self.speed}')


cat = Birds(input('Введіть ім\'я ==> '), int(input('Введіть вік ==> ')), input('Введіть колір ==> '),
            int(input('Введіть швидкість ==> ')))
cat.get_name()
cat.get_age()
cat.get_colour()
cat.get_speed()
