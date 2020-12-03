print(" ----G Thirteen Banking System----       ")
def main():
   user_name = "Mohamed"
   Full_name = "Mohamed Guled"
   user_pin = "54354"
   MoneyinBank = 500
   x = ""
   pin_attempt = 1
   is_pin_locked = False

   print("Please, Select an option number")
   # This statement helps customers make a choice
   print("____ 0. Open a new account____")
   print("____ 1. For deposit____")
   print("____2. For withdrawal____")
   print("____3. View Balance____")
   print("____4. Check Interest Rate____")
   choiceIdea = input("Select your choice number from the above menu (just a number) : ")
   # The below statement is choice 1, creating a new bank account
   if choiceIdea == "0":
       name = input("Print Fullname : ")
       UserName = input("Create a username : ")
       ID = int(input("ID Number : "))
       Gender = input("Gender : ")
       DateOfBirth = input("Date of Birth : ")
       Pin = input("Please create a pin of your choice : ")
       Location = input("Enter your Full Address : ")
       Social_security = int(input("Last 4 digits of your SSN : "))
       print("Your name is added to customers system")
       print("----New account created successfully !----")
       print("Please remember the Name, username and Pin")

   # The below statement is choice 2, for customers to deposit money.
   elif choiceIdea == "1":
       print("Customer selected choice 1")
       print("Hello! Welcome to the Deposit option")
       UserName = input("username : ")
       name = input("Fullname : ")
       # This while loop protects the account for current users. The account will lock after 3 failed attempts
       while x != user_pin and not (is_pin_locked):
           # The account Allows 3 attempts
           if pin_attempt <= 3:
               x = input("Enter pin :")
               pin_attempt = pin_attempt + 1

           else:
               is_pin_locked = True
       # The account will lock after 3 failed attempts
       if is_pin_locked:
           print("Account locked")
           exit()
       else:
           print("Login is successful")
       # Can be deposited if pin is correct
       amount = float(input("Enter the amount to be Deposited: "))
       Total = MoneyinBank + amount
       print("Customer's name", name)
       print(" Amount Deposited", amount)
       print("         Total Amount:", Total)
   # The below statement is choice 3, for customers to withdraw money.
   elif choiceIdea == "2":
       print("Customer selected choice 2")
       print("Hello! Welcome to the Withdraw option")
       UserName = input("username : ")
       name = input("Fullname : ")
       # This while loop protects the account for current users. The account will lock after 3 failed attempts
       while x != user_pin and not (is_pin_locked):
           # The account Allows 3 attempts
           if pin_attempt <= 3:
               x = input("Enter pin :")
               pin_attempt = pin_attempt + 1

           else:
               is_pin_locked = True
       # The account will lock after 3 failed attempts
       if is_pin_locked:
           print("Account locked")
           exit()
       else:
           print("Login is successful")
       # Can be withdrawn after access
       amount = float(input("Enter the amount to be withdrawn: "))
       if amount <= MoneyinBank:
           balance = MoneyinBank - amount
           Total = MoneyinBank - amount
           print("Customer's name", name)
           print(" Amount withdrawn:", amount)
           print("    Total Amount :", Total)
       else:
           print("Insufficient Funds!")
           print("Amount to withdraw is larger than current balance")
           print("You have only", MoneyinBank)

   # The below statement is choice 4, for customers to view balance.
   elif choiceIdea == "3":
       print("Customer selected choice 3")
       print("Customer name and balances mentioned below : ")
       UserName = input("username : ")
       name = input("Fullname : ")
       # This while loop protects the account for current users. The account will lock after 3 failed attempts
       while x != user_pin and not (is_pin_locked):
           if pin_attempt <= 3:
               x = input("Enter pin :")
               pin_attempt = pin_attempt + 1


           else:
               is_pin_locked = True
       # The account will lock after 3 failed attempts
       if is_pin_locked:
           print("Account locked")
           exit()
       else:
           print("Login is successful")
       print("Customer's name", name)
       print("Balance is", MoneyinBank)
   elif choiceIdea == "4":
       # Assuming interest rate = 3%
       rate = 3
       print("Customer selected choice 4")
       print("Customer name and balances mentioned below : ")
       UserName = input("username : ")
       name = input("Fullname : ")
       # This while loop protects the account for current users. The account will lock after 3 failed attempts
       while x != user_pin and not (is_pin_locked):
           if pin_attempt <= 3:
               x = input("Enter pin :")
               pin_attempt = pin_attempt + 1

           else:
               is_pin_locked = True
       # The account will lock after 3 failed attempts
       if is_pin_locked:
           print("Account locked")
           exit()
       else :
           print("Login is successful")
       amount = MoneyinBank + (rate / 100) * MoneyinBank
       print("Customer's name", name)
       print("Balance is", MoneyinBank)
       print("Interest Rate of Bank is: 3%")
       print("After a year, the amount in bank will be: ", amount)
   # Allows customers to choose another option if they choose to
   restart = input('Would you like to make a transaction or check your balance? (If yes, type lowercase yes) ')
   if restart == "yes":
       main()
   else:
       print("Thank you for choosing us!")
       print("Have a nice day")
       exit()


main()
