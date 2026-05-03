import tkinter as tk
import math
window = tk.Tk() 

#window size and name
window.geometry("1112x600")
window.title("Make physics easy")

#window expansion control
window.minsize(1112, 600)
window.maxsize(1112, 600)

#claiming string variables to store value
result_var1 = tk.StringVar()
result_var2 = tk.StringVar()
result_var3 = tk.StringVar()
result_var4 = tk.StringVar()
result_var5 = tk.StringVar()
result_var6 = tk.StringVar()
#velocity stringvar
velocity1_var = tk.StringVar()
displacement_var = tk.StringVar()
time1_var = tk.StringVar()
#weight stringvar
weight_var = tk.StringVar()
mass1_var = tk.StringVar()
gravity_var = tk.StringVar()
#momentum stringvar
momentum_var = tk.StringVar()
mass2_var = tk.StringVar()
velocity2_var = tk.StringVar()
#speed stringvar
speed_var = tk.StringVar()
distance_var = tk.StringVar()
time2_var = tk.StringVar()
#pressure stringvar
pressure_var = tk.StringVar()
force_applied_var = tk.StringVar()
total_area_var = tk.StringVar()
#kinetic energy stringvar
kinetic_energy_var = tk.StringVar()
mass3_var = tk.StringVar()
velocity3_var = tk.StringVar()

#set the variables
result_var1.set("The answer: ")
result_var2.set("The answer: ")
result_var3.set("The answer: ")
result_var4.set("The answer: ")
result_var5.set("The answer: ")
result_var6.set("The answer: ")
#velocity set
velocity1_var.set("")
displacement_var.set("")
time1_var.set("")
#weight set
weight_var.set("")
mass1_var.set("")
gravity_var.set("")
#momentum set
momentum_var.set("")
mass2_var.set("")
velocity2_var.set("")
#speed set
speed_var.set("")
distance_var.set("")
time2_var.set("")
#pressure set
pressure_var.set("")
force_applied_var.set("")
total_area_var.set("")
#kinetic energy stringvar
kinetic_energy_var.set("")
mass3_var.set("")
velocity3_var.set("")

#functions that will perform calculations
def velocity(float_V1=(0.0),float_T1=(0.0),float_D=(0.0)):
     float_V1 = float(velocity1_var.get())
     float_T1 = float(time1_var.get())
     float_D= float(displacement_var.get())
     if float_D != (0.0) and float_T1 != (0.0):
         v1 = float_D/ float_T1
         result_var1.set("Velocity: {}".format(v1))

     elif float_V1 != (0.0) and float_T1 != (0.0):
         D = float_V1 * float_T1
         result_var1.set("Displacement: {}".format(D))

     elif float_D != (0.0) and float_V1 != (0.0):
         t1 = float_D / float_V1
         result_var1.set("Time: {}".format(t1))

def weight(float_Mass1=(0.0), float_G=(0.0),float_W=(0.0)): 
         float_W = float(weight_var.get())
         float_Mass1 = float(mass1_var.get())
         float_G= float(gravity_var.get())

         if float_W != (0.0) and float_G != (0.0):
             Mass1 = float_W/float_G
             result_var2.set("Mass: {}".format(Mass1))

         elif float_G != (0.0) and float_Mass1 != (0.0):
             W = float_Mass1 * float_G
             result_var2.set("Weight: {}".format(W))

         elif float_W != (0.0) and float_Mass1 != (0.0):
             G = float_W / float_Mass1
             result_var2.set("Gravity: {}".format(G))
    
def momentum(float_M=(0.0),float_Mass2=(0.0),float_V2=(0.0)):
     float_Mass2 = float(mass2_var.get())
     float_M = float(momentum_var.get())
     float_V2= float(velocity2_var.get())

     if float_Mass2 != (0.0) and float_V2 != (0.0):
         M = float_Mass2*float_V2
         result_var3.set("Momentum: {}".format(M))

     elif float_M != (0.0) and float_Mass2 != (0.0):
         v2 = float_M/float_Mass2
         result_var3.set("Velocity: {}".format(v2))

     elif float_M != (0.0) and float_V2 != (0.0):
         Mass2 = float_M / float_V2
         result_var3.set("Mass: {}".format(Mass2))

