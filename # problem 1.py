# problem 1



numbers = [2, 7, 11, 15]
total = 17
def two_sum(nums, target):

    seen = {}

    for i,num in enumerate(nums):
        needed  = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i        

p1_sol = two_sum(numbers, total)        