
def print_solid_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


n=int(input("Enter the number of rows: "))
print_solid_square(n)
