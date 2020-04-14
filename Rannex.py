# Rannex code to explore new things

print ("\t\t\b\b## CALCULATOR ##\n\t\b\b\b## Developer name RANVEER VERMA ##")
print ()
i=int(input(":-> Enter password to start this program.  "))

if i<9634 or i>9634:
    print ()
    print ("   You have entered wrong password ")
    print ()
if i==9634:
        print ()
        print ("   ## Welcome to python programming ## ")
        print ()
while i!=9634:
    i=int(input (" Enter password again to start or enter 0 to exit the program "))
    if i==9634:
        print ()
        print ("   ## Welcome to python programming ## ")
        print ()
    if i==0:
        print ("   Thank you for using python calculator. ")
        print ()
        break
    if i!=9634:
        print ()
        print ("   You have entered wrong password ")
        print ()
while (i==9634 and i!=0 or i==12 and i!=0):
    from math import *
    
    print ("##  enter 2 to start addition \n##  enter 3 to start subtraction\n##  enter 4 to start multiplication \n##  enter 5 to start division \n##  enter 0 to exit the program ")
    print ()
    j=int(input(":-  Please enter your choice... "))
    
    def div(a,b):
            c=a/b
            print (":-  The result is...  ",c)
            print ()
    
    def multi(a,b):
            c=a*b
            print (":-  The result is...  ",c)
            print ()
   
    def sub(a,b):
            c=a-b
            print(":-  The result is...  ",c)
            print ()
        
    def add(a,b):
        c=a+b
        print (":-  The result is...  ",c)
        print ()
       
    def inp():
        x=int(input(":- Enter the first value...  "))
        y=int(input(":- Enter the second value...  "))
        print ()
        print (":-  first value is... ",x)
        print (":-  second value is... ",y)
        return x,y
    
    if j==2:
        print (" \t\t## Addition ##")
        p,q=inp()
        add(p,q)
    if j==3:
        print (" \t\t## Subtraction ##")
        p,q=inp()
        sub(p,q)
    if j==4:
        print (" \t\t## Multiplication ##")
        p,q=inp()
        multi(p,q) 
    if j==5:
        print (" \t\t## Division ##")
        p,q=inp()
        div(p,q)
    if j==0:
        print()
        print (" Thank you for using python calculator. ")
        break 
   
    i=int (input(" Enter 12 to continue with this program or 0 to exit the program. "))
    if i>0 and i<12 or i>0 and i>12:
        print ("    You have entered wrong number...😪")
