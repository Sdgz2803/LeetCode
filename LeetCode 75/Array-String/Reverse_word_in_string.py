class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  
        words.reverse()
        return ' '.join(words)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue")) 
    print(s.reverseWords("  hello world  ")) 
    print(s.reverseWords("a good   example")) 
