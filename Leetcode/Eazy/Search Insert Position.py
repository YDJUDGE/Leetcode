#9
# nums = [1,3,5,6]
# target = 2
# for i in nums:
#     if i == target:
#         print(nums.index(i))
# nums.append(target)
# nums.sort()
# print(nums.index(target))



def searchInsert(nums, target):
    for i in nums:
        if i == target:
            print(nums.index(i))
            break
    nums.append(target)
    nums.sort()
    print(nums.index(target))

print(searchInsert([1,3,5,6], target=2))