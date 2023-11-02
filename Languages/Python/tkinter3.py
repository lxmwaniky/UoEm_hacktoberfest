
#The program allows users to create account and log in to it, which is validated.
#The user has options to send money, withdraw money, deposit and take loans
#The program prompts the user to take a loan if they are trying to send or withdraw money which is more than their balance
#The python code below uses the sqlite3 library to manipulate a database with four tables
#The Users table has the user's name and password
#The Balance table has the user's name and corresponding balance. Default value is 0
#The message table has a message for a user informing him or her that they have received money from another user. The message is stored and automatically deleted when the user sees it
#The loans table stores the amount of loan a user has. Default value is 0
import sqlite3
import time
import tkinter as tk

window = tk.Tk()
window.geometry("500x820")
window.resizable(width= False, height = False)
window.configure(bg ="whitesmoke")

new_window = tk.Label(window, bg="green", width = 50, height = 25)
new_window.place(x=53, y=180)
new_window2 = tk.Label(window, bg="whitesmoke", width = 500, height = 820)


header = tk.Label(window, text="SILICON VALLEY BANK", bg="green", fg="White", width= 500, height = 2, font=("Roboto mono", 14))
header.pack()
def login1():
    number = numentry.get()
    name = nameentry.get()
    password = passentry.get()
    if len(str(number)) == 0 or len(name) == 0 or len(password) == 0:
        error = tk.Label(new_window, text="Fill out all fields", bg="green", fg="red", font=("Arial", 13))
        error.place(x=130, y=380)
    else:
        create_account(number, name, password)

def login2():
    number = numentry.get()
    name = nameentry.get()
    password = passentry.get()
    if len(str(number)) == 0 or len(name) == 0 or len(password) == 0:
        error = tk.Label(new_window, text="Fill out all fields", bg="green", fg="red", font=("Arial", 13))
        error.place(x=130, y=380)
    else:
        login_account(number, name, password)

def unplace(windownm, number, name):
    windownm.destroy()
    continuation(number, name)


def sendb(number, name):
    global new_window3
    def send2():
        usernum = number
        recipientnum = recipient.get()
        passwd2 = passwd.get()
        amount = amnt.get()
        send(usernum, amount, recipientnum, passwd2)
        login_account(number, name, passwd2)
        unplace(new_window3, number, name)

    new_window3 = tk.Label(new_window2, bg="yellow", width = 100, height = 14)
    new_window3.place(x=0, y=40)
    text = tk.Label(new_window3, text="SEND MONEY", bg="yellow", font=("Arial", 15))
    text.place(x=165, y=2)
    amnttext = tk.Label(new_window3, text="Amount: ", bg="yellow", font=("Arial", 15))
    amnttext.place(x=20, y=30)
    amnt = tk.Entry(new_window3, font=("Arial", 12))
    amnt.place(x=250, y=30)
    text2 = tk.Label(new_window3, text="Recipient Number: ", bg="yellow", font=("Arial", 15))
    text2.place(x=20, y=60)
    recipient = tk.Entry(new_window3, font=("Arial", 12))
    recipient.place(x=250, y=60)
    text3 = tk.Label(new_window3, text="Password: ", bg="yellow", font=("Arial", 15))
    text3.place(x=20, y=90)
    passwd = tk.Entry(new_window3, font=("Arial", 12), show="*")
    passwd.place(x=250, y=90)
    button = tk.Button(new_window3, text="Send", bg="red", fg="white", font=("Arial", 13), command=lambda: send2())
    button.place(x=340, y=120)
    button2 = tk.Button(new_window3, text="Cancel", bg="red", fg="white", font=("Arial", 13), command=lambda: unplace(new_window3, number, name))
    button2.place(x=20, y=120)

def logout():
    window.destroy()

