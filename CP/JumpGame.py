def canJump(nums):
        n = len(nums)
        if n==1:
            return True
        for i in range(n):
            if nums[i] == 0:
                break
            c = 0
            x = 0
            while c < n and nums[x] != 0 :
                if nums[c] == 0:
                    break
                x += i + nums[c]
                if x >= n-1:
                    return True
                if x >= n:
                    break
                c += 1
        return False

nums = [2,0,1,0,1]
print(canJump(nums))