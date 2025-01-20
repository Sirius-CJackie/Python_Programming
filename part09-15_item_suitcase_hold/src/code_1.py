# Write your solution here:
class Item:
    def __init__(self,name,weight):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    
    def name(self):
        return self.__name
    
    
    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self,mweight):
        self.mweight = mweight 
        self.items = []
    
    def weight(self):
        return sum(item.weight() for item in self.items)
    
    def add_item(self,item):
        if sum(item.weight() for item in self.items) + item.weight() <= self.mweight:
            self.items.append(item)
    
    def __str__(self):
        num_items = len(self.items)
        if num_items == 1:
            return f"{num_items} item ({sum(item.weight() for item in self.items)} kg)"
        else:
            return f"{num_items} items ({sum(item.weight() for item in self.items)} kg)"
    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        heaviest_item = self.items[0]
        for item in self.items[1:]:
            if item.weight() > heaviest_item.weight():
                heaviest_item = item
        return heaviest_item

class CargoHold:
    def __init__(self, max_weight):
        self.mweight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() <= self.mweight:
            self.suitcases.append(suitcase)
        

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.suitcases)

    def __str__(self):
        num_suitcases = len(self.suitcases)
        available_space = self.mweight - self.weight()
        if num_suitcases == 1:
            return f"{num_suitcases} suitcase, space for {available_space} kg"
        else:
            return f"{num_suitcases} suitcases, space for {available_space} kg"
    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()

