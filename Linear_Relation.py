import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Base parameters
num_tourists = 10000  # tourists per month
emissions_per_tourist = 0.5  # tons of CO2 per tourist
spending_per_tourist = 500  # dollars
tax_rate = 0.1  # 10%

# Sensitivity ranges
tourist_changes = np.linspace(-0.2, 0.2, 9)  # ±20% change
tax_changes = np.linspace(0.05, 0.2, 4)  # 5% to 20% tax rates

# Calculate carbon footprint and revenue
results = []
for change in tourist_changes:
    tourists = num_tourists * (1 + change)
    carbon_footprint = tourists * emissions_per_tourist
    revenue = tourists * spending_per_tourist
    for tax in tax_changes:
        net_revenue = revenue * (1 - tax)
        results.append([tourists, carbon_footprint, revenue, tax, net_revenue])

# Create a DataFrame
df = pd.DataFrame(results, columns=['Tourists', 'Carbon Footprint', 'Revenue', 'Tax Rate', 'Net Revenue'])

# Plotting sensitivity analysis
plt.figure(figsize=(10, 6))
for tax in tax_changes:
    subset = df[df['Tax Rate'] == tax]
    plt.plot(subset['Tourists'], subset['Net Revenue'], label=f'Tax Rate: {tax:.0%}')

plt.title("Sensitivity of Revenue to Tourists and Tax Rates")
plt.xlabel("Number of Tourists")
plt.ylabel("Net Revenue ($)")
plt.legend()
plt.grid()
plt.show()
