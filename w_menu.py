def worker_menu():
    login_id='overseas123@bank.in'
    pwd='greenway1234'
    i=1
    f=open('Worker.txt','a')
    f.write('Name\t\t\t')
    f.write('Date & Time\t\t\t\t')
    f.write('Purpose\t\t\t\t')
    f.write('Amount Loaded \n')
    import time
    import datetime

    while i<4:
        
        ask=input('Enter login_id:')
        print()
        ask_1=input('Enter password:')
        print()
    
        if ask==login_id and ask_1==pwd:
            name=input("Enter your official name: ")
            f.write(name+'\t\t')
            dt=str(datetime.datetime.today())
            f.write(dt+'\t\t\t\t')
            time.sleep(2)
            print()
            print('''             MENU BAR
          PRESS 1 FOR "LOAD CASH"
          PRESS 2 FOR "MACHINE MAINTENANCE"
          PRESS 3 FOR "EXIT"''')
            print()
            choice_1=int(input('Enter your choice:'))
            print()

            if choice_1==1:
                print('Please wait...')
                print()
                f.write('Cash Loading'+'\t\t\t')

                time.sleep(5)

                print('''MACHINE has been turned off and cash loader is open now.
Please load the cash in the machine and close cash loader.''')

                time.sleep(2)
                print()

                print('''NOTE: The loader will be closed automatically after 5 minutes if not closed by
you before 5 minutes. So kindly do accordingly.''')

                print()
                print()
                time.sleep(5)

                from random import randint
                Rs=randint(50000,150000)
                Rs=round(Rs,-3)
                f.write(str(Rs)+'\n\n')
                print("₹ ",Rs," cash has been successfully loaded. ")
                print()
                print()
                time.sleep(5)

            elif choice_1==2:
                time.sleep(2)
                print(''' Machine will be turned off after 5 seconds.
Whenever the maintenance work is over kindly restart the machine. ''')
                time.sleep(5)
                f.write('Machine Maintenance'+'\t\t')
                f.write('NIL'+'\n\n')
                

            break

        else:
            print('Wrong id or password...')
            print('Please try again.')
            print('You have',3-i,'chances left')
            i+=1

    if i==4:
         print('''You have exceeded the number of login attempts.
                  Please try again later.''')
    f.close()
          
