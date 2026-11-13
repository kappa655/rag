class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        counter = 0
        for i in range(len(flowerbed)):
            if counter == 3:
                n = n - 1
                counter = 1
            if not flowerbed[i]:
                counter = counter + 1
        if n > 0 :
            return False
        else:
            return True

solution = Solution()
flowerbed = [1,0,1,0,1,0,1]
n = 1
res = solution.canPlaceFlowers(flowerbed, n)