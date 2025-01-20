# Write your solution here
def search(products, criterion):
    return [product for product in products if criterion(product)]