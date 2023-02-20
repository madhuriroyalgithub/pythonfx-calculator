from forex_python.converter import CurrencyRates
from tkinter import *

c = CurrencyRates()


root = Tk()
root.title('Currency Converter')
root.geometry('672x490')
root.iconbitmap(r'C:\Users\User\Desktop\taskk\money.ico')
root.configure(bg='gray53')

supported_cur = \
"""
EUR - Euro Member Countries
IDR - Indonesia Rupiah
BGN - Bulgaria Lev
ILS - Israel Shekel
GBP - United Kingdom Pound
DKK - Denmark Krone
CAD - Canada Dollar
JPY - Japan Yen
HUF - Hungary Forint
RON - Romania New Leu
MYR - Malaysia Ringgit
SEK - Sweden Krona
SGD - Singapore Dollar
HKD - Hong Kong Dollar
AUD - Australia Dollar
CHF - Switzerland Franc
KRW - Korea (South) Won
CNY - China Yuan Renminbi
TRY - Turkey Lira
HRK - Croatia Kuna
NZD - New Zealand Dollar
THB - Thailand Baht
USD - United States Dollar
NOK - Norway Krone
RUB - Russia Ruble
INR - India Rupee
MXN - Mexico Peso
CZK - Czech Republic Koruna
BRL - Brazil Real
PLN - Poland Zloty
PHP - Philippines Peso
ZAR - South Africa Rand
"""


def calculate():
    am = amount_ent.get()
    for items in am:
        items.split('\n')

    first_rates = c.get_rates(ent_first_currency.get())
    for each_exch in first_rates:
        if each_exch == ent_second_currency.get():
            chosen_exch = first_rates[ent_second_currency.get()]  # Finds the exch rate dict_value attached to the dict_key defined in the []
            answer = format(float(am) * float(chosen_exch), ".2f")  # Calculate conversion to 2dp (.format())
            lab_answer = Label(root, bg='gray53', fg='blue', text=\
                str(ent_first_currency.get()) + ' >> '
                + str(answer) +
                ' >> ' + str(ent_second_currency.get())) # Label that displays the conversion
            lab_answer.place(x=277, y=360)  # Places above label on screen

def show_codes():
    codes = Tk()
    codes.title('Currency Codes')
    codes.iconbitmap(r'C:\Users\User\Desktop\taskk\money.ico')

    lab_cur_codes = Label(codes, text=supported_cur)
    lab_cur_codes.pack()

    codes.mainloop()

canvas = Canvas(root, width=250, height=250, bg='gray53', highlightthickness=0)
canvas.place(x=237, y=0)
img = PhotoImage(file='foreign_exchange.png')
canvas.create_image(0, 0, anchor=NW, image=img)

lab_amount = Label(root, text='Enter Amount')
lab_amount.place(x=291, y=220)
amount_ent = Entry(root, width=40)
amount_ent.place(x=213, y=250)


lab_first_currency = Label(root, text='Currency 1')
lab_first_currency.place(x=120, y=290)
ent_first_currency = Entry(root)
ent_first_currency.place(x=120, y=330)

btn_currency_arrows = Button(root, text='<<- calculate ->>',
                             command=calculate, borderwidth=5)
btn_currency_arrows.place(x=279, y=330)

lab_second_currency = Label(root, text='Currency 2')
lab_second_currency.place(x=420, y=290)
ent_second_currency = Entry(root)
ent_second_currency.place(x=420, y=330)

btn_show_codes = Button(root, text='Show Currency Codes',
                        command=show_codes, borderwidth=8)
btn_show_codes.place(x=266, y=425)

calculate()
root.mainloop()
