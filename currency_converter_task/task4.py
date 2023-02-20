from forex_python.converter import CurrencyRates
from tkinter import *


c = CurrencyRates()

usd_inr = c.get_rate('USD', 'INR')
inr_usd = c.get_rate('INR', 'USD')

gbp_eur = c.get_rate('GBP', 'EUR')
eur_gbp = c.get_rate('EUR', 'GBP')

usd_gbp = c.get_rate('USD', 'GBP')
gbp_usd = c.get_rate('GBP', 'USD')

usd_zar = c.get_rate('USD', 'ZAR')
zar_usd = c.get_rate('ZAR', 'USD')

aud_usd = c.get_rate('AUD', 'USD')
usd_aud = c.get_rate('USD', 'AUD')

choice_options = {
    'USD to INR': usd_inr,
    'INR to USD': inr_usd,
    'GBP to EUR': gbp_eur,
    'EUR to GBP': eur_gbp,
    'USD to GBP': usd_gbp,
    'GBP to USD': gbp_usd,
    'USD to ZAR': usd_zar,
    'ZAR to USD': zar_usd,
    'AUD to USD': aud_usd,
    'USD to AUD': usd_aud
}


def calculate():
    get_choice_value = choice_var.get()
    get_exch_rate = choice_options[get_choice_value]
    global exchange_result
    exchange_result = float(amount_entry.get()) * float(get_exch_rate)
    global exchange_result_Label
    exchange_result_Label = Label(root, fg='blue', bg='gray53',
                                  text=str(amount_entry.get()) + ' ' + str(choice_var.get()) + '   =   ' + str(
                                      exchange_result))
    exchange_result_Label.place(x=50, y=250)


root = Tk()
root.title('Currency Converter')
root.geometry('700x400')
root.iconbitmap(r'C:\Users\User\Desktop\taskk\money.ico')
root.configure(bg='gray53')

entry_Label = Label(root, text='Enter Amount')
entry_Label.place(x=50, y=50)

amount_entry = Entry(root, width=40, bd=6)
amount_entry.place(x=50, y=100)

choice_var = StringVar()
choice_var.set('Choose FOREX Pair')
choice = OptionMenu(root, choice_var, *choice_options.keys())
choice.place(x=50, y=150)

calculate_btn = Button(root, text='Calculate', command=calculate, pady=20, padx=20, bg='DarkSeaGreen4')
calculate_btn.place(x=50, y=200)

canvas = Canvas(root, width=250, height=250, bg='gray53', highlightthickness=0)
canvas.place(x=300, y=50)
img = PhotoImage(file='foreign_exchange.png')
canvas.create_image(50, 50, anchor=NW, image=img)


root.mainloop()
