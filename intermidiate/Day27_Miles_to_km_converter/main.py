from tkinter import *

window = Tk()
window.title("My first window")
window.minsize(500,300)

#Label

my_label = Label(text="is equal to ")
# my_label.place(x=15,y=15)
my_label.grid(column=0, row=1)

my_label1 = Label(text="Miles")
# my_label.place(x=15,y=15)
my_label1.grid(column=2, row=0)

my_label2 = Label(text="Km")
# my_label.place(x=15,y=15)
my_label2.grid(column=2, row=1)

my_label3 = Label(text="0")
# my_label.place(x=15,y=15)
my_label3.grid(column=1, row=1)
#Button

def button_clicked():
    miles = int(input.get())
    km = miles * 1.60934
    my_label3.config(text=km)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry

input = Entry(width=10)
input.grid(column=1, row=0)
print(input.get())


window.mainloop()
