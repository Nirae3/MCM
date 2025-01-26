import mesa
import seaborn as sns
import numpy as np
import pandas as pd



class Tourist(mesa.Agent):
    def __init__(self, unique_id, model):
        # Correctly call the parent Agent constructor
        super().__init__(unique_id, model)  # Correct initialization for Mesa Agent
#        self.current_location = current_location

#    def move_to_hotel(self, hotel):
#        self.current_location = hotel
#        hotel.add_tourist(self)

#    def interact_with_hotel(self, hotel):
#        room_price = hotel.get_room_price()
#        hotel_service_price = hotel.get_service_price()
#        total_hotel_cost = room_price + hotel_service_price
#        return f"Total Hotel price was: {total_hotel_cost}"
    
#    def step(self):
        # Choose a hotel randomly from the list of hotels
 #       hotel_choice = choice(self.model.hotels)
 #       self.move_to_hotel(hotel_choice)
 #       print(self.interact_with_hotel(hotel_choice))


class Hotel(mesa.Agent):
    def __init__(self, unique_id, model, room_price, service_price):
        # Correctly call the parent Agent constructor
        super().__init__(unique_id, model)  # Correct initialization for Mesa Agent
        self.room_price = room_price
        self.service_price = service_price
        self.visitors = []
    
    def get_room_price(self):
        return self.room_price
    
    def get_service_price(self):
        return self.service_price

    def add_tourist(self, tourist):
        if tourist not in self.visitors:
            self.visitors.append(tourist)
    
    def get_visitor_count(self):
        return len(self.visitors)
    
    def get_tourist_revenue(self):
        return f"the total revenue is {len(self.visitors) * 500} $"
    
    def step(self):
        print(f"Hotel {self.unique_id} has {self.get_visitor_count()} visitors.")
        print(self.get_tourist_revenue())


class TourismModel(mesa.Model):
    """ A model with some number of agents"""
    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents=n
        Tourist.create_agents(model=self, n=n)

    def step(self):
        self.agents.shuffle_do("say hi")

