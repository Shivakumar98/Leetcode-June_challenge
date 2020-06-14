Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        #added result list of lists for subset finding
        if len(nums)==0:
            return []
        n=sorted(nums)
        print(nums)
        r=[[i] for i in n]
        for i in range(len(n)):
            for j in range(i):
                if n[i]%n[j]==0 and len(r[i])<len(r[j])+1:
                    r[i]=r[j]+[n[i]]
        print(r)
        return max(r,key=len)
        
        
        
        #will not give max subset
#         s=set()
#         for i in range(len(nums)):
#             for j in range((i+1),len(nums)):
#                 if nums[i]%nums[j]==0 or nums[j]%nums[i]==0 :
                    
#                     s.add(nums[i])
#                     s.add(nums[j])
#         return sorted(s)

        
