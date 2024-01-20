def largestNumber(nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        dummy = nums.copy()
        
        num1 = "".join(nums)
        maxx = int(num1)
        for i in range(len(nums)):
    
            for j in range(i+1, len(nums)+1):
                dummy.insert(j+1, nums[i])
                dummy.pop(j-i-1)
                num2 = "".join(dummy)
                num2 = int(num2)
                if num2 > int(maxx):
                    maxx = num2
        return maxx
nums = input().split(" ")
print(largestNumber(nums))