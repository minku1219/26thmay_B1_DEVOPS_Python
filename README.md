## Task Menu.py ##



```
import time
import os
import getmac


user_input='''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
Press 6 to Restart Your current OS :- 
Press 7 to Print list of all available Wifi in your laptop Range :-
Press 8 to RUn another code in Your current folder  :-  
'''
while(True):
    print(user_input)
    # to accept input from user 
    user_choice=input("Input Valid Choice")
    # printing user input 
    print("user has entered ",user_choice)

    if  user_choice ==  '1' :
        print("Current date and Time is: ",time.ctime())
        
    elif  user_choice  ==  '2' :
        print("Checking RAM Size of Your current OS: ")
        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
        mem_gib = mem_bytes/(1024.**3)
        print(mem_gib)

    elif  user_choice  ==  '3' :
        print("Name of Your current OS is: ",os.system('cat /etc/os-release'))
        
    elif user_choice == '4':
        print(getmac.get_mac_address())

    elif user_choice == '5':
        print("Creating one Directory in your Desktop: ")
        name=input("Enter The Name of Directory: ")
        path="/home/harrypotter/Desktop/"+name
        os.mkdir(path)

    elif user_choice == '6':
        print("Restarting Your current OS in 5 Seconds: ")
        print(os.system('shutdown -r now'))

    elif user_choice == '7':
        print("Printing list of all available Wifi in your laptop Range: ")
        print(os.system('nmcli dev wifi'))

    elif user_choice == '8':
        print("Running Another Code in Your Current Folder: ")
        print(os.system('python3 list.py'))

    elif user_choice == '9':
        exit()
    else :
        print("Please Enter a Valid Choice: ")

```


