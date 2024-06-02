import copy
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        copied_candies = copy.copy(candies)
        sorted_candies = candies.sort()
        greatest_candie = max(candies)
        for i in range(len(candies)):
            if greatest_candie <= (copied_candies[i]+extraCandies):
                result.append(True)
            else:
                result.append(False)
        return result
                
        