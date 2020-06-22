Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((sum(set(nums))*3-sum(nums))/2)
        
        # Easier one
        s=sum(set(nums))*3
        print(s)
        s2=sum(nums)
        print(s2)
        s=s-s2
        print(s)
        n=s//2
        return n
        
        
        # My solution
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if d[k]==1:
                return k

        
