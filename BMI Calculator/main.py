import customtkinter
from tkinter import *
from tkinter import messagebox

app=customtkinter.CTk()
app.title('BMI Calculator')
app.geometry('450x450')
app.config(bg='#000')

f1=('Arial',30,'bold')
f2=('Arial',25,'bold')
f3=('Arial',25,'bold')

def calc_bmi():
    try:
        height=float(h.get())
        weight=float(w.get())
        if var2.get()=="ft":
            height*=30.48
        if var1.get()=="lbs":
            weight*=0.453592
        
        bmi=weight/((height/100)**2)
        rslt_lbl.configure(text="Your BMI is : {:.1f}".format(bmi))

        if bmi<18.5:
            rslt_lbl1.configure(text="Underweight")
        
        elif bmi>=25.0 and bmi<29.9:
            rslt_lbl1.configure(text="Overweight")
        
        elif bmi>=18.5 and bmi<24.9:
            rslt_lbl1.configure(text="Helthy Weight")
    
    except ValueError:
        messagebox.showerror('Error','Enter a Valid Number!')
    
    except ZeroDivisionError:
        messagebox.showerror('Error','Height cannot be 0!')



tlabel1 = customtkinter.CTkLabel(app,font=f1,text='BMI Calculator',text_color='#fff',bg_color='#000')
tlabel1.place(x=20,y=20)
tlabel2 = customtkinter.CTkLabel(app,font=f2,text='Weight',text_color='#fff',bg_color='#000')
tlabel2.place(x=20,y=80)
tlabel3 = customtkinter.CTkLabel(app,font=f3,text='Height',text_color='#fff',bg_color='#000')
tlabel3.place(x=20,y=150)

w=customtkinter.CTkEntry(app,font=f2,text_color='#000',fg_color='#fff',border_color='#fff')
w.place(x=20,y=110)
h=customtkinter.CTkEntry(app,font=f3,text_color='#000',fg_color='#fff',border_color='#fff')
h.place(x=20,y=180)

w_opt=['kg','lbs']
h_opt=['cm','ft']
var1=StringVar()
var2=StringVar()

w_opts = customtkinter.CTkComboBox(app,font=f2,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=w_opt,variable=var1,width=80)
w_opts.place(x=180,y=110)
w_opts.set('kg')
h_opts = customtkinter.CTkComboBox(app,font=f3,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=h_opt,variable=var2,width=80)
h_opts.place(x=180,y=180)
h_opts.set('cm')

cal_btn = customtkinter.CTkButton(app,command=calc_bmi,font=f2,text_color='#fff',text='Calculate',fg_color='#06911f',hover_color='#06911f',bg_color='#000',cursor='hand2',corner_radius=5,width=200)
cal_btn.place(x=50,y=230)

rslt_lbl = customtkinter.CTkLabel(app,text='',font=f3,text_color='#fff',bg_color='#000')
rslt_lbl.place(x=30,y=280)
rslt_lbl1 = customtkinter.CTkLabel(app,text='',font=f3,text_color='#fff',bg_color='#000')
rslt_lbl1.place(x=30,y=320)
app.mainloop()