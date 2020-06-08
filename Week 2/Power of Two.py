Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n & (-n) == n
        
                # 16 = 10000
                # 2's complement of 16 = 10000
                #                        01111
                #                        +   1
                #                        10000
                #    therfore if n and -n == n
                # then its a power of 2
        
        #----------correct for +ve numbers only
        # s="{0:b}".format(n)
        # # a=[map(int,s.split())]
        # # print(a[0])
        # a=[int(i) for i in s]
        # print(a)
        # print(sum(a))
        # if sum(a)==1:
        #     return True
        # return False
    
    
