class Tourist:
    def __init__(self, unique_id, model, current_location, pos):
        super().__init__(unique_id, model)
        self.current_location= current_location
        self.pos= pos

    def move_to_hotel(self, hotel):
        self.current_location=hotel
        hotel.add_tourist(self)

    def interact_with_hotel (self, hotel):
        room_price=hotel.room_service_price
        hotel_service_price=hotel.get_service_price
        total_hotel_cost=room_price+hotel_service_price
        return (f"Total Hotel price was: {total_hotel_cost}")


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
        

