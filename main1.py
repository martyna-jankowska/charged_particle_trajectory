import tkinter as tk


window = tk.Tk()

window.title("Dane")

q_lbl = tk.Label(window, text="q [C] = ")
q_lbl.grid(row=1, column=1)
q_entry = tk.Entry(window)
q_entry.grid(row=1, column=2)

m_lbl = tk.Label(window, text="m [kg] = ")
m_lbl.grid(row=2, column=1)
m_entry = tk.Entry(window)
m_entry.grid(row=2, column=2)

Ex_lbl = tk.Label(window, text="Ex [N/C] =  ")
Ex_lbl.grid(row=3, column=1)
Ex_entry = tk.Entry(window)
Ex_entry.grid(row=3, column=2)

Ey_lbl = tk.Label(window, text="Ey [N/C] = ")
Ey_lbl.grid(row=4, column=1)
Ey_entry = tk.Entry(window)
Ey_entry.grid(row=4, column=2)

Ez_lbl = tk.Label(window, text="Ey [N/C] = ")
Ez_lbl.grid(row=5, column=1)
Ez_entry = tk.Entry(window)
Ez_entry.grid(row=5, column=2)


Bx_lbl = tk.Label(window, text="Bx [T] =  ")
Bx_lbl.grid(row=6, column=1)
Bx_entry = tk.Entry(window)
Bx_entry.grid(row=6, column=2)

By_lbl = tk.Label(window, text="By [T] = ")
By_lbl.grid(row=7, column=1)
By_entry = tk.Entry(window)
By_entry.grid(row=7, column=2)

Bz_lbl = tk.Label(window, text="By [T] = ")
Bz_lbl.grid(row=8, column=1)
Bz_entry = tk.Entry(window)
Bz_entry.grid(row=8, column=2)


btn = tk.Button(window, text="Wyznacz", command="s")
window.mainloop()