

class Solution:

    # def two_sum(self, nums: list(), target: int):
    #     for ind, item in enumerate(nums):
    #         another = target - item
    #         for ind2, item2 in enumerate(nums):
    #             if (another == item2) and (ind2 != ind):
    #                 return [ind, ind2]

    ## 数组的遍历， 字典的构建
    def two_sum(self, nums: list(), target: int):
        tmp = {}
        for ind, item in enumerate(nums):
            another = target - item
            if another in tmp:
                return [tmp[another], ind]
            else:
                tmp[item] = ind


def main():
    nums = [2,5,15,5]

    target = 10


    lcode = Solution()
    print(lcode.two_sum(nums, target))

if __name__ == '__main__':
    main()