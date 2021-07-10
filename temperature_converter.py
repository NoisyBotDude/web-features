from tkinter import *
import tkinter as tk

class MyWindow:
            def __init__(self, win):
                self.l1 = Label(win, text="Temperature In Celsius")
                self.l1.place(x=100, y=20)
                self.e1 = Entry()
                self.e1.place(x=200, y=20)
                self.l2 = Label(win, text="Temperature In Fahrenheit")
                self.l2.place(x=100, y=100)
                self.e2 = Entry()
                self.e2.place(x=200, y=100)
                self.l3 = Label(win, text="Temperature In Kelvin")
                self.l3.place(x=100, y=180)
                self.e3 = Entry()
                self.e3.place(x=200, y=180)
                self.btnc1 = Button(win, text="Change To Fahrenheit", fg="white", bg="black", command=self.change1)
                self.btnc1.place(x=100, y=60)
                self.btnc2 = Button(win, text="Change To Kelvin", fg="white", bg="black", command=self.change2)
                self.btnc2.place(x=250, y=60)
                self.btnc3 = Button(win, text="Change To Celsius", fg="white", bg="black", command=self.change3)
                self.btnc3.place(x=100, y=140)
                self.btnc4 = Button(win, text="Change To Kelvin", fg="white", bg="black", command=self.change4)
                self.btnc4.place(x=250, y=140)
                self.btnc5 = Button(win, text="Change To Celsius", fg="white", bg="black", command=self.change5)
                self.btnc5.place(x=100, y=220)
                self.btnc6 = Button(win, text="Change To Fahrenheit", fg="white", bg="black", command=self.change6)
                self.btnc6.place(x=250, y=220)

            def change1(self):
                self.e2.delete(0, 'end')
                num1 = float(self.e1.get())
                result = num1 * 1.8 + 32
                self.e2.insert(END, float(result))

            def change2(self):
                self.e3.delete(0, 'end')
                num1 = float(self.e1.get())
                result = num1 + 273.15
                self.e3.insert(END, float(result))

            def change3(self):
                self.e1.delete(0, 'end')
                num1 = float(self.e2.get())
                result = (num1 - 32) * 5 / 9
                self.e1.insert(END, float(result))

            def change4(self):
                self.e3.delete(0, 'end')
                num1 = float(self.e2.get())
                result = (num1 - 32) * 5 / 9 + 273.15
                self.e3.insert(END, float(result))

            def change5(self):
                self.e1.delete(0, 'end')
                num1 = float(self.e3.get())
                result = num1 - 273.15
                self.e1.insert(END, float(result))

            def change6(self):
                self.e2.delete(0, 'end')
                num1 = float(self.e3.get())
                result = (num1 - 273.15) * 1.8 + 32
                self.e2.insert(END, float(result))


window = tk.Tk()
mywin = MyWindow(window)
window.geometry("500x500")
window.title("Calculator")
window.mainloop()