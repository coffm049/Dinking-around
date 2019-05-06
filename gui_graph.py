# This is taken from examples from the following url
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Add-a-combobox-widget
# The grid layout is as follows
# Col 0    : Section headers
# Col 1    : Prompts
# Col 2    : dialog boxes
# Row 0    : Title
# Row 1-6  : Initial costs inputs
# Row 7-8  : Initial costs sum
# Row 11-14: Income

from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np



window = Tk()
window.title("Calculating CoC ROI")


# Row 0
Label(window, text="Property Evaluator", font=(64)).pack(side = TOP)


# Row 1
# Initial Costs Header
Icost_fr = LabelFrame(window, text="Initial Costs", font=(24))
Icost_fr.pack(side= LEFT)
# Initial Costs input frame
Icost_in = Frame(Icost_fr)
Icost_in.pack(side=TOP)
Icost_out = Frame(Icost_fr)
Icost_out.pack(side=TOP)

# Enter the property value
Icost_lbls = Frame(Icost_in)
Icost_lbls.pack(side = LEFT)
Icost_ent = Frame(Icost_in)
Icost_ent.pack(side = RIGHT)
Label(Icost_lbls, text="Enter Property Value",bd =1).pack(side= TOP)
prop_val = Entry(Icost_ent, width=6)
prop_val.pack(side = TOP)
prop_val.insert(0, "0")


# Row 2 : Enter the down payment percentage
Label(Icost_lbls, text="Select Down Percent").pack(side = TOP)
down = Entry(Icost_ent, width=6)
down.insert(0,"0")
down.pack(side=TOP)

# Row 3: Renovations
Label(Icost_lbls, text="Renovation Costs").pack(side = TOP)
renovations     = Entry(Icost_ent, width=6)
renovations.pack(side= TOP)
renovations.insert(0,"0")

# Row 4: Closing Costs
Label(Icost_lbls, text= " ").pack(side = TOP) # spacer to align with scale bar
Label(Icost_lbls, text="Select closing percent cost").pack(side = TOP)
closing       = Scale(Icost_ent, from_=0, to=10, orient=HORIZONTAL)
closing.pack(side= TOP)

# Row 5: Misc
Label(Icost_lbls, text="Miscellaneous costs").pack(side = TOP)
misc_costs     = Entry(Icost_ent, width=6)
misc_costs.pack(side = TOP)
misc_costs.insert(0,"0")

# Row 6: Recalculate button
# add button functions
def loan_calc() :
    # convert all inserts into floats to make calculations easier to look at denote this by capitalizing first letter
    Prop_val   = float(prop_val.get())
    Down       = float(down.get())
    Renovations= float(renovations.get())
    Closing    = float((closing.get()/ 100) * Prop_val)
    Misc_costs = float(misc_costs.get())
    Down_pay   = Down * Prop_val / 100
    Total_price= Prop_val + Renovations + Closing + Misc_costs
    Total_cost = Down_pay + Renovations + Closing + Misc_costs
    Loan       = Prop_val - Down_pay
    Show_down.configure(text="Down Payment = $" + str(Down_pay))
    Show_loan.configure(text="Loan = $" + str(Loan))
    Show_total_price.configure(text="Total price = $" + str(Total_price))
    Show_total_cost.configure(text="Total personal cost = $" + str(Total_cost))

    # Cash Flow calcs

    # Income
    Rent    = float(rent.get())
    Vacancy = float(vacancy.get()) / 100
    Storage = float(storage.get())
    Other   = float(other.get())
    Income  = Rent * (1- Vacancy) + Storage + Other
    Income_lbl.configure(text= "Monthly Income = $" + str(Income))

    # Expenses
    # Mortgage, taxes, insurance, snow/lawn, utilities, HOA, CapEx, Repairs, Manager
    Monthes = float(years.get()) * 12
    Rate  = float(rate.get()) /1200
    # let user override the automatic mortgage calculator if they make an input
    if float(mortgage.get()) == 0 :
        Mortgage = Loan * (Rate * (1 + Rate) ** Monthes) / ((1 + Rate ) ** Monthes -1)
    else :
        Mortgage  = float(mortgage.get())
    Tax       = float(tax.get())
    Insurance = float(insurance.get())
    Snow_Lawn = float(snow_lawn.get())
    Utilities = float(utilities.get())
    HOA       = float(hoa.get())
    CapEx     = float(capex.get())
    Repairs   = float(repairs.get())
    Manager   = float(manager.get())
    Expenses  = Mortgage + Tax + Insurance + Snow_Lawn + Utilities + HOA + CapEx + Repairs + Manager
    Expenses_lbl.configure(text= "Monthly Expenses = $" + str(Expenses))

    # Cash flow
    Flow = Income - Expenses
    CashFlow.configure(text= "Monthly Cash flow = $ " + str(Flow))


    # CoC ROI
    CoC = Flow / Total_cost
    CoC_lbl.configure(text= "Yearly CoC ROI = " + str(CoC*12) + "%")

    if Mortgage == 0 :
        erase.configure(text="yes")
    else :
        erase.configure(text="no")


