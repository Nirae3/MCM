from tourism_model import HotelModel
import matplotlib as plt

n_tour=10
n_busin=2
n_hotel=4

from business_model import BusinessModel
model=BusinessModel(n_tour, n_busin)
model.step()

starter_model=HotelModel(n_tour, n_hotel)
for i in range(10):
    starter_model.step()

plt.show()