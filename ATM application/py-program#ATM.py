# ATM APPLICATION
# users - amount - withdraw - deposit - balance check - password change(update)
u=['shubham','shikha','ramanuj','mamta']
p=['11','22','33','44']
a=[3000,2000,8000,5000]
while(1):
    op=input('do you want to sign in or sign up 1>sign in 2>sign up 3>records check'    )
    if(op=='1'):
        au=input('enter your username   ')
        r=au in u
        if(r==True):
            b=input('enter your password now  ')
            ind=u.index(au)  
            if(b==p[ind]):
                print('  you are authenticated')
                con=input('choose any operation 1>withdraw 2>deposit 3>balance check 4>update')
                if(con=='1'):
                    amt=int(input('enter your amount  '))
                    if(amt<a[ind]):
                        ramt=a[ind]-amt
                        a[ind]=ramt
                        print('your remaining balance is: ',ramt)
                    else:
                        print('insufficient balance')
                elif(con=='2'):
                    amt=int(input('enter your amount'))
                    uamt=amt+a[ind]
                    a[ind]=uamt
                    print('your updated balance is: ',uamt)
                elif(con=='3'):
                    print=('your balance is :',a[ind])
                elif(con=='4'):
                    nup=input('enter your new password to update')
                    p[ind]=nup
                    print('your password has been updated')
            else:
                print('sorry your password is incorrect')
        else:
            print('your username is incorrect')
    elif(op=='2'):
        nu=input('enter your new username')
        np=input('enter your new password')
        na=int(input('enter your new account balance'))
        u.append(nu)
        p.append(np)
        a.append(na)
    elif(op=='3'):
        print('usernames are:',u)
        print('passwords are:',p)
        print('amounts are:',a)
