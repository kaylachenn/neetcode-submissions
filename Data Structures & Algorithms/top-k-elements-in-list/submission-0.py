class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1
        
        sorted_tracker = dict(sorted(tracker.items(), key=lambda item: item[1], reverse=True))
        just_keys = list(sorted_tracker)

        result = []
        for i in range(k):
            result.append(just_keys[i])

        return result
        