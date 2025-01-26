import random

class Agent:
    def __init__(self, start_location, destination, budget):
        self.start_location = start_location
        self.destination = destination
        self.current_location = start_location
        self.budget = budget
    
    def choose_path(self, environment):
        # Simple pathfinding: select the fastest path (based on the environment)
        # For now, just choose a path randomly from available paths
        return environment.find_shortest_path(self.start_location, self.destination)

    def move(self, path):
        for location in path:
            self.current_location = location
            print(f"Moving to: {location}")

    def interact_with_hotel(self, hotel):
        # Book a room and use hotel services
        room_cost = hotel.get_room_cost()
        services_cost = hotel.estimate_services_usage()
        total_cost = room_cost + services_cost
        print(f"Total cost for stay: {total_cost} (Room: {room_cost}, Services: {services_cost})")

        if self.budget >= total_cost:
            hotel.generate_revenue(total_cost)
            self.budget -= total_cost
            print(f"Agent can afford the stay. Remaining budget: {self.budget}")
        else:
            print("Agent cannot afford the stay.")

class Hotel:
    def __init__(self, room_price, service_prices):
        self.room_price = room_price
        self.service_prices = service_prices
        self.revenue = 0

    def get_room_cost(self):
        return self.room_price
    
    def estimate_services_usage(self):
        # Random estimation of services usage by the agent
        return sum(self.service_prices.values()) * random.uniform(0, 1)  # random chance to use services

    def generate_revenue(self, amount):
        self.revenue += amount
        print(f"Hotel's revenue generated: {amount}. Total revenue: {self.revenue}")

class Environment:
    def __init__(self):
        # Define a simple map of paths
        self.paths = {
            'Home': ['Street 1', 'Street 2'],
            'Street 2': ['Hotel'],
            'Hotel': []
        }
    
    def find_shortest_path(self, start, destination):
        # Simple pathfinding, we can assume it's always a direct path in this model
        return self.paths[start] if destination in self.paths[start] else []

# Example setup:

# Hotel with room price and services
hotel = Hotel(room_price=100, service_prices={'restaurant': 50, 'spa': 30, 'bar': 20})

# Environment setup (paths)
environment = Environment()

# Create an agent (starting at Home with a budget)
agent = Agent(start_location='Home', destination='Hotel', budget=200)

# Step 1: Choose path to the hotel
path = agent.choose_path(environment)
print(f"Chosen path: {path}")

# Step 2: Move along the path to the hotel
agent.move(path)

# Step 3: Interact with the hotel
agent.interact_with_hotel(hotel)

# Output the final revenue of the hotel
print(f"Final hotel revenue: {hotel.revenue}")