def depositb(number, name):
    global new_window3
    def deposit3():
        usernum = number
        passwd2 = passwd.get()
        amount = amnt.get()
        deposit(amount, usernum, passwd2)
        login_account(number, name, passwd2)
        unplace(new_window3, number, name)

    new_window3 = tk.Label(new_window2, bg="yellow", width = 100, height = 14)
    new_window3.place(x=0, y=40)
    text = tk.Label(new_window3, text="DEPOSIT MONEY", bg="yellow", font=("Arial", 15))
    text.place(x=165, y=2)
    text1 = tk.Label(new_window3, text="Amount: ", bg="yellow", font=("Arial", 15))
    text1.place(x=20, y=30)
    amnt = tk.Entry(new_window3, font=("Arial", 12))
    amnt.place(x=250, y=30)
    text2 = tk.Label(new_window3, text="Password: ", bg="yellow", font=("Arial", 15))
    text2.place(x=20, y=90)
    passwd = tk.Entry(new_window3, font=("Arial", 12), show="*")
    passwd.place(x=250, y=90)
    
    button = tk.Button(new_window3, text="Deposit", bg="red", fg="white", font=("Arial", 13), command=deposit3)
    button.place(x=340, y=150)
    button2 = tk.Button(new_window3, text="Cancel", bg="red", fg="white", font=("Arial", 13), command=lambda: unplace(new_window3, number, name))
    button2.place(x=20, y=150)

def withdrawb(number, name):
    new_window3 = tk.Label(new_window2, bg="yellow", width = 100, height = 14)
    new_window3.place(x=0, y=40)
    text = tk.Label(new_window3, text="WITHDRAW MONEY", bg="yellow", font=("Arial", 15))
    text.place(x=165, y=2)
    text1 = tk.Label(new_window3, text="Amount: ", bg="yellow", font=("Arial", 15))
    text1.place(x=20, y=30)
    amnt = tk.Entry(new_window3, font=("Arial", 12))
    amnt.place(x=250, y=30)
    text2 = tk.Label(new_window3, text="Password: ", bg="yellow", font=("Arial", 15))
    text2.place(x=20, y=90)
    passwd = tk.Entry(new_window3, font=("Arial", 12), show="*")
    passwd.place(x=250, y=90)
    usernum = number
    passwd = passwd.get()
    amount = amnt.get()
    button = tk.Button(new_window3, text="Withdraw", bg="red", fg="white", font=("Arial", 13))
    button.place(x=340, y=150)
    button2 = tk.Button(new_window3, text="Cancel", bg="red", fg="white", font=("Arial", 13), command=lambda: unplace(new_window3, number, name))
    button2.place(x=20, y=150)

def loanb(number, name):
    new_window3 = tk.Label(new_window2, bg="yellow", width = 100, height = 14)
    new_window3.place(x=0, y=40)
    text = tk.Label(new_window3, text="TAKE LOAN", bg="yellow", font=("Arial", 15))
    text.place(x=165, y=2)
    text1 = tk.Label(new_window3, text="Amount: ", bg="yellow", font=("Arial", 15))
    text1.place(x=20, y=30)
    amnt = tk.Entry(new_window3, font=("Arial", 12))
    amnt.place(x=250, y=30)
    text2 = tk.Label(new_window3, text="Password: ", bg="yellow", font=("Arial", 15))
    text2.place(x=20, y=90)
    passwd = tk.Entry(new_window3, font=("Arial", 12), show="*")
    passwd.place(x=250, y=90)
    usernum = number
    passwd = passwd.get()
    amount = amnt.get()
    button = tk.Button(new_window3, text="Take Loan", bg="red", fg="white", font=("Arial", 13))
    button.place(x=340, y=150)
    button2 = tk.Button(new_window3, text="Cancel", bg="red", fg="white", font=("Arial", 13), command=lambda: unplace(new_window3, number, name))
    button2.place(x=20, y=150)

def accountdelb(number, name):
    new_window3 = tk.Label(new_window2, bg="yellow", width = 100, height = 14)
    new_window3.place(x=0, y=40)
    text = tk.Label(new_window3, text="DELETE ACCOUNT!", bg="yellow", font=("Arial", 15))
    text.place(x=165, y=2)
    text2 = tk.Label(new_window3, text="Password: ", bg="yellow", font=("Arial", 15))
    text2.place(x=20, y=90)
    passwd = tk.Entry(new_window3, font=("Arial", 12), show="*")
    passwd.place(x=250, y=90)
    usernum = number
    passwd = passwd.get()
    button = tk.Button(new_window3, text="Delete", bg="red", fg="white", font=("Arial", 13))
    button.place(x=340, y=150)
    button2 = tk.Button(new_window3, text="Cancel", bg="red", fg="white", font=("Arial", 13), command=lambda: unplace(new_window3, number, name))
    button2.place(x=20, y=150)

