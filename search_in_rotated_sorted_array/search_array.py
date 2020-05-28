class Solution:
    def search(self, nums: list, target: int) -> int:
        """
        Searches for an element in a rotated array.
        """
        # first, we need to find the pivot
        # if we didn't find the element while searching for pivot
        # look for it again with ususal binary search adjusted for pivot position
        def find_pivot_index():
            start = 0
            end = len(nums) - 1
            # pivot is characterised by previous index value being bigger than the one at pivot position
            # we can modify the usual binary search algorithm to search for the pivot point
            pivot = None
            if nums[0]<nums[-1]:
                pivot = 0
            while pivot is None:
                mid = (start+end)//2
                # check if the current mid point or it's adjacent values are pivots
                if nums[mid] < nums[mid-1]:
                    pivot = mid
                elif nums[mid] > nums[mid+1]:
                    pivot = mid+1
                else:
                    # if the current mid is not the pivot
                    # compare values at the start and end to the value at the mid
                    # to find out in which direction the pivot is
                    if nums[start] > nums[mid]:
                        end = mid
                    else:
                        start = mid
            return pivot
        
        pivot = find_pivot_index()
        start = pivot
        end = len(nums) + pivot
        while start<=end:
            mid = (start+end)//2
            adjusted_mid = mid%len(nums)
            if nums[adjusted_mid] == target:
                return adjusted_mid
            elif target>nums[adjusted_mid]:
                start = mid + 1
            elif target<nums[adjusted_mid]:
                end = mid
            # print(start,end)
        return -1

print("Target index is: ", Solution().search([5, 1, 2, 3, 4], 5))
