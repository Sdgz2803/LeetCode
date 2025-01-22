class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()  # Splits by any whitespace and removes extra spaces
        # Reverse the list of words
        words.reverse()
        # Join the reversed words with a single space
        return ' '.join(words)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))  # Output: "blue is sky the"
    print(s.reverseWords("  hello world  "))  # Output: "world hello"
    print(s.reverseWords("a good   example"))  # Output: "example good a"