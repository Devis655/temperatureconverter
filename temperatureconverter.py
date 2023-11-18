import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 9/5

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def kelvin_to_rankine(kelvin):
    return kelvin * 9/5

def rankine_to_celsius(rankine):
    return (rankine - 491.67) * 5/9

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

def rankine_to_kelvin(rankine):
    return rankine * 5/9

def convert_temperature():
    try:
        temperature = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == to_unit:
            result.set(f'{temperature:.2f} {to_unit}')
        elif from_unit == 'Celsius':
            result.set(f'{globals()[f"celsius_to_{to_unit.lower()}"](temperature):.2f} {to_unit}')
        elif from_unit == 'Fahrenheit':
            result.set(f'{globals()[f"fahrenheit_to_{to_unit.lower()}"](temperature):.2f} {to_unit}')
        elif from_unit == 'Kelvin':
            result.set(f'{globals()[f"kelvin_to_{to_unit.lower()}"](temperature):.2f} {to_unit}')
        elif from_unit == 'Rankine':
            result.set(f'{globals()[f"rankine_to_{to_unit.lower()}"](temperature):.2f} {to_unit}')
    except ValueError:
        result.set('Invalid input')

# Create the main window
window = tk.Tk()
window.title('Temperature Converter')

# Entry for user input
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, padx=10, pady=10)

# Dropdowns for temperature unit selection
temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine']
from_unit_var = tk.StringVar(value=temperature_units[0])
to_unit_var = tk.StringVar(value=temperature_units[1])

from_unit_dropdown = tk.OptionMenu(window, from_unit_var, *temperature_units)
from_unit_dropdown.grid(row=0, column=1, padx=10, pady=10)

to_unit_dropdown = tk.OptionMenu(window, to_unit_var, *temperature_units)
to_unit_dropdown.grid(row=0, column=2, padx=10, pady=10)

# Button to perform the conversion
convert_button = tk.Button(window, text='Convert', command=convert_temperature)
convert_button.grid(row=1, column=0, columnspan=3, pady=10)

# Display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
window.mainloop()
