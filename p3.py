from tkinter import *
from tkinter import messagebox


def convert_temp():
	temp_str = entry_temp.get()
	
	if not temp_str:
		messagebox.showerror("Input Error", "Please enter a temperature value.")
		return

	

	try:
		temp_val = float(temp_str)
	except ValueError:
		messagebox.showerror("Input Error", "Please enter a valid numeric value.")
		return
	
		
	conversion_type = var_conversion.get()
	if conversion_type == 0:
		messagebox.showerror("Selection Error", "Please select a conversion type.")
		return

	if conversion_type == 1:
	
		result = (temp_val * 9/5)  + 32
		lbl_result.config(text=f"Result: {result:.2f} °F")
	elif conversion_type == 2:
		result = (temp_val - 32) * 5/9
		lbl_result.config(text=f"Result: {result:.2f} °C")	
root = Tk()
root.title("Temperature Converter")
root.geometry("900x400+400+400")
f = ("Arial",40,"bold")

lbl_title = Label(root, text="Temperature Converter", font = f)
lbl_title.pack(pady=10)

lbl_enter = Label(root, text="Enter Temperature:")
lbl_enter.pack()
entry_temp = Entry(root)
entry_temp.pack(pady=5)


var_conversion = IntVar()
var_conversion.set(0)



lbl_select = Label(root,text="Select One:")
lbl_select.pack()

rb_cel_to_fah = Radiobutton(root,text="Celsius to Fahrenheit", variable=var_conversion, value=1)
rb_cel_to_fah.pack()



rb_fah_to_cel = Radiobutton(root,text="Fahrenheit to Celsius", variable=var_conversion, value=2)
rb_fah_to_cel.pack()


btn_convert = Button(root, text="Convert", command=convert_temp)
btn_convert.pack(pady=10)

lbl_result = Label(root, text="Result: --",)
lbl_result.pack(pady=5)























root.mainloop()