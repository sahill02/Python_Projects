from tkinter import *

def registration():
    name=entry1.get()
    email=entry2.get()
    phone=entry3.get()
    password=entry4.get()

    if(name=="" or email=="" or phone=="" or password==""):
        label6.config(text="Please fill all the details.",bg="#faadda",fg="#FF0000",font=("Book Antiqua",16))
    else:
        label6.config(text="Registration Succesfully!!",bg="#ff0000",fg="#f7ff0b",font=("Book Antiqua",18))
def reset():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

root = Tk()
root.title("Registration Form")
root.geometry("700x500")
root.configure(bg="#faadda")

label = Label(root, text="Registration Form", fg="#050e49", bg="#faadda", font=("Berlin Sans FB", 28)).pack(pady=18)

label1 = Label(root, text="Full Name", fg="Black", bg="#faadda", font=("Candara", 13)).pack(pady=3)
entry1 = Entry(root, font=("Arial", 10))
entry1.pack(pady=3)

label2 = Label(root, text="Email", fg="Black", bg="#faadda", font=("Candara", 13)).pack(pady=3)
entry2 = Entry(root, font=("Arial", 10))
entry2.pack(pady=3)

label3 = Label(root, text="Phone Number", fg="Black", bg="#faadda", font=("Candara", 13)).pack(pady=3)
entry3 = Entry(root, font=("Arial", 10))
entry3.pack(pady=3)

label4 = Label(root, text="Password", fg="Black", bg="#faadda", font=("Candara", 13)).pack(pady=3)
entry4 = Entry(root, font=("Arial", 10), show="*")
entry4.pack(pady=3)

label6 = Label(root, text="", fg="#FC0000", bg="#faadda", font=("Candara", 13))
label6.pack(pady=3)

Button(root, text="REGISTRATION", command=registration, font=("Fixedsys", 12), bg="green", fg="white").pack(pady=7)
Button(root, text="RESET", command=reset, font=("Fixedsys", 12), bg="blue", fg="white").pack(pady=10)

root.mainloop()