import tkinter as tk
#from main2 import *

window = tk.Tk()
window.geometry("400x550")
window.title("Dane")
window["padx"] = 50
window["pady"] = 20
window.option_add("*Font", "24")

q_lbl = tk.Label(window, text="q [C] = ")
q_lbl.grid(row=1, column=1, pady=8)
q_entry = tk.Entry(window)
q_entry.grid(row=1, column=2, pady=8)

m_lbl = tk.Label(window, text="m [kg] = ")
m_lbl.grid(row=2, column=1, pady=8)
m_entry = tk.Entry(window)
m_entry.grid(row=2, column=2, pady=8)

Ex_lbl = tk.Label(window, text="Ex [N/C] =  ")
Ex_lbl.grid(row=3, column=1, pady=8)
Ex_entry = tk.Entry(window)
Ex_entry.grid(row=3, column=2, pady=8)

Ey_lbl = tk.Label(window, text="Ey [N/C] = ")
Ey_lbl.grid(row=4, column=1, pady=8)
Ey_entry = tk.Entry(window)
Ey_entry.grid(row=4, column=2, pady=8)

Ez_lbl = tk.Label(window, text="Ez [N/C] = ")
Ez_lbl.grid(row=5, column=1, pady=8)
Ez_entry = tk.Entry(window)
Ez_entry.grid(row=5, column=2, pady=8)

Bx_lbl = tk.Label(window, text="Bx [T] =  ")
Bx_lbl.grid(row=6, column=1, pady=8)
Bx_entry = tk.Entry(window)
Bx_entry.grid(row=6, column=2, pady=8)

By_lbl = tk.Label(window, text="By [T] = ")
By_lbl.grid(row=7, column=1, pady=8)
By_entry = tk.Entry(window)
By_entry.grid(row=7, column=2, pady=8)

Bz_lbl = tk.Label(window, text="Bz [T] = ")
Bz_lbl.grid(row=8, column=1, pady=8)
Bz_entry = tk.Entry(window)
Bz_entry.grid(row=8, column=2, pady=8)

vx_lbl = tk.Label(window, text="vx [m/s] =  ")
vx_lbl.grid(row=9, column=1, pady=8)
vx_entry = tk.Entry(window)
vx_entry.grid(row=9, column=2, pady=8)

vy_lbl = tk.Label(window, text="vy [m/s] = ")
vy_lbl.grid(row=10, column=1, pady=8)
vy_entry = tk.Entry(window)
vy_entry.grid(row=10, column=2, pady=8)

vz_lbl = tk.Label(window, text="vz [m/s] = ")
vz_lbl.grid(row=11, column=1, pady=8)
vz_entry = tk.Entry(window)
vz_entry.grid(row=11, column=2, pady=8)

btn = tk.Button(window, text="Wyznacz")
btn.grid(row=12, column=2, pady=8)



window.mainloop()