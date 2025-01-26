from matplotlib import pyplot as plt
import plotly.express as px
import numpy as np

#data
categories = ["Glacier Size", "Revenue", "Envrionment", "Expenditure", "Water Supply"]
# Revenue = One day = 400$ per person

Tour_1 = [4, 1, 2, 3, 4]
Tour_1 = np.concatenate((Tour_1, [Tour_1[0]]))
categories=np.concatenate((categories, [categories[0]]))

label_placement = np.linspace(start=0, stop=2*np.pi, num=len(Tour_1))

print ("radians", label_placement)
print ("degrees", np.degrees(label_placement))

plt.figure( figsize=(6,6))
plt.subplot(polar=True)
plt.plot(label_placement, Tour_1)
lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categories)
plt.title("Tourist's affect on other factors", y=1.1, fontdict={"fontsize": 10})
plt.show()

