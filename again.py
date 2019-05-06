import numpy as np
import matplotlib.pyplot as plt


# Making the first plot work. Make 1-D arrays: rents, downs
monthes   = 12 * 30
Prop_val  = 200000
Expense  = 2000
rate      = 4.375
rents     = np.linspace(Expense, Expense * 1.5, 41)
downs     = np.linspace(0,1, 21)
loans     =  Prop_val - (downs * Prop_val)
mortgages = loans * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1)
Tax  = 100
Insurance = 150
Utilities= 0
HOA =0
Lawn_snow = 0
Repairs= 100
Capex = 100
Manager = 200
Expenses   = Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + mortgages

# Generate 2-D arrays from u and v: X, Y
RENT,DOWN = np.meshgrid(rents,downs)
FLOW = RENT - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1)))
# Display the resulting image with pcolor()
plt.xlabel('RENT')

plt.pcolor(RENT, DOWN, FLOW, cmap = 'gray')
plt.colorbar()
plt.axis('tight')
plt.show()


import numpy as np
import matplotlib.pyplot as plt


# Making the first plot work. Make 1-D arrays: rents, downs

monthes   = 12 * 30
Prop_val  = 200000
Expense  = 2000
rate  = 4.375
rents = np.linspace(Expense, Expense * 1.5, 41)
downs = np.linspace(0,1, 21)
loans =  Prop_val - (downs * Prop_val)
mortgages = loans * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1)
Tax  = 100
Insurance = 150
Utilities= 0
HOA =0
Lawn_snow = 0
Repairs= 100
Capex = 100
Closing = 3000
Manager = 200
Expenses   = Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + mortgages

# Generate 2-D arrays from u and v: X, Y
RENT,DOWN = np.meshgrid(rents,downs)
FLOW = RENT - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1)))

Rehab = 70000
Other =0

# Plot 2
CoC = ((RENT - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1))))* 12) / ((DOWN * Prop_val) + Closing + Rehab + Other)
fig, ax = plt.subplots()
CS = ax.contour(RENT, DOWN * 100, CoC)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('CoC vs. Down vs. Rent')
plt.xlabel('RENT ($ monthly)')
plt.ylabel('DOWN (% property value)')
plt.show()
# I SHOULD FIND THE GRADIENT SO I CAN MATCH THE BEST DOWN PAYMENT TO AN APPROPRIATE RENT ###

CoC = ((RENT - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1))))* 12) / ((DOWN * Prop_val) + Closing + Rehab + Other)

plt.contourf(RENT, DOWN * 100, CoC)
ax.set_title('CoC vs. Down vs. Rent')
plt.xlabel('RENT ($ monthly)')
plt.ylabel('DOWN (% property value)')
plt.show()


import numpy as np
import matplotlib.pyplot as plt


# Making the first plot work. Make 1-D arrays: rents, downs

monthes   = 12 * 30
Prop_val  = 200000
Expense  = 2000
rate  = 4.375
rents = np.linspace(Expense, Expense * 1.5, 41)
downs = np.linspace(0,1, 21)
loans =  Prop_val - (downs * Prop_val)
mortgages = loans * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1)
Tax  = 100
Insurance = 150
Utilities= 0
HOA =0
Lawn_snow = 0
Repairs= 100
Capex = 100
Closing = 3000
Manager = 200
Expenses   = Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + mortgages

# Generate 2-D arrays from u and v: X, Y
RENT,DOWN = np.meshgrid(rents,downs)
FLOW = RENT - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1)))

Rehab = 70000
Other =0

# Plot 2
CoC = ((RENT - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1))))* 12) / ((DOWN * Prop_val) + Closing + Rehab + Other)
fig, ax = plt.subplots()
CS = ax.contour(RENT, DOWN * 100, CoC)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('CoC vs. Down vs. Rent')


#plot 3 (with gradient vectors)
horizontal_stepsize = (max(rents) - min(rents)) / len(rents)
vertical_stepsize   = (max(downs) - min(rents)) / len(rents)

RENT_shift = RENT + horizontal_stepsize/2.0
DOWN_shift = RENT + vertical_stepsize/2.0

CoC_shift = ((RENT_shift - (Tax + Insurance + Utilities + HOA + Lawn_snow + Repairs + Capex + Manager + ((Prop_val - (DOWN_shift * Prop_val)) * (rate * (1 + rate) ** monthes) / ((1 + rate ) ** monthes -1))))* 12) / ((DOWN_shift * Prop_val) + Closing + Rehab + Other)

yd, xd = np.gradient(CoC_shift)

def func_to_vectorize(x, y, dx, dy, xscaling=1, yscaling= 1):
    plt.arrow(x, y, dx*xscaling, dy*yscaling, fc='k', ec='k', head_width=0.06, head_length=0.1)

vectorized_arrow_drawing = np.vectorize(func_to_vectorize)

plt.contourf(RENT, DOWN, CoC)
vectorized_arrow_drawing(RENT_shift, DOWN_shift, xd, yd, 1, 0.1)
plt.colorbar()
plt.show()


