def print_character_right_angled_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord('A') + i), end=' ')
        print()


n = int(input("Enter the number of rows: "))
print_character_right_angled_triangle(n)
"""
A 
B B 
C C C 
D D D D 
E E E E E 
"""