def speed(float_S=(0.0),float_T2=(0.0),float_Dis=(0.0)):
     float_S = float(speed_var.get())
     float_T2 = float(time2_var.get())
     float_Dis = float(distance_var.get())

     if float_S != (0.0)and float_T2 != (0.0):
         Dis = float_S*float_T2
         result_var4.set("Distance: {}".format(Dis))

     elif float_Dis != (0.0) and float_T2 != (0.0):
         S = float_Dis/float_T2
         result_var4.set("Speed: {}".format(S))

     elif float_Dis != (0.0) and float_S != (0.0):
         t2 = float_Dis / float_S
         result_var4.set("Time: {}".format(t2))

def pressure(float_P=(0.0),float_F=(0.0),float_A=(0.0)):
     float_P = float(pressure_var.get())
     float_F = float(force_applied_var.get())
     float_A = float(total_area_var.get())

     if float_P != (0.0) and float_A != (0.0):
         F = float_A*float_P
         result_var5.set("Force Applied: {}".format(F))

     elif float_F != (0.0) and float_A != (0.0):
         P = float_F/float_A
         result_var5.set("Pressure: {}".format(P))

     elif float_F != (0.0) and float_P != (0.0):
         A = float_F / float_P
         result_var5.set("Total Area: {}".format(A))

def kinetic_energy(float_K=(0.0),float_Mass3=(0.0),float_V3=(0.0)):

     float_K = float(kinetic_energy_var.get())
     float_Mass3 = float(mass3_var.get())
     float_V3 = float(velocity3_var.get())

     if float_K != (0.0) and float_Mass3 != (0.0):
         v3 = math.sqrt((2 * float_K) / float_Mass3)
         result_var6.set("Velocity: {}".format(v3))

     elif float_K != (0.0) and float_V3 != (0.0):
         Mass3 = (2 * float_K) / (float_V3 ** 2) 
         result_var6.set("Mass: {}".format(Mass3))

     elif float_Mass3 != (0.0) and float_V3!= (0.0):
         K = 0.5* float_Mass3 * float_V3
         result_var6.set("Kinetic Energy: {}".format(K))

def restart():
    result_var1.set("The answer: ")
    result_var2.set("The answer: ")
    result_var3.set("The answer: ")
    result_var4.set("The answer: ")
    result_var5.set("The answer: ")
    result_var6.set("The answer: ")

    velocity1_var.set("")
    displacement_var.set("")
    time1_var.set("")

    weight_var.set("")
    mass1_var.set("")
    gravity_var.set("")

    momentum_var.set("")
    mass2_var.set("")
    velocity2_var.set("")
 
    speed_var.set("")
    distance_var.set("")
    time2_var.set("")

    pressure_var.set("")
    force_applied_var.set("")
    total_area_var.set("")

    kinetic_energy_var.set("")
    mass3_var.set("")
    velocity3_var.set("")
    
#widgets
find_velocitylbl = tk.Label(window, bg= '#DCDCDC', fg= '#3D59AB', text= 'FIND VELOCITY, DISPLACEMENT OR TIME', font= ('calibre',13,'bold'))
find_weightlbl = tk.Label(window, bg= '#DCDCDC', fg= '#3D59AB', text= 'FIND WEIGHT, MASS OR GRAVITY', font= ('calibre',13,'bold'))
find_momentumlbl = tk.Label(window, bg= '#DCDCDC', fg= '#3D59AB', text= 'FIND MOMENTUM, MASS OR VELOCITY', font= ('calibre',13,'bold'))
find_speedlbl = tk.Label(window, bg= '#DCDCDC', fg= '#3D59AB', text= 'FIND SPEED, DICTANCE OR TIME', font= ('calibre',13,'bold'))
find_pressurelbl = tk.Label(window, bg= '#DCDCDC', fg= '#3D59AB', text= 'FIND PRESSURE, FORCE APPLIED OR AREA', font= ('calibre',13,'bold'))
find_kinetic_energylbl = tk.Label(window, bg= '#DCDCDC', fg= '#3D59AB', text= 'FIND KINETIC ENERGY, MASS OR VELOCITY', font= ('calibre',13,'bold'))

