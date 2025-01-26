import mesa
import random

class Tourist(mesa.Agent):
    def __init__(self, unique_id, model, current_location):
        super().__init__(unique_id, model)
        self.current_location = current_location

    def interact_with_hotel(self, hotel):
        hotel_room_price=hotel.get_hotel_room_cost()
        hotel_service_price=hotel.get_hotel_service_cost()
        hotel_room_price=random.randint(100,500)
        hotel_service_price=random.randint(0,200)
        return (f"In total I payed {str(hotel_room_price+hotel_service_price)} $.")

    def step(self):
        hotel = next(agent for agent in self.model.schedule.agents if isinstance(agent, Hotel))
        print (f"hi my unique id {str(self.unique_id)}. Here is a try to interact with hotel {self.interact_with_hotel(hotel)}")



class Hotel(mesa.Agent):
    def __init__(self, unique_id, model, hotel_room_cost, hotel_service_cost):
        super().__init__(unique_id, model)
        self.hotel_room_cost=hotel_room_cost
        self.hotel_service_cost=hotel_service_cost


    def get_hotel_room_cost(self):
        return self.hotel_room_cost
        
    def get_hotel_service_cost(self):
        return self.hotel_service_cost


class HotelModel(mesa.Model):
    def __init__(self, num_tourists, num_hotels):
        self.num_tourists=num_tourists
        self.num_hotels=num_hotels
        self.schedule=mesa.time.RandomActivation(self) # self schedule is responseible for the order of agents activation
        
        for i in range (self.num_hotels):
            hotel=Hotel(i, self, hotel_room_cost=200, hotel_service_cost=50)
            self.schedule.add(hotel)

        for i in range(self.num_tourists):
            tourist = Tourist(i, self, current_location=2)
            self.schedule.add(tourist)
   
    def step(self):
        self.schedule.step()