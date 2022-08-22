import time
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0]#,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
n = len(nums)
# dp = [-1 for jump in range(n)]
def recurCheck(i):
    if i == n-1 or nums[i] >= n-1-i:
        return 1
    # if dp[i] != -1:
    #     return dp[i]
    jumpLength = nums[i]
    for jump in range(1, jumpLength+1):
        if recurCheck(i+jump):
            # dp[i]  = 1
            return 1
        # else:
        #     dp[i]  = 0
    return 0
st = time.process_time()
recurCheck(0)
et = time.process_time()
print(et-st)