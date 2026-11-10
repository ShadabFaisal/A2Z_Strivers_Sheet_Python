def print_butterfly_pattern(n):
    # Upper half
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for j in range(2*(n-i-1)):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()
    
    # Lower half
    for i in range(n):
        for j in range(1,n-i+1):
            print("*", end="")
        for j in range(2*i):
            print(" ", end="")
        for j in range(1,n-i+1):
            print("*", end="")
        print()

n=int(input("Enter the number of rows for the butterfly pattern: "))
print_butterfly_pattern(n)