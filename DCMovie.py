class DCMovie:
    def __init__(self, title: str, release_year: int, genre: str, director: str, 
                 budget_m: float, box_office_m: float, rating: float, 
                 duration_mins: int, mpaa_rating: str):
        self.title = title            
        self.release_year = release_year 
        self.genre = genre           
        self.director = director      
        self.budget_m = budget_m     
        self.box_office_m = box_office_m
        self.rating = rating       
        self.duration_mins = duration_mins 
        self.mpaa_rating = mpaa_rating 