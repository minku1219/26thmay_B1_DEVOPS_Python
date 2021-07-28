import subprocess
while(True):
    m=1;
    print("Press ctrl+c to Exit from Code")
    n=input("Enter the Command: $ ")
    s=subprocess.getstatusoutput(n)
    if (n.isdigit()==True):
        while(m<=10):
            print(int(n),"*",m,"=",int(n)*m)
            m=m+1
    elif(s[0]==0):
        op=subprocess.getstatusoutput(n)
        if(op[0]==0):
            print(op[1]);
    else:
        re=n.replace(" ",'+')
        print(subprocess.getoutput('google-chrome https://www.google.com/search?q='+re))
