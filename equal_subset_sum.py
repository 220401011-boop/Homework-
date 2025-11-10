def can_partition(nums):
    """
    Checks if the given array 'nums' can be partitioned into two subsets with equal sum.
    """
    total_sum = sum(nums)
    
    # If the total sum is odd, it's impossible to partition into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # dp[i][j] will be True if a sum of 'j' can be formed using the first 'i' elements
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # A sum of 0 is always achievable: the empty subset
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                # Can we form sum j: either without current element or with it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][target]


# Example usage
nums = [1, 5, 11, 5]
if can_partition(nums):
    print("The array can be partitioned into two subsets with equal sum")
else:
    print("The array cannot be partitioned into two subsets with equal sum")
