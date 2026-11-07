

def print_half_diamond(n):
    for i in range(2*n):
        stars=i
        if(i>n):
            stars=2*n-i
        for j in range(stars):
            print("*", end=" ")
        print()
    


n=int(input("Enter the number of rows: "))
print_half_diamond(n)