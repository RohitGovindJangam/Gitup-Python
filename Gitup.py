import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Git')

Name_Label = ttk.Label(root, text='Enter Your Name')
Name_Label.grid(row=0, column=0, sticky=tk.W)

Age_Label = ttk.Label(root, text='Enter Your Age')
Age_Label.grid(row=1, column=0, sticky=tk.W)

Gender_Label = ttk.Label(root, text='Select Your Gender')
Gender_Label.grid(row=2, column=0, sticky=tk.W)

Gender_Var = tk.StringVar()
Combo_Box = ttk.Combobox(root, width=14, textvariable=Gender_Var, state='readonly')
Combo_Box['values'] = ('Female', 'Male', 'Other')
Combo_Box.grid(row=2, column=1)

Name_Var = tk.StringVar()
Name_Enter = tk.Entry(root, width=16, textvariable=Name_Var)
Name_Enter.grid(row=0, column=1)
root.title('Git')
Name_Enter.focus()

Age_Var = tk.StringVar()
Age_Enter = ttk.Entry(root, width=16, textvariable=Age_Var)
Age_Enter.grid(row=1, column=1, pady=10)

Check_Var = tk.IntVar()
Check_Box = ttk.Checkbutton(root, text='Subscribe To Channel', variable=Check_Var)
Check_Box.grid(row=3, columnspan=2, pady=10)

Radio_Var = tk.StringVar()
Radio_Value = ttk.Radiobutton(root, text='Student', value='Student', variable=Radio_Var)
Radio_Value.grid(row=4, column=0, pady=10)

Radio_Value1 = ttk.Radiobutton(root, text='Teacher', value='Teacher', variable=Radio_Var)
Radio_Value1.grid(row=4, column=1)

def value():
    Name = Name_Var.get()
    Age = Age_Var.get()
    Gender = Gender_Var.get()
    Radio = Radio_Var.get()
    print(f'{Name}, {Age}, {Gender}')
    if Check_Var.get() == 0:
        Subscribed = 'No'
    else:
        Subscribed = 'Yes'
        print(f'{Radio}, {Subscribed}, {Gender}')
        with open('file.txt', 'a') as f:
            f.write(f'{Name}, {Age}, {Gender}, {Radio}, {Subscribed}\n')

        Name_Enter.delete(0, tk.END)
        Age_Enter.delete(0, tk.END)

Submit_Button = ttk.Button(root, text='Submit', command=value)
Submit_Button.grid(row=5, column=0)

tk.mainloop()
