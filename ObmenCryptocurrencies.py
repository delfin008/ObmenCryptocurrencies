from idlelib.pyshell import extended_linecache_checkcache

import requests
from tkinter import *
from tkinter import messagebox as mb


window = Tk()
window.title("Курс обмена криптовалют")
window.geometry("360x180")

Label(text="Введите код криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=extended).pack(padx=10, pady=10)

window.mainloop()
#url = "https://api.coingecko.com/api/v3/exchange_rates"

#headers = {"accept": "application/json"}

#response = requests.get(url, headers=headers)

#p = pprint.PrettyPrinter(indent=4)

#p.pprint(response.text)

