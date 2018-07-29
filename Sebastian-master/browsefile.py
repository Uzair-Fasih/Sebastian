import tkinter as tk
from tkinter.filedialog import askopenfilename

def some_function():
    filename = askopenfilename()
    if filename:
        print("selected:", filename)
    else:
        print("file not selected")

mGui = tk.Tk()
browsebutton = tk.Button(mGui,text='Browse',command=some_function)
browsebutton.pack()

mGui.mainloop()




