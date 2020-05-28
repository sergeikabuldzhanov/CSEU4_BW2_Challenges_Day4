class Solution:
    def findDuplicate(self, nums: list) -> int:
        # if there's only 1 duplicate, the sum of all elements in the array is 
        # 1 + 2 + 3 ... + n + x
        # if we group the operands we will get
        # (n+1)+(2+n-1)+(3+n-2)...
        # which can be reduced to (n+1)n/2 + x
        # which means that x can be found as sum(list) - (n+1)*n/2
        n = len(nums)-1
        # runtime O(n), because of the sum
        return int(sum(nums) - (n+1)*n/2)

print(Solution().findDuplicate([1,3,4,4,2]))