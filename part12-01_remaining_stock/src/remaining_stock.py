# Write your solution here:
def sort_by_remaining_stock(items: list):
    return sorted(items, key=lambda x: x[2])
