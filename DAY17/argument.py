# positional aruguments:

'''def display(name,email,pw):
    print("name: ",name)
    print("email: ",email)
    print("pw:",pw)
display('sai','sai@gmail','s123')
display('sai@gmail','sai','s123')
display('s123','sai','sai@gmail')'''


#KEyword arguments:

'''def display(name,email,pw):
    print("name: ",name)
    print("email: ",email)
    print("pw:",pw)
display(name='sai',email='sai@gmail',pw='s123')
display(email='sai@gmail',name='sai',pw='s123')
display(pw='s123',name='sai',email='sai@gmail')'''


#default argument:

'''def display(name,email,pw=None):
    print("name: ",name)
    print("email: ",email)
    print("pw:",pw)
display("sai","email")
display("sai","email","pw@123")'''



#variable argument


'''def display(*names):
    print(names)


display("sai")
display("sai","Ram")
display("sai","ram","prasad")'''


def display(**names):
    print(names)


display(n1="sai")
display(n1="sai",n2="Ram")

