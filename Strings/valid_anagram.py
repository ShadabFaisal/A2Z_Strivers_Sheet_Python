class Solution:
    def isAnagram(self, s,t)->bool:
        if len(s) != len(t):
            return False

        return sorted(s)==sorted(t)

    def isAnagram_Opt(self,s,t):
        if len(s) != len(t):
            return False

        freq=[0]*26

        for ch in s:
            freq[ord(ch)-ord('a')]+=1

        for ch in t:
            freq[ord(ch)-ord('a')]-=1

        for count in freq:
            if count!=0:
                return False

        return True


s = "listen"
t = "silentq"
 
obj = Solution()
result=obj.isAnagram_Opt(s, t)
print(f"Both strings are Anagrams of each other: {result}")