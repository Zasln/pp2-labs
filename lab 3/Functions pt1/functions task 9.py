def spy_game(nums):
    for i in range(0, len(nums)-2):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            print("True")
            break
        if i==len(nums)-3:
            print("False")
spy_game([1, 2, 3, 0, 0, 5, 0, 0, 7])