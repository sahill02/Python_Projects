from tkinter import *

def crcl_area():
    print("Calculate area Button called successfully")
    r = int(entry.get())
    area = 3.14 * r * r
    message = "The area of circle is " + str(area)
    label.config(text=message)

def crcl_perimeter():
    print("Calculate perimeter Button called successfully")
    r = int(entry.get())
    perimeter = 2 * 3.14 * r
    message = "The perimeter of circle is " + str(perimeter)
    label.config(text=message)



root = Tk();
root.title("Tkinter Example")
root.geometry("800x500")

root.configure(bg="#efdf6b")

label = Label(root, text='Enter the radius of the circle :', bg="#54be12", fg='black', font=('High Tower Text', 20))
label.pack(pady=10)

entry = Entry(root, font=('Montserrat', 14))
entry.pack(pady=10)

Btnarea = Button(root, text='Area', command=crcl_area, bg='#ff0000', fg='white', font=('Helvetica', 16))
Btnarea.pack(pady=10)

Btnperimeter = Button(root, text='Perimeter', command=crcl_perimeter, bg='#ff0000', fg='white', font=('Helvetica', 16))
Btnperimeter.pack(pady=10)


root.mainloop()