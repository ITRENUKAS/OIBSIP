import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert height to meters
        bmi = round(weight / (height ** 2), 2)

        result = f'Your BMI is: {bmi}\n'

        if bmi < 18.5:
            result += 'Category: Underweight'
        elif 18.5 <= bmi < 24.9:
            result += 'Category: Normal weight'
        elif 25 <= bmi < 29.9:
            result += 'Category: Overweight'
        else:
            result += 'Category: Obesity'

        result_label.config(text=result)
    except ValueError:
        result_label.config(text='Please enter valid numbers.')

# Create the main window
window = tk.Tk()
window.title('BMI Calculator')

# Create and place widgets
tk.Label(window, text='Weight (kg):').grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text='Height (cm):').grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text='Calculate BMI', command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text='')
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()