def continuation(number, username):
    new_label = tk.Label(new_window2, bg="whitesmoke", width = 70, height = 500)
    new_label.pack()
    cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (number,))
    balance = cursor.fetchall()
    error = tk.Label(new_label, text=f"Balance: \n{balance[0][0]}", bg="whitesmoke", fg="black", font=("Arial", 20))
    error.place(x = 40, y = 20)
    cursor.execute("SELECT Message FROM Messages WHERE Number LIKE (?)", (number,))
    messages = cursor.fetchall()
    for message in messages:
        messerror = tk.Label(new_label, text=f"Messages: \n{message[0]}", bg="whitesmoke", fg="black", font=("Arial", 13))
        messerror.place(x=40, y= 110)
        continue
 
    cursor.execute("DELETE FROM Messages WHERE Number LIKE (?)", (number,))
    cursor.execute("INSERT INTO Messages(Number, Message) VALUES(?, ?)", (number, " ",))
    cursor.execute("SELECT Loan FROM Loan WHERE Number LIKE (?)", (number,))
    loan = cursor.fetchall()
    error = tk.Label(new_label, text=f"Loans: \n{loan[0][0]}", bg="whitesmoke", fg="black", font=("Arial", 20))
    error.place(x = 340, y = 20)
    conn.commit()
    other_window = tk.Label(new_label, bg="green", fg="red", font=("Arial", 13), width= 40, height = 500)
    other_window.place(x=40, y=300)
    button1 = tk.Button(other_window, text="Send Money", bg="red", fg="white", font=("Arial", 13), width= 12, height = 2,command=lambda: sendb(number, username))
    button1.place(x=50, y=40)
    button2 = tk.Button(other_window, text="Deposit", bg="red", fg="white", font=("Arial", 13), width= 12, height = 2,command=lambda: depositb(number, username))
    button2.place(x=210, y=40)
    button3 = tk.Button(other_window, text="Withdraw", bg="red", fg="white", font=("Arial", 13), width= 12, height = 2,command=lambda: withdrawb(number, username))
    button3.place(x=50, y=140)
    button4 = tk.Button(other_window, text="Take Loan", bg="red", fg="white", font=("Arial", 13), width= 12, height = 2,command=lambda: loanb(number, username))
    button4.place(x=210, y=140)
    button5 = tk.Button(other_window, text="Delete account", bg="red", fg="white", font=("Arial", 13), width= 12, height = 2,command=lambda: accountdelb(number, username))
    button5.place(x=50, y=240)
    button6 = tk.Button(other_window, text="Log out", bg="red", fg="white", font=("Arial", 13), width= 12, height = 2, command=lambda: logout())
    button6.place(x=210, y=240)

def newwindow():
    global nameentry, passentry, numentry
    text = tk.Label(new_window, text="WELCOME TO SILICON BANK!", bg="green", fg="whitesmoke", font=("Arial", 15))
    text.place(x=50, y=20)
    text2 = tk.Label(new_window, text="Create account or login if you have one!", bg="green", fg="whitesmoke", font=("Arial", 13))
    text2.place(x=35, y=60)

    numlbl = tk.Label(new_window, text="NUMBER: ", bg="green", fg="whitesmoke", font=("Arial", 15))
    numlbl.place(x=40, y=150)
    numentry = tk.Entry(new_window, bg="Whitesmoke", fg="black", font=("Arial", 12))
    numentry.place(x=160, y=150)
    namelbl = tk.Label(new_window, text="NAME: ", bg="green", fg="whitesmoke", font=("Arial", 13))
    namelbl.place(x=40, y=200)
    nameentry = tk.Entry(new_window, bg="Whitesmoke", fg="black", font=("Arial", 12))
    nameentry.place(x=160, y=200)
    paswdlbl = tk.Label(new_window, text="PASSWORD: ", bg="green", fg="whitesmoke", font=("Arial", 13))
    paswdlbl.place(x=40, y=250)
    passentry = tk.Entry(new_window, bg="Whitesmoke", fg="black", font=("Arial", 12), show="*")
    passentry.place(x=160, y=250)

    buttoncreate = tk.Button(new_window, text="Create Account", bg="grey", fg="whitesmoke", command=login1)
    buttoncreate.place(x=55, y=330)
    buttonlog = tk.Button(new_window, text="     Login\t   ", bg="grey", fg="whitesmoke", command=login2)
    buttonlog.place(x=215, y=330)


