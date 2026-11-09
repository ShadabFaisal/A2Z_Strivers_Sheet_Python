def print_character_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end=" ")

        for j in range(i + 1):
            print(chr(ord("A") + j), end=" ")

        for j in range(i - 1, -1, -1):
            print(chr(ord("A") + j), end=" ")

        print()


n = int(input("Enter the number of rows: "))
print_character_pyramid(n)
""""
        A 
      A B A 
    A B C B A 
  A B C D C B A 
A B C D E D C B A 
"""