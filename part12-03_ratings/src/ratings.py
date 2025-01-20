# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def get_rating(item):
        return item["rating"]
    return sorted(items, key=get_rating, reverse=True)