#Create connection to database
conn = sqlite3.connect("bank.sqlite")

#create a cursor to help manipulate the database
cursor = conn.cursor()
#allow user to take loan if balance is too low
def take_loan(number):
    amount = input("Enter amount: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Number LIKE (?)", (number,))
    passwords = cursor.fetchall()
    for passwd in passwords:
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (number,))
            balance = cursor.fetchall()
            curr_balance = int(balance[0][0])
            cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (number,))
            new_balance = curr_balance + int(amount)
            cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (number, new_balance,))
            cursor.execute("SELECT Loan FROM Loan WHERE Number LIKE (?)", (number,))
            rec_loan = cursor.fetchall()
            cursor.execute("DELETE FROM Loan WHERE Number LIKE (?)", (number,))
            rec_new_loan = int(amount) + int(rec_loan[0][0])
            cursor.execute("INSERT INTO Loan(Number, Loan) VALUES(?, ?)", (number, rec_new_loan,))
            conn.commit()
            print(f"{amount} loan transferred successfully current balance is {new_balance}! \t\t\t\t")
            other_options(number, password)
        else:
            print("Invalid password or username!")
            other_options(number, password)

#Allows user to completely delete his account
def delete(number):
    print("WARNING YOU ARE TRYING TO DELETE YOUR ACCOUNT")
    print("Enter 1 to continue or 0 to terminate")
    choice = input(">> ")
    if choice == 1 or choice == '1':
        password = input("Enter your password: ")
        cursor.execute("SELECT Password FROM Users WHERE Number LIKE (?)", (number,))
        passwords = cursor.fetchall()
        for passwd in passwords:
            if passwd[0] == password:
                print("\t\t\t\t ***DELETING ACCOUNT*** \t\t\t\t\n")
                time.sleep(2)
                cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (number,))
                cursor.execute("DELETE FROM Loan WHERE Number LIKE (?)", (number,))
                cursor.execute("DELETE FROM Users WHERE Number LIKE (?)", (number,))
                cursor.execute("DELETE FROM Messages WHERE Number LIKE (?)", (number,))
                conn.commit()
                print("Account deleted successfully.")
            else:
                print("Invalid password or username!")
                delete(number)
    else:
        print("Process was terminated successfully!")
        other_options(number, password)

#allow the user to withdraw from the bank
def withdraw(number):
    amount = input("Enter the amount: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Number LIKE (?)", (number,))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (number,))
            balance = cursor.fetchall()
            curr_balance = int(balance[0][0])
            if curr_balance >= int(amount):
                cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (number,))
                new_balance = curr_balance - int(amount)
                cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (number, new_balance,))
                conn.commit()
                print(f"{amount} withdrawn successfully current balance is {new_balance}! \t\t\t\t")
                other_options(number, password)
            else:
                print("Your balance is too low!")
                print("1: Take loan")
                print("2: Back")
                choice = input("Choice: ")
                if choice == 1 or choice == '1':
                    take_loan(number)
                    withdraw(number)
                    other_options(number, password)
                else:
                    other_options(number, password)
        else:
            print("Invalid password or username!")
            other_options(number, password)

#give the user account statement
def balance(number):
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Number LIKE (?)", (number,))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (number,))
            balance = cursor.fetchall()
            print(f"Account balance: {balance[0][0]}")
            cursor.execute("SELECT Message FROM Messages WHERE Number LIKE (?)", (number,))
            messages = cursor.fetchall()
            for message in messages:
                print(f"Message: {message[0]}")
                cursor.execute("DELETE FROM Messages WHERE Number LIKE (?)", (number,))
                cursor.execute("INSERT INTO Messages(Number, Message) VALUES(?, ?)", (number, " ",))
                cursor.execute("SELECT Loan FROM Loan WHERE Number LIKE (?)", (number,))
                loan = cursor.fetchall()
                print(f"Loans: {loan[0][0]}")
                conn.commit()
                other_options(number, password)
        else: 
            print("Invalid username or password!")
            other_options(number, password)

