# Miles to kilometers converter with user inpt and formatted output with tkinter

import tkinter as tk

def convert_miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_results_label.config(text=f"{km:.2f}")

window = tk.Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

miles_input = tk.Entry(window, width=10, border=1 )
miles_input.grid(column=1, row=0)

miles_label = tk.Label(window, text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(window, text="is equal to")
equal_label.grid(column=0, row=1)

km_results_label = tk.Label(window, text="0")
km_results_label.grid(column=1, row=1)

km_label = tk.Label(window, text="KM")
km_label.grid(column=2, row=1)

calculate_button = tk.Button(window, text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
