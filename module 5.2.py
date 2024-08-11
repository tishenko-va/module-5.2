class House:
    def __init__(self, name, num):
        self.name = name
        self.number_of_floors = num
    def go_to(self, new_flor):
        if 1 < new_flor and new_flor < self.number_of_floors:
            for i in range(1, new_flor + 1):
                print(i)
        else:
            print('Такого этажа не существует')
#__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
#__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))
