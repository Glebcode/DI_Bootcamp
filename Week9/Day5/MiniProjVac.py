class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
    def __str__(self):
        return "one of the instances"

class Queue:
    def __init__(self):
        self.humans = []
    def add_person(self, person):
        if person.age >= 60:
            self.humans.insert(0, person)
            # print(self.humans)
    def find_in_queue(self, person):
        return self.humans.index(person)
    def swap(self, person1, person2):
        index_pr1 = self.find_in_queue(person1)
        index_pr2 = self.find_in_queue(person2)
        self.humans[index_pr1], self.humans[index_pr2] = self.humans[index_pr2], self.humans[index_pr1]
        return self.humans
    def get_next(self):
        return self.humans[0]
        self.humans.remove(self.humans[0])
        self.humans.insert(x-1, self.humans[0])
    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                return self.humans[i]
    def sort_by_age(self):
        priorities = []
        old_age = []
        other = []
        for i in range(len(self.humans)-1):
            if self.humans[i].priority == True:
                priorities.append(self.humans[i])
            elif self.humans[i].age >= 60:
                old_age.append(self.humans[i])
            else:
                other.append(self.humans[i])
            self.humans = priorities + old_age + other
        return self.humans

jack = Human("aa345678aa", "Jack", 61, False, "A")
sara = Human("bb345678aa", "Sara", 20, True, "B")
abraham = Human("aa345678bb", "Abraham", 55, False, "A")
lill = Human("cc345678aa", "Lill", 70, False, "B")

queue = Queue()
queue.add_person(jack)
queue.add_person(sara)
queue.add_person(abraham)
queue.add_person(lill)
queue.get_next_blood_type('A')
print(queue.find_in_queue(jack))
queue.sort_by_age()
