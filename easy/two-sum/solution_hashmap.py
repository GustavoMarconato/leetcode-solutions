class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in hashmap:
                return [hashmap[complemento], i]

            hashmap[num] = i
