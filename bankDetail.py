from tkinter import *
def bank_details():
    cardType=entry1.get()
    cardNumber=entry2.get()
    name=entry3.get()
    cvv=entry4.get()
    PIN=entry5.get()
    if(cardType.lower()=="debit"or cardType.lower()=="credit"):
        if(len(cardNumber)==16):
            if(len(name)!=0):
                if(len(cvv)==3 or len(cvv)==4):
                    if(len(PIN)>=4):
                        label7.config(text="Login Succesfully",bg="grey",fg="yellow",font=("Algerian",20))
                    else:
                        label7.config(text="Invalid pin")
                else:
                    label7.config(text="Enter valid CVV")
            else:
                label7.config(text="Enter your name")
        else:
            label7.config(text="Invalid card no.")
    else:
        label7.config(text="invalid card")


root = Tk()
root.title("First Class")
root.geometry("700x500")
root.configure(bg="#efe88f")

label = Label(root, text="Welcome to ATM", fg="#050e49", bg="#efe88f", font=("Kristen ITC", 24)).pack(pady=20)

label2 = Label(root, text="Enter card Type (debit/credit)", fg="Black", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry1 = Entry(root, font=("Arial", 10))
entry1.pack(pady=2)

label3 = Label(root, text="Enter Card Number", fg="Black", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry2 = Entry(root, font=("Arial", 10))
entry2.pack(pady=2)

label4 = Label(root, text="Enter Name", fg="Black", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry3 = Entry(root, font=("Arial", 10))
entry3.pack(pady=2)

label5 = Label(root, text="Enter CVV", fg="Black", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry4 = Entry(root, font=("Arial", 10))
entry4.pack(pady=2)

label6 = Label(root, text="Enter PIN", fg="Black", bg="#efe88f", font=("Leelawadee", 12)).pack(pady=3)
entry5 = Entry(root, font=("Arial", 10))
entry5.pack(pady=2)

Button(root, text="login", font=("Fixedsys", 12), bg="blue", fg="white", command=bank_details).pack(pady=20)

label7 = Label(root, text="", fg="#FC0000", bg="#efe88f", font=("Leelawadee", 12))
label7.pack(pady=3)


root.mainloop()