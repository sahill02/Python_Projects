from tkinter import *

def login():
    username = entry1.get()
    password = entry2.get()
    # if username == "admin" and password == "1234":
    #     print("Login Successful!!")
    # else:
    #     print("Invalid username or password.")
    label4.config(text="Login Successful!!" if username == "admin" and password == "1234" else "Invalid username or password.")

root = Tk()
root.title("Login Page")
root.geometry("800x400")

root.configure(bg="#efe88f")

label = Label(root, text="Welcome to the Login Page", fg="#ff0000", bg="#80e2ec",font=("Kristen ITC", 24)).pack(pady=20)

label2 = Label(root, text="Enter Username:",fg="#040440", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry1 = Entry(root, font=("Arial", 10))
entry1.pack(pady=2)

label3 = Label(root, text="Enter Password:", fg="#040440", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry2 = Entry(root, font=("Arial", 10),)
entry2.pack(pady=2)

label4 = Label(root, text="",fg="red",bg="#efe88f" ,font=("Arial", 12))
label4.pack(pady=3)

Button(root, text="Login", command=login, font=("Fixedsys", 12), bg="blue", fg="white").pack(pady=20)

root.mainloop()