class Solution:
    ### 逆序删除
    def removeDup(self, nums):
        max_len = len(nums) - 1
        new_len = 1
        while max_len > 0:
            if nums[max_len] == nums[max_len - 1]:
                del nums[max_len]
                max_len -= 1
            else:
                max_len -= 1
                new_len += 1
        return new_len

    ### 双指针
    def removeDuplicates(self, nums):
        p = 0
        q = 1
        numsLen = len(nums)

        # 输入列表为空
        if not numsLen:
            return 0

        # 输入列表不为空
        while q < numsLen:
            if nums[p] == nums[q]:
                q += 1
            else:
                p += 1
                nums[p] = nums[q]
                q += 1
        return p + 1


if __name__ == '__main__':
    test = [1, 1]
    test2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Uniq_parse = Solution()
    print(Uniq_parse.removeDuplicates(test2))

"""
Python 用集合的特性set()
arr = [1,4,3,3,4,2,3,4,5,6,1]
uniq_arr = list(set(arr))

"""