insert_valuelbl1 = tk.Label(window, text = 'Insert any 2 values and get the third value.', font= ('calibre',9,'bold'), fg= '#458B00')
insert_valuelbl2 = tk.Label(window, text = 'Insert any 2 values and get the third value.', font= ('calibre',9,'bold'), fg= '#458B00')
insert_valuelbl3 = tk.Label(window, text = 'Insert any 2 values and get the third value.', font= ('calibre',9,'bold'), fg= '#458B00')
insert_valuelbl4 = tk.Label(window, text = 'Insert any 2 values and get the third value.', font= ('calibre',9,'bold'), fg= '#458B00')
insert_valuelbl5 = tk.Label(window, text = 'Insert any 2 values and get the third value.', font= ('calibre',9,'bold'), fg= '#458B00')
insert_valuelbl6 = tk.Label(window, text = 'Insert any 2 values and get the third value.', font= ('calibre',9,'bold'), fg= '#458B00')


formula_v_lbl = tk.Label(window, fg= '#DC143C', text= 'Formula: Velocity = Displacement/Time', font= ('calibre',9,'bold'))
formula_W_lbl = tk.Label(window, fg= '#DC143C', text= 'Formula: Weight = Mass x Gravity', font= ('calibre',9,'bold'))
formula_M_lbl = tk.Label(window, fg= '#DC143C', text= 'Formula: Momentum = Mass x Velocity', font= ('calibre',9,'bold'))
formula_S_lbl = tk.Label(window, fg= '#DC143C', text= 'Formula: Speed = Distance/Time', font= ('calibre',9,'bold'))
formula_P_lbl = tk.Label(window, fg= '#DC143C', text= 'Formula: Pressure = Force applied/Total area', font= ('calibre',9,'bold'))
formula_K_lbl = tk.Label(window, fg= '#DC143C', text= 'Formula: Kinetic Energy = 0.5 x Mass x Velocity', font= ('calibre',9,'bold'))

velocity1_label = tk.Label(window, fg= '#000000', text= 'Velocity:', font=('calibre',12,'bold'))
velocity1_entry = tk.Entry(window,textvariable= velocity1_var, font=('calibre',11,'normal'))
velocity1_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
displacement_label = tk.Label(window, fg= '#000000', text = 'Displacement:', font= ('calibre',12,'bold'))
displacement_entry = tk.Entry(window,textvariable= displacement_var, font=('calibre',11,'normal'))
displacement_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
time1_label = tk.Label(window, fg= '#000000', text= 'Time:', font=('calibre',12,'bold'))
time1_entry = tk.Entry(window,textvariable= time1_var, font=('calibre',11,'normal'))
time1_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

weight_label = tk.Label (window, fg='#000000', text= 'Weight:', font=('calibre',12,'bold'))
weight_entry = tk.Entry(window,textvariable= weight_var, font=('calibre',11,'normal'))
weight_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
mass1_label = tk.Label(window, fg='#000000', text= 'Mass:', font=('calibre',12,'bold'))
mass1_entry = tk.Entry(window,textvariable= mass1_var, font=('calibre',11,'normal'))
mass1_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
gravity_label = tk.Label(window, fg='#000000', text= 'Gravity:', font=('calibre',12,'bold'))
gravity_entry = tk.Entry(window,textvariable= gravity_var, font=('calibre',11,'normal'))
gravity_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

momentum_label = tk.Label(window, fg='#000000', text= 'Momentum:', font=('calibre',12,'bold'))
momentum_entry = tk.Entry(window,textvariable= momentum_var, font=('calibre',11,'normal'))
momentum_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
mass2_label = tk.Label(window, fg='#000000', text= 'Mass:', font=('calibre',12,'bold'))
mass2_entry = tk.Entry(window,textvariable= mass2_var, font=('calibre',11,'normal'))
mass2_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
velocity2_label = tk.Label(window, fg= '#000000', text= 'Velocity:', font=('calibre',12,'bold'))
velocity2_entry = tk.Entry(window,textvariable= velocity2_var, font=('calibre',12,'normal'))
velocity2_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

