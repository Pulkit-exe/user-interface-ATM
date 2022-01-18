def user_menu():
    print('''          Welcome User
          Please insert your card to proceed further.''')
    print()

    import time
    import datetime
    time.sleep(3)

    import random
    f=open('User.txt','a')
    f.write('Account_no\t\t')
    f.write('Date & time\t\t')
    f.write('Type of transaction\n') 
    f.close()

    card_no=str(random.randint(300000000000,999999900000))
    card_no+='\t'

    while True:
        a="Your card has been successfully inserted"
        b="Please try one more time"
        c=random.choice([a,b])
        print(c)

        if c==a:
            pin=int(input("          Enter your card pin: "))
            print()
            print('''          Press 1 to "Withdraw Cash"
          Press 2 to "Deposit Cash"
          Press 3 for "Updation of mobile number" ''')
            break
        
        print()
        time.sleep(3)
    print()
    choice_2=int(input('          Enter your choice: '))
    print()
    balance=random.randint(5000,200000)    

    if choice_2==1: 
        print('''          NOTE:  The withdrawal amount should not exceed ₹ 20000 as per the guidelines issued by the RBI. ''')

        while True:
            withdrawal= int(input('          Enter amount: ₹'))
            print()
            

            if withdrawal > 20000:
                print('          The amount you exceeded is more than the specified amount.')

            else:
                if balance >= withdrawal:
                    f=open('User.txt','a')
                    wthdrw=str(withdrawal)+'  '
                    date=datetime.datetime.now()
                    date=str(date)+'\t\t'
                    f.write(card_no)
                    f.write(date)
                    f.write(wthdrw)
                    f.write('Dr\n\n')
                    f.close()

                    print()
                    print("           ₹", withdrawal,' has been debited from your account.')
                    print()
                    time.sleep(2)
                    print("          ₹",balance-withdrawal,' is the balance amount.')
                    print()
                    time.sleep(2)
                    print('          Thank you for using our services....')
                    print()
                    time.sleep(2)
                    print('          Please visit us again........')
                    print()
                    time.sleep(2)

                else:
                    print('Insufficient balance')

                break
            
    elif choice_2==2:
        deposit=int(input("          Enter the amount to be deposited : ₹"))
        dpsit=str(deposit)+'  '
        f=open('User.txt','a')
        date=datetime.datetime.now()
        date=str(date)+'\t\t'
        f.write(card_no)
        f.write(date)
        f.write(dpsit)
        f.write('Cr\n\n')
        f.close()

        print()
        time.sleep(2)
        print('          ₹',deposit,' has been successfully credited in your account.')
        print()
        time.sleep(2)
        print('          ₹',balance+deposit,' is the balance amount. ')
        print()
        time.sleep(2)
        print('          Thank you for using our services....')
        print()
        time.sleep(2)
        print('          Please visit us again........')
        print()
        time.sleep(2)

    elif choice_2==3:
        while True:
            n_m=int(input("Enter the Phone Number i.e. to be updated: "))
            
            n_m=str(n_m)
            print()

            if len(n_m)==10:
                f=open('User.txt','a')
                date=datetime.datetime.now()
                date=str(date)+'\t\t'
                f.write(card_no)
                f.write(date)
                f.write('Mobile number updated\n\n')
                f.close()

                break
            else:
                print("Please type the correct mobile number.")
                print()
                time.sleep(2)
                continue
        print()
        time.sleep(2)
        print("Please wait for a while we are updating our records.")
        time.sleep(2)
        print()
        print("Your mobile number has been successfully updated.")
        time.sleep(2)
        print()
        print('          Thank you for using our services....')
        print()
        time.sleep(2)
        print('          Please visit us again........')
        print()
        time.sleep(2)
        

        
        
        
        
         
        
        
        
    
          
