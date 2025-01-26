import agentpy as ap


class Tourist(ap.Agent):
    def setup(self):
        self.budget=self.p.budget


class Hotel(ap.Agent):
    def setup(self):
        self.revenue=0
        self.visitors=set()

    def revenue(self, tourist):
        if tourist.id not in self.visitors:
            self.visitors.add(tourist.id)
            self.revenue+=300
            return (f"Tourist id: {str(tourist.id)} Revenue: {str(self.revenue)}")
        else:
            return (f"Tourist id: {str(tourist.id)} has already entered")
        

class ToursitHotel(ap.Model):
    def setup(self):
        self.agents=ap.AgentList(self, self.p.n, Tourist)

    def step(self):
        tourist = self.random.choice(self.tourists)
        tourist.visit_hotel(self.hotel)     