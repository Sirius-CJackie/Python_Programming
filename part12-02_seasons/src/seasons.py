# Write your solution here:
def sort_by_seasons(items: list):
    def get_seasons(item):
        return item["seasons"]
    
    return sorted(items, key=get_seasons)
