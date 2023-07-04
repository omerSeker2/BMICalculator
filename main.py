import tkinter

def calculateBMI():
    my_weight = weight_entry.get()
    my_height = height_entry.get()

    if my_weight == "" or my_height == "":
        result_label.config(text="Enter values.")
    else:
        try:
            bmi = float(my_weight) / pow(float(my_height)/100, 2)
            result_string = write_result(bmi)
            result_label.config(text=f"{result_string}")
        except:
            result_label.config(text="Enter a valid number.")

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=200)
window.config(padx=50, pady=25)

weight_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_label.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

height_label = tkinter.Label(text="Enter Your Height (cm)")
height_label.pack()

height_entry = tkinter.Entry()
height_entry.pack()

button = tkinter.Button(text="Calculate", command=calculateBMI)
button.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Your bmi {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severly thin."
    elif 16 < bmi <= 17:
        result_string += "moderately thin."
    elif 17 < bmi <= 18.5:
        result_string += "mild thin."
    elif 18.5 < bmi <= 25:
        result_string += "normal."
    elif 25 < bmi <= 30:
        result_string += "overweight."
    elif 30 < bmi <= 35:
        result_string += "obes."
    else:
        result_string += "too obes."
    return result_string

window.mainloop()