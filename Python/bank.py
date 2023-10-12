#The code below uses python and the sqlite3 library to maipulate a database with four tables
#The tables include the Users table where it stores the username and the user's password
#It also has the message table which stores messages to inform a user that he/she has received money from a specified user. The message is later deleted after the user sees it.
#it also has a balance table where the user's account balance is stored
#Its also has a loan table where the user's loan is stored until repayment

#The python program allows a user to create an account, to log in once created, to send money to an existing user, to deposit money, to withdraw money and to take a loan.
#The user will also be prompted to take a loan when sending or withdrawing money if the balance is not enough.


import sqlite3
import time

#Create connection to database
conn = sqlite3.connect("bank.sqlite")

#create a cursor to help manipulate the database
cursor = conn.cursor()
#allow user to take loan if balance is too low
def take_loan(user):
    amount = input("Enter amount: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Name LIKE (?)", (user.capitalize(),))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
            balance = cursor.fetchall()
            curr_balance = int(balance[0][0])
            cursor.execute("DELETE FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
            new_balance = curr_balance + int(amount)
            cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (user.capitalize(), new_balance,))
            cursor.execute("SELECT Loan FROM Loan WHERE Name LIKE (?)", (user.capitalize(),))
            rec_loan = cursor.fetchall()
            cursor.execute("DELETE FROM Loan WHERE Name LIKE (?)", (user.capitalize(),))
            rec_new_loan = int(amount) + int(rec_loan[0][0])
            cursor.execute("INSERT INTO Loan(Name, Loan) VALUES(?, ?)", (user.capitalize(), rec_new_loan,))
            conn.commit()
            print(f"{amount} loan transferred successfully current balance is {new_balance}! \t\t\t\t")
            other_options(user, password)
        else:
            print("Invalid password or username!")
            other_options(user, password)

#allow the user to withdraw from the bank
def withdraw(user):
    amount = input("Enter the amount: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Name LIKE (?)", (user.capitalize(),))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
            balance = cursor.fetchall()
            curr_balance = int(balance[0][0])
            if curr_balance >= int(amount):
                cursor.execute("DELETE FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
                new_balance = curr_balance - int(amount)
                cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (user.capitalize(), new_balance,))
                conn.commit()
                print(f"{amount} withdrawn successfully current balance is {new_balance}! \t\t\t\t")
                other_options(user, password)
            else:
                print("Your balance is too low!")
                print("1: Take loan")
                print("2: Back")
                choice = input("Choice: ")
                if choice == 1 or choice == '1':
                    take_loan(user)
                    withdraw(user)
                    other_options(user, password)
                else:
                    other_options(user, password)
        else:
            print("Invalid password or username!")
            other_options(user, password)

#give the user account statement
def balance(user):
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Name LIKE (?)", (user.capitalize(),))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
            balance = cursor.fetchall()
            print(f"Account balance: {balance[0][0]}")
            cursor.execute("SELECT Message FROM Messages WHERE Name LIKE (?)", (user.capitalize(),))
            messages = cursor.fetchall()
            for message in messages:
                print(f"Message: {message[0]}")
                cursor.execute("DELETE FROM Messages WHERE Name LIKE (?)", (user.capitalize(),))
                cursor.execute("INSERT INTO Messages(Name, Message) VALUES(?, ?)", (user.capitalize(), " ",))
                cursor.execute("SELECT Loan FROM Loan WHERE Name LIKE (?)", (user.capitalize(),))
                loan = cursor.fetchall()
                print(f"Loans: {loan[0][0]}")
                conn.commit()
                other_options(user, password)
        else: 
            print("Invalid username or password!")
            other_options(user, password)

