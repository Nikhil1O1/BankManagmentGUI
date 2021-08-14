#imports
from tkinter import *
import os
from PIL import ImageTk, Image

#main screen
master = Tk()
master.title('Bank app')

#functions
def finish_reg():
    name = tempName.get()
    age = tempAge.get()
    gender = tempGen.get()
    password = tempPass.get()
    all_account = os.listdir()
    if name == "" or age =="" or gender =="" or password =="":
        notif.config(fg="red",text="All fields required * ")
        return
    for name_check in all_account:
        if name == name_check:
            notif.config(fg="red",text="Account already exists ")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write("0")
            new_file.close()
            notif.config(fg="green",text="account created ")
    print("Succesfull")

    #print(all_account)
def register():
    #Var
    global tempName
    global tempAge
    global tempGen
    global tempPass
    global notif
    
    tempName = StringVar()
    tempAge = StringVar()
    tempGen = StringVar()
    tempPass = StringVar()
    #register screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="please enter your details below", font = ('calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font = ('calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font = ('calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font = ('calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font = ('calibri',12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font = ('calibri',12))
    notif.grid(row=6,sticky=N,pady =10)
    #Entries
    Entry(register_screen,textvar = tempName).grid(row=1,column=0)
    Entry(register_screen,textvar = tempAge ).grid(row=2,column=0)
    Entry(register_screen,textvar = tempGen).grid(row=3,column=0)
    Entry(register_screen,textvar = tempPass,show="*").grid(row=4,column=0)

    #Buttons
    Button(register_screen,text='Register', command = finish_reg,font = ('Calibri',12)).grid(row=5,sticky=N,pady=10)

def login_session():
    global login_name
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    #retreiving all names in the directory
    for name in all_accounts:
        if name ==login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                #Labels
                Label(account_dashboard, text = "Account_Dashboard",font = ('calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text = "Welcome"+ name,font = ('calibri',12)).grid(row=1,sticky=N,pady=5)
                #Button
                Button(account_dashboard, text = "Personal Details",font = ('Calibri',12),width=30,command = Personal_details).grid(row = 2,sticky = N,padx = 10)
                Button(account_dashboard, text = "Deposit",font = ('Calibri',12),width=30,command = Deposit).grid(row = 3,sticky = N,padx = 10)
                Button(account_dashboard, text = "Withdrawl",font = ('Calibri',12),width=30, command = Withdrawl).grid(row = 4,sticky = N,padx = 10)
                Label(account_dashboard).grid(row = 5,sticky = N,pady = 10)
                return

            else:
                login_notif.config(fg="red", text = "password incorrect!!")
            return
        
    login_notif.config(fg = "red", text = "No account found!!")


def Personal_details():
    #Vars
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    #Labels
    Label(personal_details_screen, text = "Personal Details",font = ('calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text = "Name : "+details_name ,font = ('calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen, text = "age : "+details_age,font = ('calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen, text = "gender : "+details_gender,font = ('calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen, text = "balance : "+details_balance,font = ('calibri',12)).grid(row=4,sticky=W)


def Deposit():
    #var
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    #label
    Label(deposit_screen, text="Deposit", font = ('Calibri', 12)).grid(row=0,sticky =N,pady = 10)
    current_balance_label = Label(deposit_screen, text="Current Balance : $"+ details_balance, font = ('Calibri', 12))
    current_balance_label.grid(row = 1,sticky = W)
    Label(deposit_screen,text = 'Amount :', font = ('Calibri', 12)).grid(row =2,sticky = W)
    deposit_notif = Label(deposit_screen,font = ('Calibri', 12))
    deposit_notif.grid(row = 4, sticky= N,pady = 5)
    #Entry
    Entry(deposit_screen, textvariable = amount).grid(row = 2,column = 1)
    #Button
    Button(deposit_screen, text = 'Finish', font=('Calibri', 12),command = finish_deposit).grid(row = 3,sticky=W,pady = 5)

def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text = "amount is required!",fg = "red")
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text = 'Negative currency is not accepted',fg = "red")
        return
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data = file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text = "current balance : $"+ str(updated_balance),fg = "green")
    deposit_notif.config(text = 'Balance Updated', fg = "green")


def Withdrawl():
    #var
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('withdraw')
    #label
    Label(withdraw_screen, text="Deposit", font = ('Calibri', 12)).grid(row=0,sticky =N,pady = 10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : $"+ details_balance, font = ('Calibri', 12))
    current_balance_label.grid(row = 1,sticky = W)
    Label(withdraw_screen,text = 'Amount :', font = ('Calibri', 12)).grid(row =2,sticky = W)
    withdraw_notif = Label(withdraw_screen,font = ('Calibri', 12))
    withdraw_notif.grid(row = 4, sticky= N,pady = 5)
    #Entry
    Entry(withdraw_screen, textvariable = withdraw_amount).grid(row = 2,column = 1)
    #Button
    Button(withdraw_screen, text = 'Finish', font=('Calibri', 12),command = finish_withdraw).grid(row = 3,sticky=W,pady = 5)

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text = "amount is required!",fg = "red")
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text = 'Negative currency is not accepted',fg = "red")
        return
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]

    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text = "insufficient_balance", fg = "red")
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance,str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text = "current balance : $"+ str(updated_balance),fg = "green")
    withdraw_notif.config(text = 'Balance Updated', fg = "green")




def login():
    #Var
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen 
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text = "Login to your account",font = ('Calibri',12)).grid(row = 0,sticky = N,pady = 10)
    Label(login_screen, text = "User Name",font = ('Calibri',12)).grid(row = 1,sticky =W)
    Label(login_screen, text = "Password",font = ('Calibri',12)).grid(row = 2,sticky =W)
    login_notif = Label(login_screen, font = ('Calibri',12))
    login_notif.grid(row = 4,sticky=N)
    #Entry
    Entry(login_screen, textvariable = temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable = temp_login_password,show = "*").grid(row=2,column=1,padx=5)

    #Button
    Button(login_screen, text="login",command = login_session,width = 15,font = ('Calibri',12)).grid(row = 3,sticky=W,pady = 5,padx = 5)



#image import
img = Image.open('secure.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#labels
Label(master, text = "Custom Banking Beta", font=('Calibri', 14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "Secure Bank", font=('Calibri', 12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2, sticky=N,pady=15)

#Buttons
Button(master, text = "Register", font = ('calibri',12),width=20,command = register).grid(row=3,sticky=N)
Button(master, text = "Login", font = ('calibri',12),width=20,command = login).grid(row=4,sticky=N,pady = 10)
master.mainloop()