def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            print("True")
            break
        if i==len(nums)-2:
            print("False")
has_33([3,1,2])