#give the user an option to deposit money
def deposit(amnt, number, password):
    amount = int(amnt)
    password = password
    cursor.execute("SELECT Password FROM Users WHERE Number LIKE (?)", (number,))
    passwords = cursor.fetchall()
    for passwd in passwords:
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Loan FROM Loan WHERE Number LIKE (?)", (number,))
            rec_loan = cursor.fetchall()
            cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (number,))
            balance = cursor.fetchall()
            new_balance = int(balance[0][0]) + int(amount) - int(rec_loan[0][0])
            if new_balance > 0:
                cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (number,))
                cursor.execute("DELETE FROM Loan WHERE Number LIKE (?)", (number,))
                cursor.execute("INSERT INTO Loan(Number, Loan) VALUES(?, ?)", (number, 0,))
                cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (number, new_balance,))
                conn.commit()
                text1 = tk.Label(new_window3, text=f"{amount} deposited successfully \nnew balance = {new_balance}!!", bg="green", font=("Arial", 15))
                text1.place(x=60, y=180)
            elif new_balance < 0:
                cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (number,))
                cursor.execute("DELETE FROM Loan WHERE Number LIKE (?)", (number,))
                cursor.execute("INSERT INTO Loan(Number, Loan) VALUES(?, ?)", (number, (-1*new_balance),))
                cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (number, 0,))
                conn.commit()
                text1 = tk.Label(new_window3, text=f"{amount} deposited successfully \nnew balance = {new_balance}!!", bg="green", font=("Arial", 15))
                text1.place(x=60, y=180)
        else:
            print("Invalid password or username!")
            other_options(number, password)

def destroy(name):
    name.destroy()
#the user can send money to other users of the bank
def send(number, amnt, recipient, password):
    amount = int(amnt)
    recipient = int(recipient)
    password = password
    cursor.execute("SELECT Name, Password FROM Users WHERE Number LIKE (?)", (number,))
    passwords = cursor.fetchall()
    for passwd in passwords:
        if passwd[1] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (number,))
            balance = cursor.fetchall()
            curr_balance = int(balance[0][0])
            if curr_balance >= int(amount):
                cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (number,))
                new_balance = curr_balance - int(amount)
                cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (number, new_balance,))
                cursor.execute("SELECT Balance FROM Balance WHERE Number LIKE (?)", (recipient,))
                rec_balance = cursor.fetchall()
                rec_curr_balance = int(rec_balance[0][0])
                cursor.execute("SELECT Loan FROM Loan WHERE Number LIKE (?)", (recipient,))
                rec_loan = cursor.fetchall()
                cursor.execute("DELETE FROM Balance WHERE Number LIKE (?)", (recipient,))
                rec_new_balance = rec_curr_balance + int(amount) - int(rec_loan[0][0])
                if rec_new_balance > 0:
                    cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (recipient, rec_new_balance,))
                    cursor.execute("DELETE FROM Loan WHERE Number LIKE (?)", (recipient,))
                    cursor.execute("INSERT INTO Loan(Number, Loan) VALUES(?, ?)", (recipient, 0,))
                    cursor.execute("INSERT INTO Messages(Number, Message) VALUES(?, ?)", (recipient, f"You have received {amount} from {number } {passwd[0]} \nnew balance is: {rec_new_balance}",))
                    conn.commit()
                    text1 = tk.Label(new_window3, text=f"{amount} transferred successfully to {recipient}\n current balance is {new_balance}!", bg="green", font=("Arial", 15))
                    text1.place(x=80, y=180)
                    print("Done")
                elif rec_new_balance < 0:
                    cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (recipient, 0,))
                    cursor.execute("INSERT INTO Messages(Number, Message) VALUES(?, ?)", (recipient, f"You have received {amount} from {number} new balance is: {rec_new_balance}",))
                    cursor.execute("DELETE FROM Loan WHERE Number LIKE (?)", (recipient,))
                    cursor.execute("INSERT INTO Loan(Number, Loan) VALUES(?, ?)", (recipient, (-1*rec_new_balance),))
                    conn.commit()
                    text1 = tk.Label(new_window3, text=f"{amount} transferred successfully to {recipient}\n current balance is {new_balance}!", bg= "green", fg= "red", font=("Arial", 15))
                    text1.place(x=60, y=180)
                    print("Done")
            else:
                text1 = tk.Label(new_window3, text="Your balance is too low", bg="yellow", fg= "red", font=("Arial", 15))
                text1.place(x=60, y=180)
        else:
            text1 = tk.Label(new_window3, text="Invalid password!", bg="yellow", font=("Arial", 15), fg= "red")
            text1.place(x=60, y=180)


