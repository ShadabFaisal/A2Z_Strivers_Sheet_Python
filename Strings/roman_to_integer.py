class Solution:
 
    # Converts a Roman numeral into an integer.
    def romanToInt(self, s: str) -> int:
        romanValues: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res=0

        for i in range(len(s)):
            if i+1<len(s) and romanValues[s[i]]<romanValues[s[i+1]]:
                res-=romanValues[s[i]]
            else:
                res+=romanValues[s[i]]

        return res
 

# Driver Code starts
def main() -> None:
    s: str = "XLII"
 
    solution = Solution()
 
    # Call the function to convert the Roman numeral.
    answer: int = solution.romanToInt(s)
 
    print(f"Integer value for {s} is {answer}")
 
 
# Run the driver code.
if __name__ == "__main__":
    main()