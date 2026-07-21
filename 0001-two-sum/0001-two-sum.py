from typing import List

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = list(enumerate(nums))  # (index, value)
        indexed.sort(key=lambda x: x[1])  # sort by value
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            total = indexed[left][1] + indexed[right][1]
            
            if total == target:
                return [indexed[left][0], indexed[right][0]]
            elif total < target:
                left += 1
            else:
                right -= 1
        
        return []