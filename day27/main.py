import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.geometry("800x600")

label = tk.Label(window, text="Olá, Braulio!", font=("Ubuntu", 24))
label.pack(pady=20)

def button_clicked():
    label.config(text="Botão Clicado!")

button = tk.Button(window, text="Clique Aqui", font=("Ubuntu", 16), command=button_clicked)
button.pack(pady=10)

input_field = tk.Entry(window, width=30)
input_field.pack(pady=10)
input_field.insert(0, "Digite algo aqui")

text_area = tk.Text(window, height=5, width=40)
text_area.pack(pady=10)
text_area.insert(tk.END, "Este é um campo de texto.\nVocê pode digitar várias linhas aqui.")

check_state = tk.IntVar()
check_button = tk.Checkbutton(window, text="Eu aceito os termos", variable=check_state)
check_button.pack(pady=10)

def show_selection():
    print(f"Checkbox selecionado: {check_state.get()}")
check_button.config(command=show_selection)

radio_var = tk.IntVar()
radio_var.set(1)

radio_button1 = tk.Radiobutton(window, text="Opção 1", variable=radio_var, value=1)
radio_button2 = tk.Radiobutton(window, text="Opção 2", variable=radio_var, value=2)
radio_button3 = tk.Radiobutton(window, text="Opção 3", variable=radio_var, value=3)
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

def show_radio_selection():
    print(f"Opção selecionada: {radio_var.get()}")
radio_button1.config(command=show_radio_selection)
radio_button2.config(command=show_radio_selection)
radio_button3.config(command=show_radio_selection)

def slider_changed(value):
    print(f"Slider value: {value}")
slider = tk.Scale(window, from_=0, to=100, orient="horizontal", command=slider_changed)
slider.pack(pady=10)

def spinbox_changed():
    print(f"Spinbox value: {spinbox.get()}")

spinbox = tk.Spinbox(window, from_=0, to=10, width=5, command=spinbox_changed)
spinbox.pack(pady=10)

listbox = tk.Listbox(window, height=5)
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

window.mainloop()


