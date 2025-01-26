from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from random import choice

class Tourist:
    def __init__(self, unique_id, model, current_location):
        super().__init__(unique_id, model)
        self.current_location= current_location

    def move_to_hotel(self, hotel):
        self.current_location=hotel
        hotel.add_tourist(self)

    def interact_with_hotel (self, hotel):
        room_price=hotel.room_service_price
        hotel_service_price=hotel.get_service_price
        total_hotel_cost=room_price+hotel_service_price
        return (f"Total Hotel price was: {total_hotel_cost}")
    
    def step(self):
        # we need for it to choose from other hotels
        hotel_choice=choice(self.model.hotel)
        self.move_to_hotel(hotel_choice)
        print(self.interact_with_hotel(hotel_choice))



class Hotel:
    def __init__(self, unique_id, model, room_price, service_price):
        super().__init__(unique_id, model)
        self.room_price=room_price
        self.service_price = service_price
        self.visitors=[]
    
    def get_room_price (self):
        return self.room_price
    
    def get_service_price(self):
        return self.service_price

    def add_tourist(self, tourist):
        if tourist not in self.visitors:
            self.visitors.append(tourist)
    
    def get_visitor_count(self):
        return len(self.visitors)
    
    def get_tourist_revenue(self):
        return (f"the total revenue is {len(self.visitors)*500} $")
    
    def step(self):
        # Example of Hotel actions per step (can expand with more hotel behaviors)
        print(f"Hotel {self.unique_id} has {self.get_visitor_count()} visitors.")
        print(self.get_tourist_revenue())

class TourismModel(Model):
    def __init__(self, num_tourists, num_hotels, width, height):
        self.num_tourists = num_tourists
        self.num_hotels = num_hotels
        self.width = width
        self.height = height
        
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(self.width, self.height, True)
        
        # Create hotels
        self.hotels = []
        for i in range(self.num_hotels):
            hotel = Hotel(i, self, 100, 50)
            self.hotels.append(hotel)
            self.schedule.add(hotel)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(hotel, (x, y))
        
        # Create tourists
        for i in range(self.num_tourists):
            tourist = Tourist(i + self.num_hotels, self, None, (0, 0))
            self.schedule.add(tourist)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(tourist, (x, y))

    def step(self):
        self.schedule.step()

# Run the model for a few steps
model = TourismModel(5, 2, 10, 10)

for i in range(10):
    print(f"Step {i}")
    model.step()