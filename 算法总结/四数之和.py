#  四数之和
'''
思路：
使用双循环固定两个数，用双指针找另外两个数，通过比较与target 的大小，移动指针。

所以时间复杂度不超过O(n^3)

'''
def fourSum(self,nums:List[int],target:int)->List[List[int]]:
    n = len(nums)
    if n<4:
        return []

    nums.sort()
    res = []

    for i in range(n-3):
        # 防止重复，数组进入res
        if i>0 and nums[i] == nums[i-1]:
            continue
        # 如果大于target 
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            break
        # 当数组最大值和都小于target ，说明i这个数太小，遍历下一个
        if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
            continue
        
        for j in range (i+1,n-2):
            #防止重复
            if j-i > 1 and nums[j] == nums[j-1]:
                continue
            # 如果大于target 
        if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
            break
        # 当数组最大值和都小于target ，说明i这个数太小，遍历下一个
        if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
            continue

        # 双指针
        left = j + 1
        right = n - 1

        while left < right:
            tmp = nums[i] + nums[j] + nums[left] + nums[right]
            if tmp == target:
                res.append([nums[i] , nums[j] , nums[left] , nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1 
            elif tmp > target:
                right -= 1
            else:
                left += 1
    return res


#  解2
def fourSum(self,nums:List[int],target:int)->List[List[int]]:
    length = len(nums)
    result = []
    if length < 3:
        return result

    nums.sort()
    for i in range(length - 3):
        if i > 0 and nums[i] == nmms[i-1]:
            continue
        for j in range(i+1,length-2):
            if j > 0 and nums[j] == nums[j-1]:
                continue

            l = j+1
            r = length - 1

            while l<r:
                res = nums[i] + nums[j] + nums[l] + nums[r]

                if res == target:
                    result.append([nums[i],nums[j],nums[l],nums[r]])

                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                
                elif res < target:
                    l += 1
                else:
                    r -= 1
    return result 

