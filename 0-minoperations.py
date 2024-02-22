#!/usr/bin/python3

def minOperations(n):
    if n == 1:
        return 0
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    return dp[n]

# Example usage
n = 9
print(minOperations(n))  # Output: 6
