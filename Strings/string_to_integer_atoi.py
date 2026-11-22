




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