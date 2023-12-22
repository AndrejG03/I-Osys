import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Walmart Input Output System")
root.geometry("300x250")  # Adjusted height to accommodate labels

# Function to update the combobox dropdown when typing
def on_type(event, values_list):
    widget = event.widget
    typed = widget.get()
    if typed:
        widget['values'] = [item for item in values_list if typed.lower() in item.lower()]
    else:
        widget['values'] = values_list
    widget.event_generate('<Down>')

# Departments list
departments = ['RX', 'FE', 'FS', 'TLE', 'SD', 'COS', 'LQR']
# Hardware types list
hardware_types = ['Debit Reader Lain 7000', 'Debit Reader Ingenico ISC 250', 
                  'Debit Reader MX915', 'Register Model A', 'Hand-held Scanner X']
# Problems list
problems_list = ['ICC not reading cards', 'MSR not reading cards', 'Debit reader broken']

# Function to process the input data and generate the output
def process_data():
    department = selected_department.get()
    hardware = selected_hardware.get()
    problem = selected_problem.get()
    output_text.set(f"{department} {hardware} {problem}")

# Layout configuration
root.columnconfigure(0, weight=1)

# Label and Dropdown for departments
tk.Label(root, text="1. Enter Department:").grid(column=0, row=0, padx=5, pady=2, sticky='w')
selected_department = tk.StringVar()
department_menu = ttk.Combobox(root, textvariable=selected_department, values=departments, width=15)
department_menu.bind('<KeyRelease>', lambda event: on_type(event, departments))
department_menu.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

# Label and Dropdown for hardware types
tk.Label(root, text="2. Enter Device:").grid(column=0, row=2, padx=5, pady=2, sticky='w')
selected_hardware = tk.StringVar()
hardware_type_menu = ttk.Combobox(root, textvariable=selected_hardware, values=hardware_types, width=25)
hardware_type_menu.bind('<KeyRelease>', lambda event: on_type(event, hardware_types))
hardware_type_menu.grid(column=0, row=3, padx=5, pady=5, sticky='ew')

# Label and Dropdown for problems
tk.Label(root, text="3. Enter Problem:").grid(column=0, row=4, padx=5, pady=2, sticky='w')
selected_problem = tk.StringVar()
problem_menu = ttk.Combobox(root, textvariable=selected_problem, values=problems_list, width=25)
problem_menu.bind('<KeyRelease>', lambda event: on_type(event, problems_list))
problem_menu.grid(column=0, row=5, padx=5, pady=5, sticky='ew')

# Button to generate output
process_button = tk.Button(root, text="Generate Output", command=process_data)
process_button.grid(column=0, row=6, padx=5, pady=5, sticky='ew')

# Output field
output_text = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_text, state='readonly', readonlybackground='white', fg='black')
output_entry.grid(column=0, row=7, padx=5, pady=5, sticky='ew')

# Run the application
root.mainloop()
