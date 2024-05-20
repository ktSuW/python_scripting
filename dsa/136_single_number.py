# 136. Single Number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # Approach - 1
    # Time - O(n)
    # Space - O(n)
    # count_dict = {}
    # for num in nums:
    #     if num in count_dict:
    #         count_dict[num] += 1
    #     else:
    #         count_dict[num] = 1
    
    # for num, count in count_dict.items():
    #     if count == 1:
    #         return num
    
    # Approach - 2
    # Time O(n)
    # Space O(1)
        result = 0
        for num in nums:
            result ^= num
        return result

def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([2,2,1],1),
        ([4,1,2,1,2], 4),
        ([1], 1)
    ]
    
    # Run test cases
    for nums, expected in test_cases:
        result = solution.singleNumber(nums)
        print(f'Input: {nums},\nOutput : {result},\nPass : {result == expected}')

if __name__ == "__main__":
    main()