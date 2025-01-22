class Solution:
    def reverseVowels(self, s: str) -> str:
        result = list(s)
        vowels = set("aeiouAEIOU")
        i, j = 0, len(result) - 1
        while i < j:
            if result[i] not in vowels:
                i += 1
            elif result[j] not in vowels:
                j -= 1
            else:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1
        return ''.join(result)
if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels("leetcode"))
        