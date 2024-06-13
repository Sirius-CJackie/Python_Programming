# Write your solution here:
class Series:
    def __init__(self, name, number, types):
        self.title = name
        self.number = number
        self.types = types
        self.ratings = []
        self.average = 0

    def __str__(self):
        genre_string = ", ".join(self.types)
        if self.ratings:
            ratings_string = f"{len(self.ratings)} ratings, average {self.average:.1f} points"
        else:
            ratings_string = "no ratings"
        return f"{self.title} ({self.number} seasons)\ngenres: {genre_string}\n{ratings_string}"
   
    def rate(self, rating):
        self.ratings.append(rating)
        self.average = sum(self.ratings) / len(self.ratings)
    
def minimum_grade(rating, series_list):
    return [series for series in series_list if series.ratings and series.average >= rating]

def includes_genre(genre, series_list):
    return [series for series in series_list if genre in series.types]


