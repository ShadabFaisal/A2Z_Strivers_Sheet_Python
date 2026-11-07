def print_number_crown(n):
    spaces = 2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        for k in range(spaces-2*i):
            print(" ", end=" ")
        for l in range(i,-1,-1):
            print(l+1, end=" ")
        print()

n=int(input("Enter the number of rows: "))
print_number_crown(n)
"""
1             1
1 2         2 1
1 2 3     3 2 1 
1 2 3 4 4 3 2 1

"""