speed_label = tk.Label(window, fg='#000000', text= 'Speed:', font=('calibre',12,'bold'))
speed_entry = tk.Entry(window,textvariable= speed_var, font=('calibre',11,'normal'))
speed_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
distance_label = tk.Label(window, fg='#000000', text= 'Distance:', font=('calibre',12,'bold'))
distance_entry = tk.Entry(window,textvariable= distance_var, font=('calibre',11,'normal'))
distance_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
time2_label = tk.Label(window, fg= '#000000', text= 'Time:', font=('calibre',12,'bold'))
time2_entry = tk.Entry(window,textvariable= time2_var, font=('calibre',11,'normal'))
time2_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

pressure_label = tk.Label(window, fg='#000000', text= 'Pressure:', font=('calibre',12,'bold'))
pressure_entry = tk.Entry(window,textvariable= pressure_var, font=('calibre',11,'normal'))
pressure_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
force_applied_label =tk.Label(window, fg='#000000', text= 'Force Applied:', font=('calibre',12,'bold'))
force_applied_entry = tk.Entry(window,textvariable= force_applied_var, font=('calibre',11,'normal'))
force_applied_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
total_area_label = tk.Label(window, fg= '#000000', text= 'Total Area:', font=('calibre',12,'bold'))
total_area_entry = tk.Entry(window,textvariable= total_area_var, font=('calibre',11,'normal'))
total_area_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

kinetic_energy_label = tk.Label(window, fg='#000000', text= 'Kinetic Energy:', font=('calibre',12,'bold'))
kinetic_energy_entry = tk.Entry(window,textvariable= kinetic_energy_var, font=('calibre',11,'normal'))
kinetic_energy_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
mass3_label =tk.Label(window, fg='#000000', text= 'Mass:', font=('calibre',12,'bold'))
mass3_entry = tk.Entry(window,textvariable= mass3_var, font=('calibre',11,'normal'))
mass3_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)
velocity3_label = tk.Label(window, fg= '#000000', text= 'Velocity:', font=('calibre',12,'bold'))
velocity3_entry = tk.Entry(window,textvariable= velocity3_var, font=('calibre',11,'normal'))
velocity3_entry.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2)

calculatebtn_V = tk.Button(window, bg='#36648B', fg= 'white', command= velocity,  font=("Helvetica", 12, "bold"), text = 'Calculate', relief="groove")
calculatebtn_V.config(highlightbackground = "#36648B", highlightcolor= "#36648B", highlightthickness=2)
calculatebtn_W = tk.Button(window, bg='#36648B', fg= 'white',command= weight, font=("Helvetica", 12, "bold"), text = 'Calculate', relief="groove")
calculatebtn_W.config(highlightbackground = "#36648B", highlightcolor= "#36648B", highlightthickness=2)
calculatebtn_M = tk.Button(window, bg='#36648B', fg= 'white',command= momentum, font=("Helvetica", 12, "bold"), text = 'Calculate', relief="groove")
calculatebtn_M.config(highlightbackground = "#36648B", highlightcolor= "#36648B", highlightthickness=2)
calculatebtn_S = tk.Button(window, bg='#36648B', fg= 'white',command= speed, font=("Helvetica", 12, "bold"), text = 'Calculate', relief="groove")
calculatebtn_S.config(highlightbackground = "#36648B", highlightcolor= "#36648B", highlightthickness=2)
calculatebtn_P = tk.Button(window, bg='#36648B', fg= 'white',command= pressure, font=("Helvetica", 12, "bold"), text = 'Calculate', relief="groove")
calculatebtn_P.config(highlightbackground = "#36648B", highlightcolor= "#36648B", highlightthickness=2)
calculatebtn_K = tk.Button(window, bg='#36648B', fg= 'white',command= kinetic_energy, font=("Helvetica", 12, "bold"), text = 'Calculate', relief="groove")
calculatebtn_K.config(highlightbackground = "#36648B", highlightcolor= "#36648B", highlightthickness=2) 


resultlbl1 = tk.Label(window, textvariable=result_var1, font=('calibre',11,'bold'), fg="#008080", bg="#C6E2FF")
resultlbl2 = tk.Label(window, textvariable=result_var2, font=('calibre',11,'bold'), fg="#008080", bg="#C6E2FF")
resultlbl3 = tk.Label(window, textvariable=result_var3, font=('calibre',11,'bold'), fg="#008080", bg="#C6E2FF")
resultlbl4 = tk.Label(window, textvariable=result_var4, font=('calibre',11,'bold'), fg="#008080", bg="#C6E2FF")
resultlbl5 = tk.Label(window, textvariable=result_var5, font=('calibre',11,'bold'), fg="#008080", bg="#C6E2FF")
resultlbl6 = tk.Label(window, textvariable=result_var6, font=('calibre',11,'bold'), fg="#008080", bg="#C6E2FF")

