import mesa
import seaborn as sns
import numpy as np
import pandas as pd


class Tourist(mesa.Agent):
    def __init__(self, model, tourist_money):
        # Correctly call the parent Agent constructor
        super().__init__(model)  # Correct initialization for Mesa Agent
        self.tourist_money= tourist_money


    def pay_to_hotel(self, hotel):
        return (f"Hi, I am agent number {str(self.unique_id)} and I am paying to Hotel {str(self.tourist_money-hotel.get_hotel_cost)}")

class Hotel(mesa.Agent):
    def __init__(self, model, hotel_cost):
        super().__init__(model)
        self.hotel_cost=hotel_cost
    
    def get_hotel_cost(self):
        return self.hotel_cost


class TourismModel(mesa.Model):
    """ A model with some number of agents"""
    def __init__(self, n, seed=None):
        super().__init__(self, n, seed=None)
        self.num_agents=n
        Tourist.create_agents(model=self, n=n)


    def step(self):
        self.agents.shuffle_do("pay_to_hotel")