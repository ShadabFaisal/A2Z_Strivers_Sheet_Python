
def print_numbered_right_angled_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        print()


n=int(input("Enter the number of rows: "))
print_numbered_right_angled_triangle(n)
