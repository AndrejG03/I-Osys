import tkinter as tk
from tkinter import ttk

# Kreirajte glavni prozor
root = tk.Tk()
root.title("Walmart Input Output System")

# Definišite raspored prozora
root.geometry("400x300")  # širina x visina

# Lista odeljenja
departments = ['RX', 'FE', 'FS', 'TLE', 'SD', 'COS', 'LQR']

# Kreirajte StringVar da drži izabrano odeljenje
selected_department = tk.StringVar()

# Kreirajte padajući meni za odeljenja sa omogućenim pretraživanjem
department_menu = ttk.Combobox(root, textvariable=selected_department, values=departments)
department_menu['state'] = 'readonly'  # Sprečava korisnika da unese vrednost koja nije na listi
department_menu.grid(column=0, row=0, padx=10, pady=10)

# Polje za unos broja kase
register_number_entry = tk.Entry(root)
register_number_entry.grid(column=0, row=1, padx=10, pady=10)

# Lista hardvera
hardware = ['Lain 7000', 'Ingenico ISC 250', 'MX915', 'Register Model A', 'Hand-held Scanner X']

# Kreirajte StringVar da drži izabrani hardver
selected_hardware = tk.StringVar()

# Kreirajte padajući meni za hardver sa omogućenim pretraživanjem
hardware_menu = ttk.Combobox(root, textvariable=selected_hardware, values=hardware)
hardware_menu['state'] = 'readonly'  # Sprečava korisnika da unese vrednost koja nije na listi
hardware_menu.grid(column=0, row=2, padx=10, pady=10)

# Lista problema - inicijalno prazna
problems = []

# Kreirajte StringVar da drži izabrani problem
selected_problem = tk.StringVar()

# Kreirajte padajući meni za probleme sa omogućenim pretraživanjem
problem_menu = ttk.Combobox(root, textvariable=selected_problem, values=problems)
problem_menu['state'] = 'readonly'  # Sprečava korisnika da unese vrednost koja nije na listi
problem_menu.grid(column=0, row=3, padx=10, pady=10)

# Funkcija za obradu unetih podataka i generisanje izlaza
def process_data():
    department = selected_department.get()
    register_number = register_number_entry.get()
    hw = selected_hardware.get()
    problem = selected_problem.get()
    output = f"{department} {register_number} {hw} {problem}"
    print(output)  # Ili ažurirajte ovu liniju da rukuje izlazom kako je potrebno

# Kreirajte dugme za aktiviranje obrade podataka
process_button = tk.Button(root, text="Generiši Izlaz", command=process_data)
process_button.grid(column=0, row=4, padx=10, pady=10)

# Funkcija za dodavanje problema u padajući meni
def add_problem():
    new_problem = problem_entry.get()
    if new_problem and new_problem not in problems:
        problems.append(new_problem)
        problem_menu['values'] = problems  # Ažurirajte opcije padajućeg menija
        selected_problem.set(new_problem)  # Postavite novododati problem kao trenutni izbor
        problem_entry.delete(0, tk.END)  # Očistite polje za unos

# Polje za unos da se doda novi problem
problem_entry = tk.Entry(root)
problem_entry.grid(column=0, row=5, padx=10, pady=10)

# Dugme za dodavanje novog problema na listu
add_problem_button = tk.Button(root, text="Dodaj Problem", command=add_problem)
add_problem_button.grid(column=0, row=6, padx=10, pady=10)

# Pokrenite aplikaciju
root.mainloop()
