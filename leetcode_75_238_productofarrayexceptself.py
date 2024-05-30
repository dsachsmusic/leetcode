# potentially doesn't solve for all potential inputs, and potentially, also, incomplete (even if is )
# tested against input fro leetcode, but not against all possible input
# not sure this adheres to time complexity requirement of problem
nums = [-1,1,0,-3,3]
output = []
for i in range(len(nums)):
    product = 1
    print("i is",i)
    #math for anything that appears after the current index of nums, to product
    for j in range(i+1,len(nums)):
        print("j is",j)
        product *= nums[j]
    #math for anything that prior after the current index of nums, to product
    for k in range(0,i):
        print("k is",k)
        product *= nums[k]
    output.append(product)
output
# use the iterator as placeholder for what element of array should be excluded from multiplication

# if the first element of array, can multiple all in range(len(nums)-1) skipping the first, similar for last

# if middle of array, have to do split length twice?