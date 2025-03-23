def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    
    p1 = 1
    for p2 in range(1, len(nums)):
        if nums[p2] != nums[p2-1]:
            nums[p1] = nums[p2]
            p1 += 1
            
    return p1

def testRemoveDuplicates():
    nums = []
    k = removeDuplicates(nums)
    assert(k == 0)
    assert(nums[:k] == [])
    
    nums = [1, 1, 2]
    k = removeDuplicates(nums)
    assert(k == 2)
    assert(nums[:k] == [1, 2])
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = removeDuplicates(nums) 
    assert(k == 5)
    assert(nums[:k] == [0, 1, 2, 3, 4])