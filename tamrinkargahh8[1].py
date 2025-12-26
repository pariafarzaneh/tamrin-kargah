import tkinter as tk
from tkinter import messagebox

def calculate_share():
    try:
        total = float(entry_total.get())
        people = int(entry_people.get())
        if people == 0:
            raise ZeroDivisionError
        share = total / people
        messagebox.showinfo("Result", f"Each person pays: {int(share)} Toman")
    except ValueError:
        messagebox.showwarning("Error", "Please enter numbers only.")
    except ZeroDivisionError:
        messagebox.showwarning("Error", "Number of people can't be zero.")

# GUI setup
window = tk.Tk()
window.title("Dong Calculator")

tk.Label(window, text="Total Bill:").grid(row=0, column=0)
entry_total = tk.Entry(window)
entry_total.grid(row=0, column=1)

tk.Label(window, text="Number of People:").grid(row=1, column=0)
entry_people = tk.Entry(window)
entry_people.grid(row=1, column=1)

btn = tk.Button(window, text="Calculate Share", command=calculate_share)
btn.grid(row=2, columnspan=2, pady=10)

window.mainloop()