# why to but this outside the classes? add each one the apprpriate class as class attribute
inhabitants = []
ages = []
dict_liv_pl = {}
class Human():
    def __init__(self, name, age, living_place = None):
        self.name = name
        self.age = age
        self.living_place = living_place
    def move(self, building):
        inhabitants.append(self.name)
        ages.append(self.age)
        dict_liv_pl[self.living_place] = ''
        return self.living_place

class Building():
    def __init__(self, address, inhabitants = None):
        self.address = address
        self.inhabitants = inhabitants
class City():
    def __init__(self, name, buildings = None):
        self.name = name
        self.buildings = buildings
    def construct(self, address):
        if address in dict_liv_pl:
            dict_liv_pl[address] = self.buildings

    def info(self, address):
        print(f"The number of buildings {len(dict_liv_pl)}")
        sum_age = 0
        for i in range(len(ages)):
            sum_age = sum_age + ages[i]/len(ages)
        print(f"Mean age of the citizens {sum_age}")

pers_sam = Human('Sam', 20, 'NY Brooklyn')
pers_sam.move(2)
print(inhabitants)
print(ages)
print(dict_liv_pl)
sok_ny = City('Sok', 4)
sok_ny.construct('NY Brooklyn')
print(inhabitants)
print(ages)
print(dict_liv_pl)
pers_lod = Human('Lod', 30, 'Tel Aviv')
pers_lod.move(3)
bok_ny = City('Bok', 2)
bok_ny.construct('Tel Aviv')
sok_ny.info(dict_liv_pl)
print(inhabitants)
print(ages)
print(dict_liv_pl)
