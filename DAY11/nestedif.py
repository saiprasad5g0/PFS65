'''fa  = eval(input("FOllow account:"))
if fa:
    cf = eval(input("Close Friend :"))
    if cf:
        print("story visisble ")
    else:
        print("Nt in the closefriends")
else:
    print("FOllow the account first")'''

'''reg = eval(input("Registered : "))
if reg:
    fee = eval(input("fee paid"))
    if fee :
        print("tournement entry conformed")
    else:
        print("Fee pending")
else:
    print("registration reqired")'''

'''lk  = eval(input("ENTER active :"))
if lk:
    pg = eval(input("permission granted"))
    if pg:
        print("Accesed")
    else:
        print("access denied")
else:
    print("LINk experied")'''

'''data  = {'Ram':{'status':True,'python':90,'mysql':95,'flask':98},
         'Sai':{'status':False,'python':None,'mysql':None,'flask':None},
         'suresh':{'status':True,'python':20,'mysql':30,'flask':50},
         'venky':{'status':True,'python':90,'mysql':95,'flask':98},
         'Mahesh':{'status':True,'python':60,'mysql':65,'flask':70},
         'krishna':{'status':True,'python':50,'mysql':55,'flask':48}
         }

name  = input("Enter name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = sum/3
        print(f"hello {name}!!!")
        print(f"your average score is {avg}")
        if avg >=90:
            print("Outstanding")
        if avg >=80:
            print("very good")
        if avg >=70:
            print("good")
        if avg >=35:
            print("Better luck next time")
        else:
            print("failed")
    else:
        print(f'{name} did not attend the exam')
else:
    print("Absent")'''