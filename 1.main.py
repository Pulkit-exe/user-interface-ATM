def main():
    print('          Welcome to OVERSEAS BANK!!!!           ')

    import time
    time.sleep(2)
    a=input('              Press enter to continue            ')
    print()

    print('''          Press 1 if you are bank official
          Press 2 if you are customer         ''')
    print()
    choice=int(input("Enter your choice: "))
    print()
    if choice==1:
        from Banking import w_menu 
        w_menu.worker_menu()
    elif choice==2:
        from Banking import u_menu
        u_menu.user_menu()
    
main()    
    

