# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # 0 to length of nums-1
            for j in range(len(nums)): # same as Above
                if nums[i]+nums[j] == target:   
                    return [i,j]    # If True Then Return Value and Exit

# --HappyCode--
