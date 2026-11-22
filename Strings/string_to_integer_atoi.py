class Solution:
    def myAtoi(self, s:str)->int:
        s=s.strip()

        sign=1
        res=0

        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign=-1
            s=s[1:]

        for char in s:
            if not char.isdigit():
                break
            res=res*10 + int(char)

        return res*sign
        




# Driver Code starts
def main() -> None:
    s: str = "   -123ab"
 
    solution = Solution()
 
    # Call the function to convert the Roman numeral.
    answer: int = solution.myAtoi(s)
 
    print(answer)
 
 
# Run the driver code.
if __name__ == "__main__":
    main()