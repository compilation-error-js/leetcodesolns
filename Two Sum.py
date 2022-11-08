

#Solutions 1: using hashmap , key point is else condition not required.
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {};
        for i, num in enumerate(nums):
            if target - num in hashMap:
                return [i,hashMap[target-num]];
            hashMap[num] = i;
        return [-1,-1];
