#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
import tkinter.messagebox

root=tk.Tk()
root.title("Currency Conversion")



root.configure(bg = '#e6e5e5')
root.geometry("700x400")

headlabel = tk.Label(root,font=('lato black', 19,'bold'), text = '         Python Project   :    Currency Converter  ', bg= '#663300',fg='white') 
headlabel.grid(row=1, column=0,sticky=W)


variable1 = tk.StringVar(root) 
variable2 = tk.StringVar(root) 
 
variable1.set("currency") 
variable2.set("currency") 


    
CurrencyCode_list= ["INR","USD","CAD","CNY","DKK","EUR","AUD"]




def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c= CurrencyRates()
    
    from_cur= variable1.get();
    to_cur=variable2.get()
    
    if(Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Error!!  AMOUNT NOT ENTERED")
    elif(from_cur=="currency" or to_cur=="currency"):
        tkinter.messagebox.showinfo("Error!!  CURRENCY NOT SELECTED")
    else:
        new_amt= c.convert(from_cur,to_cur,float(Amount1_field.get()))
        Amount2_field.insert(0,str(new_amt))
        
        
def clear_all():
    Amount1_field.delete(0,tk.END)
    Amount2_field.delete(0,tk.END)

Label_1 =Label(root, font=('lato black', 27,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=1, column=0,sticky=W)


label1= tk.Label(root,font=('lato black',15,'bold'),text="\t  Amount :  ",bg="#e6e5e5", fg="black")
label1.grid(row=2,column=0,sticky=W)                 


label1= tk.Label(root,font=('lato black',15,'bold'),text="\t  From Currency  :  ",bg="#e6e5e5", fg="black")
label1.grid(row=3,column=0,sticky=W)     


label1= tk.Label(root,font=('lato black',15,'bold'),text="\t  To Currency  :  ",bg="#e6e5e5", fg="black")
label1.grid(row=4,column=0,sticky=W)     


label1= tk.Label(root,font=('lato black',15,'bold'),text="         Converted Amount :",bg="#e6e5e5", fg="black")
label1.grid(row=8,column=0,padx=2,sticky=W)   

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=5, column=0,sticky=W)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=7, column=0,sticky=W)




FromCurrency_option= tk.OptionMenu(root,variable1,*CurrencyCode_list) 
ToCurrency_option= tk.OptionMenu(root,variable2,*CurrencyCode_list)

FromCurrency_option.grid(row=3,column=0,ipadx=45,sticky=E)  
ToCurrency_option.grid(row=4,column=0,ipadx=45,sticky=E)    

Amount1_field= tk.Entry(root)     
Amount1_field.grid(row=2,column=0,sticky=E)

Amount2_field= tk.Entry(root)
Amount2_field.grid(row=8,column=0,sticky=E)   


Label_9= Button(root,font=("arial",15,"bold"),text="  Convert  ",padx=2,pady=2,bg="#e6e5e5", fg="black",command= RealTimeCurrencyConversion)
Label_9.grid(row=6,column=0)

Label_1 =Label(root, font=('lato black', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black")
Label_1.grid(row=9, column=0,sticky=W)


Label_9= Button(root,font=("arial",15,"bold"),text="  Clear All ",padx=2,pady=2,bg="white", fg="red",command= clear_all)
Label_9.grid(row=10,column=0)


root.mainloop()


                
