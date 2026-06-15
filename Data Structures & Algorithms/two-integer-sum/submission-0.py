class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valores_vistos = {}
        for i, n in enumerate(nums):
            diferencia = target - n
            if diferencia in valores_vistos:
                return [valores_vistos[diferencia], i]
            valores_vistos[n] = i
            
