class Solution:
    def reverse_string(self,s: list[str])->None:
        i=0
        j=len(s)-1

        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1

        return s

s = ["h","e","l","l","o"]
 
obj = Solution()

obj.reverse_string(s)
print(s)