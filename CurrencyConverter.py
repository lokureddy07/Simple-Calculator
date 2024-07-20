from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()

window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    try:
        amount = float(entry1.get())
        cur1 = entry2.get().upper()
        cur2 = entry3.get().upper()
        data = c.convert(amount, cur1, cur2)
        result_label.config(text=f"{amount} {cur1} is equal to {data:.2f} {cur2}", font="Times 16 bold")
    except Exception as e:
        result_label.config(text=f"Error: {e}", font="Times 16 bold")

tk.Label(window, text="Currency Converter", font="Times 20 bold").place(x=120, y=40)
tk.Label(window, text="Enter amount here:", font="Times 16 bold").place(x=70, y=100)
entry1 = tk.Entry(window)
tk.Label(window, text="Enter your currency here:", font="Times 16 bold").place(x=30, y=150)
entry2 = tk.Entry(window)
tk.Label(window, text="Enter your desired currency:", font="Times 16 bold").place(x=15, y=200)
entry3 = tk.Entry(window)

tk.Button(window, text="Click", font="Times 16 bold", command=clicked).place(x=220, y=250)

entry1.place(x=270, y=105)
entry2.place(x=270, y=155)
entry3.place(x=270, y=205)

result_label = tk.Label(window, text="", font="Times 16 bold")
result_label.place(x=200, y=300)

window.mainloop()
