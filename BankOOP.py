L=list()
bold= '\33[1m'
red='\33[41m'
green= '\33[42m'
end= '\33[0m'
class bank():
    def __init__(self,b,c,d,e,f):
        self.name=b
        self.nic=c
        self.accnum=d
        self.pw=e
        self.amount=f
    def datainput(self):
        inp=print('Welcome User')
        fn=input('Please input your full name: ')
        nic=input('Please input the last 4 digits of your NIC: ')
        an=input('Please input your 5 digit Account number: ')
        while len(an)!=5:
            print(red+'ERROR: Input correct data.'+end)
            an=input('Please input your 5 digit Account number: ')
        pw=(fn[0:2]+nic[0:3]+an[1:2]+fn[2:3])
        amount=float(input('Please input the amount you want to credit:'))
        self.dataentry(fn, nic, an, pw, amount)
    
    def datainput1(self):
        an=input('Please input your account number: ')
        pww=input('Please enter your password: ')
        global L
        status=False
        while status == False:
            for x in L:
                if x.accnum==an and x.pw==pww:
                    print(green+"APPROVED"+end)
                    print(f'Your current balance is {x.amount} ')
                    s=input("Input 1 if you want to Withdraw and 2 if you want to Deposit")
                    if s=="1":
                        am=float(input('Please enter the amount: '))
                        x.amount=x.amount-am
                        print(f'Your new balance is {x.amount}')
                        status=True
                    elif s=="2":
                        am=float(input('Please enter the amount: '))
                        x.amount=x.amount+am
                        print(f'Your new balance is {x.amount}')
                        status=True
                else:
                    print(red+"Incorrect Data"+end)
                    pww=input('Please enter your password: ')
                    status=False
                    

              
            
    def dataentry(self,b,c,d,e,f):
        global L
        L=L+[bank(b, c, d, e,f)]
    
    def printer(self):
        global L
        for x in L:
            print(f'Full Name: {x.name}     NIC: 42xxx-xxx-{x.nic}     Account Number: {x.accnum}   Password: {x.pw}   Balance: {x.amount}')
    
   
    def insertionsort(self):
        for a in range(1, len(L)):
            key=L[a]
            i=a-1
            while i>-1 and L[i].accnum>key.accnum:
                L[i+1]=L[i]
                i=i-1
            L[i+1]=key

    
    def mainmenu(self):
        value=input('press:\n1 for input\n2 If you already have an account\n3 for Sorting According to Account Numbers\n4 for printer\n\n\n')
        while value!="1" and value!="2" and value!="3" and value!='4':
            print("Incorrect value given.")
            value=input('press:\n1 for signing up\n2 If you already have an account\n3 for Sorting According to Account Numbers\n4 for printer\n\n\n')
        if value=='1':
            self.datainput()
        elif value=='2':
            self.datainput1()
        elif value=='3':
            self.insertionsort()
        elif value=='4':
            self.printer()
    
   
        
                
A=bank(0,0,0,0,0)
c=False
while c==False:
    A.mainmenu()
    f=int(input("Please enter 1 to exit or 0 to continue"))
    if f==1:
        c=True
        
          