#give the user an option to deposit money
def deposit(user):
    amount = input("Enter the amount: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Name LIKE (?)", (user.capitalize(),))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Loan FROM Loan WHERE Name LIKE (?)", (user.capitalize(),))
            rec_loan = cursor.fetchall()
            cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
            balance = cursor.fetchall()
            new_balance = int(balance[0][0]) + int(amount) - int(rec_loan[0][0])
            if new_balance > 0:
                cursor.execute("DELETE FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
                cursor.execute("DELETE FROM Loan WHERE Name LIKE (?)", (user.capitalize(),))
                cursor.execute("INSERT INTO Loan(Name, Loan) VALUES(?, ?)", (user.capitalize(), 0,))
                cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (user.capitalize(), new_balance,))
                conn.commit()
                print(f"{amount} transferred successfully new balance = {new_balance}! \t\t\t\t")
                other_options(user, password)
            elif new_balance < 0:
                cursor.execute("DELETE FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
                cursor.execute("DELETE FROM Loan WHERE Name LIKE (?)", (user.capitalize(),))
                cursor.execute("INSERT INTO Loan(Name, Loan) VALUES(?, ?)", (user.capitalize(), (-1*new_balance),))
                cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (user.capitalize(), 0,))
                conn.commit()
                print(f"{amount} transferred successfully new balance = {new_balance}! \t\t\t\t")
                other_options(user, password)
        else:
            print("Invalid password or username!")
            other_options(user, password)

#the user can send money to other users of the bank
def send(user):
    amount = input("Enter the amount: ")
    recipient = input("Enter the recipient: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Name LIKE (?)", (user.capitalize(),))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            print("\t\t\t\t ***Depositing amount*** \t\t\t\t\n")
            time.sleep(2)
            cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
            balance = cursor.fetchall()
            curr_balance = int(balance[0][0])
            if curr_balance >= int(amount):
                cursor.execute("DELETE FROM Balance WHERE Name LIKE (?)", (user.capitalize(),))
                new_balance = curr_balance - int(amount)
                cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (user.capitalize(), new_balance,))
                cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (recipient.capitalize(),))
                rec_balance = cursor.fetchall()
                rec_curr_balance = int(rec_balance[0][0])
                cursor.execute("SELECT Loan FROM Loan WHERE Name LIKE (?)", (recipient.capitalize(),))
                rec_loan = cursor.fetchall()
                cursor.execute("DELETE FROM Balance WHERE Name LIKE (?)", (recipient.capitalize(),))
                rec_new_balance = rec_curr_balance + int(amount) - int(rec_loan[0][0])
                if rec_new_balance > 0:
                    cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (recipient.capitalize(), rec_new_balance,))
                    cursor.execute("DELETE FROM Loan WHERE Name LIKE (?)", (recipient.capitalize(),))
                    cursor.execute("INSERT INTO Loan(Name, Loan) VALUES(?, ?)", (recipient.capitalize(), 0,))
                    cursor.execute("INSERT INTO Messages(Name, Message) VALUES(?, ?)", (recipient.capitalize(), f"You have received {amount} from {user.capitalize()} new balance is: {rec_new_balance}",))
                    conn.commit()
                    print(f"{amount} transferred successfully to {recipient} current balance is {new_balance}! \t\t\t\t")
                elif rec_new_balance < 0:
                    cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (recipient.capitalize(), 0,))
                    cursor.execute("INSERT INTO Messages(Name, Message) VALUES(?, ?)", (recipient.capitalize(), f"You have received {amount} from {user.capitalize()} new balance is: {rec_new_balance}",))
                    cursor.execute("DELETE FROM Loan WHERE Name LIKE (?)", (recipient.capitalize(),))
                    cursor.execute("INSERT INTO Loan(Name, Loan) VALUES(?, ?)", (recipient.capitalize(), (-1*rec_new_balance),))
                    conn.commit()
                    print(f"{amount} transferred successfully to {recipient} current balance is {new_balance}! \t\t\t\t")
            else:
                print("Your balance is too low!")
                print("1: Take loan")
                print("2: Back")
                choice = input("Choice: ")
                if choice == 1 or choice == '1':
                    take_loan(user)
                    withdraw(user)
                    other_options(user, password)
                else:
                    other_options(user, password).
        else:
            print("Invalid password or username!")
            other_options(user, password)