#Give user option to send money, deposit, withdraw and take loan
def other_options(number, password):
    print("\n1: Deposit")
    print("2: Send Money")
    print("3: Withdraw")
    print("4: Take loan")
    print("5: Show details")
    print("6: Log out")
    print("7: Delete account")
    choice = input("Choice: ")
    if choice == 1 or choice == '1':
        deposit(number)
    elif choice == 2 or choice == '2':
        send(number)
    elif choice == 3 or choice == '3':
        withdraw(number)
    elif choice == 4 or choice == '4':
        take_loan(number)
    elif choice == 5 or choice == '5':
        balance(number)
    elif choice == 6 or choice == '6':
        print("\t\t\t\t ***Logging out*** \t\t\t\t")
    elif choice == 7 or choice == '7':
        delete(number)
    else:
        print("Invalid input! Try again")
        other_options(number, password)

#Creating an account by adding name, password, balance to the database
def create_account(number, username, password):
    number = int(number)
    username = username.capitalize()
    password = password
    cursor.execute("SELECT Number FROM Users")
    numbers = cursor.fetchall()
    if (number,) in numbers:
        error = tk.Label(new_window, text="Account already exists! Try to log in", bg="green", fg="red", font=("Arial", 13))
        error.place(x=55, y=380)
        newwindow()
    
    else:
        print("\t\t\t\t ***Creating account*** \t\t\t\t\n")
        cursor.execute("INSERT INTO Users(Number, Name, Password) VALUES(?, ?, ?)", (number, username.capitalize(), password,))
        cursor.execute("INSERT INTO Messages(Number, Message) VALUES(?, ?)", (number, " ",))
        cursor.execute("INSERT INTO Loan(Number, Loan) VALUES(?, ?)", (number, 0,))
        cursor.execute("INSERT INTO Balance(Number, Balance) VALUES(?, ?)", (number, 0,))
        conn.commit()
    
        print("\t\t\t\t ***Account created successfully!*** \t\t\t\t\n")
        new_window2.pack()
        error = tk.Label(new_window2, text="Account created successfully!", bg="green", fg="whitesmoke", font=("Arial", 13), width=500)
        error.pack()
        continuation(number, username.capitalize())
        new_window.destroy()
        
    
#loggin in to the account and displaying the account detail balance, loan, message
def login_account(number, username, password):
    number = int(number)
    username = username.capitalize()
    password = password
    cursor.execute("SELECT Name, Number FROM Users")
    numbers = cursor.fetchall()
    print(numbers)
    if (username, number) in numbers:
        cursor.execute("SELECT Name, Password FROM Users WHERE Number LIKE (?)", (number,))
        passwords = cursor.fetchall()
        for passwd in passwords:
            if passwd[1] == password:
                print("\t\t\t\t ***Logging in*** \t\t\t\t\n")
                new_window2.pack()
                print(f"Welcome back {passwd[0]}! \t\t\t\t")

                error = tk.Label(new_window2, text=f"Welcome back {passwd[0]}!", bg="green", fg="whitesmoke", font=("Arial", 13), width = 50)
                error.pack()
                continuation(number, username.capitalize())
                new_window.destroy()
            else:
                error = tk.Label(new_window, text="Invalid password!", bg="green", fg="red", font=("Arial", 13))
                error.place(x=130, y=380)
                newwindow()
    else:
        error = tk.Label(new_window, text="Invalid Number or Name!", bg="green", fg="red", font=("Arial", 13))
        error.place(x=130, y=380)
        newwindow()



newwindow()
window.mainloop()
