## Code to Talk to Terminal



```
import subprocess
while(True):
    print("Press ctrl+c to Exit from Code")
    n=input("Enter the Command: $ ")
    s=subprocess.getstatusoutput(n)
    if (n.isdigit()==True):
        print(int(n)*2)
    elif(s[0]==0):
        op=subprocess.getstatusoutput(n)
        if(op[0]==0):
            print(op[1]);
    else:
        re=n.replace(" ",'+')
        print(subprocess.getoutput('google-chrome https://www.google.com/search?q='+re))

```
