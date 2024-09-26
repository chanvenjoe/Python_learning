from tkinter import *
#import tkinter as tk
from PIL import Image , ImageTk #pip install pillow
import tkinter.messagebox

window = Tk()
window.geometry("600x600")
window.title("Radioflyer motor selection tool v0.1")

img = Image.open("C:/Users/kzhou/Desktop/RF projects/Git/Python_learning/Motor calculation/Photo/Logo.png")
photo = ImageTk.PhotoImage(img)

label = Label(image = photo)
label.pack()

bv          = StringVar()
max_weight  = StringVar()
wheel_size  = StringVar()
top_speed   = StringVar()
ramp_time   = StringVar()
gear_ratio  = StringVar()
incline_angle = StringVar()

var = StringVar()

def submit():
    batvol=bv.get()
    maxweight = max_weight.get()
    wheelsize = wheel_size.get()
    topspeed  = top_speed.get()
    print("Here is the information:...")
    tkinter.messagebox.showinfo("Hi, here is the info...", f'You want to select a motor for a ride-on({maxweight}Kg) to realize {topspeed}km/h with {batvol}V battery, and the wheel size is {wheelsize}mm ')
    #f is to turn the variables into number
def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("About",'This is a Radioflyer motor selection tool that helps you to get a motor recommendation based on the information you input \r\nPress enter to continue')
label1 = Label(window, text = " Welcome to Radioflyer motor selection tool", bg='red',fg='white', font = ("arial",16, "bold"))
label1.pack(fill = BOTH, pady=5, padx = 5, expand=False)

input1 = Label(window, text = "Battery Voltage(V):")
input1.place(x=10, y=150)
entry1 = Entry(window, textvar = bv)
entry1.place(x=110, y=150)

list1 = ['6','12', '24', '36', '48']
droplist = OptionMenu(window, bv,*list1)
droplist.config(width=1)
droplist.place(x=230, y=140)

input2 = Label(window, text = "Max weight(Kg):")
input2.place(x=300, y=150)
entry2 = Entry(window, textvar = max_weight)
entry2.place(x=400, y=150)

input3 = Label(window, text = "Wheel size(m):")
input3.place(x=10, y=200)
entry3 = Entry(window, textvar = wheel_size)
entry3.place(x=110, y=200)

input4 = Label(window, text = "Top speed(km/h):")
input4.place(x=300, y=200)
entry4 = Entry(window, textvar = top_speed)
entry4.place(x=400, y=200)

input5 = Label(window, text = "Ramp time(s):")
input5.place(x=300, y=250)
entry5 = Entry(window, textvar = ramp_time)
entry5.place(x=400, y=250)

input6 = Label(window, text = "Gear ratio:")
input6.place(x=10, y=250)
entry6 = Entry(window, textvar = gear_ratio)
entry6.place(x=110, y=250)

input7 = Label(window, text = "Incline angle:")
input7.place(x=10, y=300)
entry7 = Entry(window, textvar = incline_angle)
entry7.place(x=110, y=300)

label2 = Label(window, text = " Powered by Kevin @Radioflyer", fg = 'black')
label2.pack(side = BOTTOM, fill = NONE)
button1 = Button(window, text = "Get motor recommendation", fg = 'white', bg = 'blue', relief = RAISED, font = ("arial",16, "bold"), command = submit  )
button1.pack(side = BOTTOM, fill = BOTH, pady=5, padx = 5, expand=False)
button2 = Button(button1, text = "Exit", fg = 'white', bg = 'blue', relief = RAISED, font = ("arial",16, "bold"), command = exit1)
button2.pack(side= RIGHT, fill = NONE)

menu = Menu(window)
window.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label = "Exit", command=exit1)# don't add (),else it will be excuted immediatly

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label = "About", command= abt)
window.mainloop()





