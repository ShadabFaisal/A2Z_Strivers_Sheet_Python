
def print_right_angled_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()


n=int(input("Enter the number of rows: "))
print_right_angled_triangle(n)
