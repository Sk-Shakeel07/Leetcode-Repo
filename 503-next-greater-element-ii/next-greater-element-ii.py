class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxIdx = 0
        maxx = nums[0]
        for i in range(len(nums)):
            if nums[i] > maxx:
                maxIdx = i
                maxx = nums[i]
        
        st = []
        lenn = len(nums)
        res = [-1] * lenn
        
        for i in range(maxIdx, maxIdx - lenn, -1):
            idx = i % lenn  # Wrap index for circular behavior
            
            if not st:
                st.append(idx)
                res[idx] = -1
                continue
            
            while st and nums[idx] >= nums[st[-1]]:
                st.pop()
            
            if not st:
                res[idx] = -1
            else:
                res[idx] = nums[st[-1]]
            
            st.append(idx)
        
        return res
