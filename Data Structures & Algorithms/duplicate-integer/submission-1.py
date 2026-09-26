class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set
        s = set()
        # bool for tracking
        duplicate = False

        # iterate through the list "nums"
        for num in nums:
            if num in s:
                duplicate = True
            else:
                s.add(num)
        
        return duplicate
        