#Give user option to send money, deposit, withdraw and take loan
def other_options(user, password):
    print("\n1: Deposit")
    print("2: Send Money")
    print("3: Withdraw")
    print("4: Take loan")
    print("5: Show details")
    print("6: Log out")
    choice = input("Choice: ")
    if choice == 1 or choice == '1':
        deposit(user)
    elif choice == 2 or choice == '2':
        send(user)
    elif choice == 3 or choice == '3':
        withdraw(user)
    elif choice == 4 or choice == '4':
        take_loan(user)
    elif choice == 5 or choice == '5':
        balance(user)
    elif choice == 6 or choice == '6':
        print("\t\t\t\t ***Logging out*** \t\t\t\t")
        main()
    else:
        print("Invalid input! Try again")
        other_options(user, password)

#Creating an account by adding name, password, balance to the database
def create_account():
    username = input("Enter your name: ")
    password = input("Enter your desired password: ")
    print("\t\t\t\t ***Creating account*** \t\t\t\t\n")
    cursor.execute("INSERT INTO Users(Name, Password) VALUES(?, ?)", (username.capitalize(), password,))
    cursor.execute("INSERT INTO Messages(Name, Message) VALUES(?, ?)", (username.capitalize(), " ",))
    cursor.execute("INSERT INTO Loan(Name, Loan) VALUES(?, ?)", (username.capitalize(), 0,))
    cursor.execute("INSERT INTO Balance(Name, Balance) VALUES(?, ?)", (username.capitalize(), 0,))
    conn.commit()
    time.sleep(2)
    print("\t\t\t\t ***Account created successfully!*** \t\t\t\t\n")
    other_options(username.capitalize(), password)
    
#loggin in to the account and displaying the account detail balance, loan, message
def login_account():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT Password FROM Users WHERE Name LIKE (?)", (username.capitalize(),))
    passwords = cursor.fetchall()
    for passwd in passwords:
        print(passwords)
        if passwd[0] == password:
            print("\t\t\t\t ***Logging in*** \t\t\t\t\n")
            time.sleep(2)

            print(f"Welcome back {username.capitalize()}! \t\t\t\t")
            cursor.execute("SELECT Balance FROM Balance WHERE Name LIKE (?)", (username.capitalize(),))
            balance = cursor.fetchall()
            print(f"Account balance: {balance[0][0]}")
            cursor.execute("SELECT Message FROM Messages WHERE Name LIKE (?)", (username.capitalize(),))
            messages = cursor.fetchall()
            for message in messages:
                print(f"Message: {message[0]}")
                continue
            cursor.execute("DELETE FROM Messages WHERE Name LIKE (?)", (username.capitalize(),))
            cursor.execute("INSERT INTO Messages(Name, Message) VALUES(?, ?)", (username.capitalize(), " ",))
            cursor.execute("SELECT Loan FROM Loan WHERE Name LIKE (?)", (username.capitalize(),))
            loan = cursor.fetchall()
            print(f"Loans: {loan[0][0]}")
            conn.commit()
        else:
            print("Invalid password or username!")
            main()
    other_options(username.capitalize(), password)


#The main function that begins the whole program
def main():
    print("\n\t\t\t\t ***SILICON VALLEY BANK**** \t\t\t\t")
    print("\n")
    print("1: Create account")
    print("2: Log in")
    print("00: Quit")
    main_choice = input("Choice: ")
    if main_choice == 1 or main_choice == '1':
        create_account()
    elif main_choice == 2 or main_choice == '2':
        login_account()
    elif main_choice == 00 or main_choice == '00':
        return
    else:
        print("Invalid input. Try again!")
        main()

main()
