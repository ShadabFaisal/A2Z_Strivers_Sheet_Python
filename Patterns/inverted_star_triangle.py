
def print_inverted_star_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()


n=int(input("Enter the number of rows: "))
print_inverted_star_triangle(n)
