from tkinter import *

window = Tk()

window.title("Miles to KM Converter")
# window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

equalsTo = Label(text="My Label", font=("Arial", 18))
equalsTo.grid(column=0, row=1)  # To pack label o n screen
equalsTo.config(text="is equal to")

Miles_input = Entry(width=7)
Miles_input.grid(column=1, row=0)

Unit_mile = Label(text="My Label1", font=("Arial", 18))
Unit_mile.grid(column=2, row=0)
Unit_mile.config(text="Miles")

Unit_km = Label(text="My Label2", font=("Arial", 18))
Unit_km.grid(column=2, row=1)
Unit_km.config(text="Km")


def miles_to_km():
    miles = float(Miles_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

km_result = Label(text="My Label2", font=("Arial", 18))
km_result.grid(column=1, row=1)
km_result.config(text="0")

window.mainloop()
