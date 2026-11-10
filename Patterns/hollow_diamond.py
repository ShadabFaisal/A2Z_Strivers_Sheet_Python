def print_hollow_diamond(n):
    spaces=0
    for i in range(n):
        #print stars
        for j in range(1,n-i+1):
            print("*",end="")
        #print spaces
        for j in range(1,spaces+1):
            print(" ",end="")   
        #print stars
        for j in range(1,n-i+1):
            print("*",end="")
        print()
        spaces+=2

    spaces=2*n-2
    for i in range(n):
        #print stars
        for j in range(i+1):
            print("*",end="")
        #print spaces
        for j in range(1,spaces+1):
            print(" ",end="")   
        #print stars
        for j in range(i+1):
            print("*",end="")
        print()
        spaces-=2


n=int(input("Enter the number of rows for the hollow diamond: "))
print_hollow_diamond(n)

"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""