#add physical button
calc_btn = Button(window, text= "Calculate", command=loan_calc).pack(side = BOTTOM)


# Row 7-8: Display Down payment and Loan
Show_down = Label(Icost_out, text="Down Payment")
Show_down.pack(side = BOTTOM)
Show_loan = Label(Icost_out, text="Loan Value")
Show_loan.pack(side = BOTTOM)
Show_total_price = Label(Icost_out, text="Total Price")
Show_total_price.pack(side = BOTTOM)
Show_total_cost  = Label(Icost_out, text="Total Cost")
Show_total_cost.pack(side = BOTTOM)
######################################################
# Cash flow
CF_fr = LabelFrame(window, text="Cash Flow", font=(32))
CF_fr.pack(side= TOP)
CF_in = Frame(CF_fr)
CF_in.pack(side=TOP)
CF_lbls = Frame(CF_in)
CF_lbls.pack(side=LEFT)
CF_ents = Frame(CF_in)
CF_ents.pack(side=RIGHT)
CF_out = Frame(CF_fr)
CF_out.pack(side=TOP)

# Income
Label(CF_lbls, text="Income", font=(24)).pack(side = TOP)
Label(CF_ents, text= "AS", font= (24)).pack(side=TOP) # top align with label
Label(CF_ents, text= "AS", font= (24)).pack(side=TOP) # top align with label
# Row 11: Rent
Label(CF_lbls, text= "Rent").pack(side = TOP)
rent     = Entry(CF_ents, width = 6)
rent.insert(0,"0")
rent.pack(side = TOP)
Label(CF_lbls, text= " ").pack(side=TOP)
vacancy_lbl = Label(CF_lbls, text= "Vacancy rate (%)").pack(side = TOP)
vacancy     = Scale(CF_ents, from_=0, to=10, orient = HORIZONTAL)
vacancy.pack(side = TOP)
Label(CF_lbls, text= "Storage").pack(side = TOP)
storage = Entry(CF_ents, width= 6)
storage.pack(side = TOP)
storage.insert(0,"0")
Label(CF_lbls, text= "Other").pack(side = TOP)
other = Entry(CF_ents, width=6)
other.insert(0,"0")
other.pack(side = TOP)

# Expenses
# Row 15: Expenses
Label(CF_lbls, text="Expenses", font=(24)).pack(side = TOP)
Label(CF_ents, text="Mirror", font=(24)).pack(side= TOP) # to make sure the boxes align
Label(CF_lbls, text="Mortgage").pack(side = TOP)
mortgage = Entry(CF_ents, width=6)
mortgage.pack(side = TOP)
mortgage.insert(0, "0")

Label(CF_lbls, text="Rate").pack(side = TOP)
rate = Entry(CF_ents, width=6)
rate.pack(side = TOP)
rate.insert(0, "4.73")

Label(CF_lbls, text="Years").pack(side = TOP)
years= Entry(CF_ents, width=6)
years.pack(side = TOP)
years.insert(0, "30")

Label(CF_lbls, text= "Taxes").pack(side = TOP)
tax = Entry(CF_ents, width=6)
tax.pack(side = TOP)
tax.insert(0, "0")

Label(CF_lbls, text="Insurance").pack(side = TOP)
insurance = Entry(CF_ents, width=6)
insurance.pack(side = TOP)
insurance.insert(0,"0")

Label(CF_lbls, text="Snow/Lawn").pack(side = TOP)
snow_lawn = Entry(CF_ents, width=6)
snow_lawn.pack(side = TOP)
snow_lawn.insert(0, "0")

Label(CF_lbls, text="Utilities").pack(side = TOP)
utilities = Entry(CF_ents, width=6)
utilities.pack(side = TOP)
utilities.insert(0, "0")

Label(CF_lbls, text="HOA").pack(side = TOP)
hoa = Entry(CF_ents, width=6)
hoa.pack(side = TOP)
hoa.insert(0, "0")

Label(CF_lbls, text="CapEx").pack(side = TOP)
capex = Entry(CF_ents, width=6)
capex.pack(side = TOP)
capex.insert(0, "0")

Label(CF_lbls, text="Repairs").pack(side = TOP)
repairs = Entry(CF_ents, width=6)
repairs.pack(side = TOP)
repairs.insert(0, "0")

Label(CF_lbls, text="Manager").pack(side = TOP)
manager = Entry(CF_ents, width=6)
manager.pack(side = TOP)
manager.insert(0, "0")

Income_lbl = Label(CF_out, text= "Income")
Income_lbl.pack(side = TOP)
Expenses_lbl = Label(CF_out, text= "Expenses")
Expenses_lbl.pack(side = TOP)
CashFlow = Label(CF_out, text = "Cash Flow")
CashFlow.pack(side = TOP)

CoC_lbl = Label(CF_out, text= "CoC ROI")
CoC_lbl.pack(side = TOP)

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2* t)

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    window.quit()     # stops mainloop
    window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = Button(master=window, text="Quit", command=_quit)
button.pack(side=BOTTOM)


window.mainloop()

