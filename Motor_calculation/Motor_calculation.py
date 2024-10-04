from tkinter import *
#import tkinter as tk
from PIL import Image , ImageTk #pip install pillow
import tkinter.messagebox

window = Tk()
window.geometry("600x600")
window.title("Radioflyer motor selection tool v0.1")

img = Image.open("C:/Users/kzhou/Desktop/RF_projects/Git/Python_learning/Motor_calculation/Photo/Logo.png")
img1 = Image.open("C:/Users/kzhou/Desktop/RF_projects/Git/Python_learning/Motor_calculation/Photo/Incline.png")
img1 = img1.resize((700, 500))
photo = ImageTk.PhotoImage(img)
photo1 = ImageTk.PhotoImage(img1)

label = Label(image = photo)
label.pack()
image_label = Label(image= photo1)
image_label.place(x = 600, y=200)

bv          = IntVar()
max_weight  = DoubleVar()
wheel_size  = DoubleVar()
top_speed   = DoubleVar()
ramp_time   = DoubleVar()
gear_ratio  = DoubleVar()
incline_angle = DoubleVar()
var = StringVar()


def submit():
    #_____________Input_____________
    batvol=bv.get()
    maxweight = max_weight.get()
    wheelsize = wheel_size.get()
    topspeed  = top_speed.get()
    ramptime  = ramp_time.get()
    gearratio = gear_ratio.get()
    inclineangle = incline_angle.get()
    #_____________Output____________
    #	1. P=T*N/9554
	#2. T_motor = F*r / gear_ratio
	#3. F_total =  F_friction + F_inertia+F_gravity = 
	#                                        μ*mg （or μmg*sinθ）+ ma  + mgsinθ(if on a slop)    a=△V/t（m/s²）
    # P=T*N/9554 (or P = T*ω）
    # ω = v/r
    rpmvalue = topspeed/60/(3.1415926*wheelsize)*1000
    motor_rpm = rpmvalue*gearratio
    rpm.set(f"RPM:{rpmvalue:0.2f}/{motor_rpm:0.0f}")

    forcevalue = maxweight*((topspeed*1000/3600)/ramptime) #a is m/s
    torquevlue = forcevalue*wheelsize/2/gearratio
    powervalue = torquevlue*(rpmvalue*gearratio)/9554 #Or use formular P = t* w, the w is based on tire size, but this formular N means motor RPM
    torque.set(f"Torque:{torquevlue:0.4f}N*M")
    power.set(f"Power:{powervalue:0.4f}kW")








    
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

# Output_____________________________________________
torque = DoubleVar()
torque.set("Torque:")
output1 = Label(window, textvariable = torque)
output1.place(x=10, y=400)
Entry(window, textvariable= torque, state='readonly').place(x=10, y=400)

rpm = DoubleVar()
rpm.set("RPM:")
output2 = Label(window, textvariable = rpm)
output2.place(x=400, y=400)
Entry(window, textvariable= rpm, state='readonly').place(x=400, y=400)

power = DoubleVar()
power.set("Power:")
output3 = Label(window, textvariable = power)
output3.place(x=400, y=450)
Entry(window, textvariable= power, state='readonly').place(x=400, y=450)


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





