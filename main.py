from tkinter import *

#Set functionality
def conv_dist():
    lblVal.config(text=int(txtMiles.get())*1.60934)

#Show window elements
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
txtMiles = Entry(text="Enter miles here...")
lblConv = Label(text="is equal to")
lblMiles = Label(text="Miles")
lblKm = Label(text="Km")
lblVal = Label(text="0")
btnCalc = Button(text="Calculate", command=conv_dist)

#Assign grid positions
txtMiles.grid(column=1, row=0)
lblConv.grid(column=0, row=1)
lblMiles.grid(column=2, row=0)
lblKm.grid(column=2, row=1)
lblVal.grid(column=1, row=1)
btnCalc.grid(column=1, row=2)
txtMiles.focus()

window.mainloop()
