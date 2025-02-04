#Write a python program to read three numbers and if any two variables are equal, print that number
x=int(input("enter the num:"))
y=int(input("enter the num:"))
z=int(input("enter the num:"))
if(x==y):
    print(x)
elif(y==z):
    print(y)
elif(x==z):
    print(x)
else:
        print("no same variables")
        
