from math import gcd
class Solution: 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # The gcd string will be the prefix of length gcd_length
        return str1[:gcd_length]

if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings("ABCABC", "ABC"))
    print(s.gcdOfStrings("ABABAB", "ABAB"))
    print(s.gcdOfStrings("LEET", "CODE"))
        
        