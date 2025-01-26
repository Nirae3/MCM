import mesa
import random

class Tourist(mesa.Agent):
    def __init__(self, unique_id, model, current_location):
        super().__init__(unique_id, model)
        self.current_location = current_location

    def interact_with_business(self, business):
        business_price=business.get_business_cost()   # get business room price
        
        

        business_customer_list= business.get_customer_list().append(self.unique_id) # get customer line in a string


        
        
        return (f"In total I payed for business {str(business_price)} $.")   # return business total price

    def step(self):
        business = next(agent for agent in self.model.schedule.agents if isinstance(agent, Business)) #define business
        print (f"hi my unique id {str(self.unique_id)}. interact with business {self.interact_with_business(business)}")
        print(f"the business has {len(business.get_customer_list())} cusotmers")


class Business(mesa.Agent):
    def __init__(self, unique_id, model, business_cost, customers):
        super().__init__(unique_id, model)
        self.business_cost=business_cost
        self.customers=[]
    
    
    def get_customer_list(self):
        return self.customers
    
    def get_customer_amount(self):
        return (len(self.customers))



    def get_business_cost(self):
        return self.business_cost


class BusinessModel(mesa.Model):
    def __init__(self, num_tourists, num_businesses):
        self.num_tourists=num_tourists
        self.num_businesses=num_businesses
        self.schedule=mesa.time.RandomActivation(self) # self schedule is responseible for the order of agents activation
        
        for i in range (self.num_businesses):
            business=Business(i, self, business_cost=700, customers=0)
            self.schedule.add(business)

        for i in range(self.num_tourists):
            tourist = Tourist(i, self, current_location=2)
            self.schedule.add(tourist)

    def step(self):
        self.schedule.step()
   
