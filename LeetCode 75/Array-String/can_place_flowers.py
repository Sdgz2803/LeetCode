class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1 
                    count += 1
                    if count >= n:
                        return True
        
        return count == n
    
if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1))
    print(s.canPlaceFlowers([1,0,0,0,1], 2))      