exitbtn = tk.Button(window, command=window.destroy, font=("Helvetica", "13", "bold"), text = "Exit", bg='black', fg='black') 
exitbtn.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2, relief="raised")
restartbtn = tk.Button(window, command=restart, font=("Helvetica", "13", "bold"), text = "Refresh", bg='black', fg='black')
restartbtn.config(highlightbackground = "black", highlightcolor= "black", highlightthickness=2, relief="raised")

#placing the widgets correctly in window
find_velocitylbl.place(x=25, y=25, width=320)
find_weightlbl.place(x=400, y=25, width=320)
find_momentumlbl.place(x=775, y=25, width=320)
find_speedlbl.place(x=25, y=300, width=320) 
find_pressurelbl.place(x=400, y=300, width=320)
find_kinetic_energylbl.place(x=775, y=300, width=320) 

insert_valuelbl1.place(x=25,y=50)
insert_valuelbl2.place(x=400,y=50)
insert_valuelbl3.place(x=775,y=50)
insert_valuelbl4.place(x=25,y=325)
insert_valuelbl5.place(x=400,y=325)
insert_valuelbl6.place(x=775,y=325)

formula_v_lbl.place(x=25, y=75)
formula_W_lbl.place(x=400, y=75)
formula_M_lbl.place(x=775, y=75)
formula_S_lbl.place(x=25, y=350)
formula_P_lbl.place(x=400, y=350)
formula_K_lbl.place(x=775, y=350)

velocity1_label.place(x=25, y=100)
velocity1_entry.place(x=140, y=100)
displacement_label.place(x=25, y=125)
displacement_entry.place(x=140, y=125)
time1_label.place(x=25, y=150)
time1_entry.place(x=140, y=150)

weight_label.place(x=400, y=100)
weight_entry.place(x=515, y=100)
mass1_label.place(x=400, y=125)
mass1_entry.place(x=515, y=125)
gravity_label.place(x=400, y=150)
gravity_entry.place(x=515, y=150)

momentum_label.place(x=775, y=100)
momentum_entry.place(x=890, y=100)
mass2_label.place(x=775, y=125)
mass2_entry.place(x=890, y=125)
velocity2_label.place(x=775, y=150)
velocity2_entry.place(x=890, y=150, width=150)

speed_label.place(x=24, y=375)
speed_entry.place(x=120, y=375)
distance_label.place(x=25, y=400)
distance_entry.place(x=120, y=400)
time2_label.place(x=25, y=425)
time2_entry.place(x=120, y=425)

pressure_label.place(x=400, y=375)
pressure_entry.place(x=496, y=375)
force_applied_label.place(x=400, y=400)
force_applied_entry.place(x=496, y=400)
total_area_label.place(x=400, y=425)
total_area_entry.place(x=496, y=425)

kinetic_energy_label.place(x=775, y=375)
kinetic_energy_entry.place(x=871, y=375)
mass3_label.place(x=775, y=400)
mass3_entry.place(x=871, y=400)
velocity3_label.place(x=775, y=425)
velocity3_entry.place(x=871, y=425)

calculatebtn_V.place(x=140, y=200, width=150)
calculatebtn_W.place(x=515, y=200, width=150)
calculatebtn_M.place(x=890, y=200, width=150)
calculatebtn_S.place(x=120, y=475, width=150)
calculatebtn_P.place(x=495, y=475, width=150)
calculatebtn_K.place(x=870, y=475, width=150)


resultlbl1.place(x=25, y=230)
resultlbl2.place(x=400, y=230)
resultlbl3.place(x=775, y=230)
resultlbl4.place(x=25, y=505)
resultlbl5.place(x=400, y=505)
resultlbl6.place(x=775, y=505)

exitbtn.place(x=556, y=550)
restartbtn.place(x=480, y=550)

window.mainloop()