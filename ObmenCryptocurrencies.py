import requests
from tkinter import *
from tkinter import messagebox as mb

def exchange():
    code = entry.get()

    if code:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rete = data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rete} за 1 крипту")
            else:
                mb.showerror("Ошибка!", f"Криптавалюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", f"Введите код криптовалюты")

window = Tk()
window.title("Курс обмена криптовалют")
window.geometry("360x180")

Label(text="Введите код криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
#url = "https://api.coingecko.com/api/v3/exchange_rates"

#headers = {"accept": "application/json"}

#response = requests.get(url, headers=headers)

#p = pprint.PrettyPrinter(indent=4)

#p.pprint(response.text)

