def singleNumber(nums):
    num_dict = {}
    for i in nums:
        if i in num_dict:
            del num_dict[i]
        else:
            num_dict[i]=1
    return num_dict.popitem()[0]
