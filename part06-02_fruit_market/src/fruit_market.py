# write your solution here
def read_fruits():
    fruits_dict = {}
    with open("fruits.csv") as file:
        for line in file:
              
            fruit, price_str = line.strip().split(';')
            price = float(price_str)
            fruits_dict[fruit] = price
    
        return fruits_dict

