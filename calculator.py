from tkinter import *

def Button1():
    print("Button 1 clicked")
    data1 = int(entry1.get())
    data2 = int(entry2.get())
    result = data1 + data2 
    label4.config(text="Result: " + str(result))

def Button2():
    print("Button 2 clicked")
    data1 = int(entry1.get())
    data2 = int(entry2.get())
    result = data1 - data2
    label4.config(text="Result: " + str(result))

def Button3():
    print("Button 3 clicked")
    data1 = int(entry1.get())
    data2 = int(entry2.get())
    result = data1 * data2
    label4.config(text="Result: " + str(result))

def Button4():
    print("Button 4 clicked")
    data1 = int(entry1.get())
    data2 = int(entry2.get())
    result = data1 / data2
    label4.config(text="Result: " + str(result))


root = Tk()
root.title("Calculator")
root.geometry("800x500")
root.configure(bg="lightgray")  

label = Label(root, text="Welcome to the Calculator", font=("High Tower Text", 26),fg="black", bg="#fff200").pack(pady=12)


label2 = Label(root, text="Enter First number:", font=("Arial", 12), bg="lightgray").pack(pady=5)
entry1 = Entry(root, font=("Arial", 10))
entry1.pack(pady=5)


label3 = Label(root, text="Enter Second number:", font=("Arial", 12), bg="lightgray").pack(pady=5)
entry2 = Entry(root, font=("Arial", 10))
entry2.pack(pady=5)

label4 = Label(root, text="Result:__", font=("Arial", 12), bg="lightgray")
label4.pack(pady=10)


button1 = Button(root, text="Addition", command=Button1, bg="blue", fg="white", font=("Helvetica", 12))
button1.pack(pady=3)
button2 = Button(root, text="Subtraction", command=Button2, bg="green", fg="white", font=("Helvetica", 12))
button2.pack(pady=3)
button3 = Button(root, text="Multiplication", command=Button3, bg="red", fg="white", font=("Helvetica", 12))
button3.pack(pady=3)
button4 = Button(root, text="Division", command=Button4, bg="orange", fg="white", font=("Helvetica", 12))
button4.pack(pady=3)



root.mainloop()