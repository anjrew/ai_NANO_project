
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys


# CUSTOMER VARIABLES
qsWorkers = 2
qsWage = 50000
qsYearlyLabourCost = qsWage * qsWorkers
modulesPerYear = 6000
expectedYearReturn = 8

# AI VARIABLES
dataNodesNeeded = 12000
reasons = 6000

# OTHER VARIABLES
years = 10

# ECK VARIABLES
priceCouldCharge = qsYearlyLabourCost * expectedYearReturn

price = [ ]
labourCost = []
i = 0
while i < years:
    labourCost.append(qsYearlyLabourCost * i) 
    price.append(priceCouldCharge)
    i = i+1

# PLOTTING
fig, ax = plt.subplots()
ax.plot( range(0, years), price, range(0, years), labourCost )

# LEGEND
ax.set(xlabel='Time', ylabel='Cost', title='Payback period')
ax.legend(['Price', 'Cost'])
ax.grid()

# SAVING PNG AND RENDERING
fig.savefig("test.png")
plt.show()

exit()