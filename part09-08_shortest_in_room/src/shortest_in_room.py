# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
class Room:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if self.is_empty():
            print(f"There are 0 persons in the room, and their combined height is 0 cm")
        else:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")
    def shortest(self):
        if self.is_empty():
            return None
        if len(self.persons) == 1:
            shortest_person = self.persons[0]
        else:
            shortest_person = min(self.persons, key=lambda x: x.height)
        return shortest_person
    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person

