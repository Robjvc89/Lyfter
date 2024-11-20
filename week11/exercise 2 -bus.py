class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers =[]  
    
    
    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f'{person.name} has gotten on the bus.')
        else:
            print('The bus is full. It cannot add more passengers.')


    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person.name} got off the bus.')
        else:
            print(f'{person.name} is not on the bus.')
        

    def current_passengers(self):
        return [person.name for person in self.passengers]


person1 = Person("Gabriel")
person2 = Person("Priss")
person3 = Person("Adrian")
person4 = Person("Mariana")


bus = Bus(3)

bus.add_passenger(person1)  
bus.add_passenger(person2)  
bus.add_passenger(person3)  
bus.add_passenger(person4)

print("Current passengers:", bus.current_passengers())

bus.remove_passenger(person2)
bus.add_passenger(person4)

print("Current passengers:", bus.current_passengers())