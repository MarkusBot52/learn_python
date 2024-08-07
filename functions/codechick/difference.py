# https://codechick.io/challenges/38


# №1
# def difference(nums):
#     maxx = max(nums)
#     minn = min(nums)
#     return maxx - minn


# №2
def difference(nums):
    if not nums:
        return []

    nums.sort()  # сортировка списка
    return nums[-1] - nums[0]
