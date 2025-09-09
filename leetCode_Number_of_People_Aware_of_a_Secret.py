class Solution:
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        dp = [0] * (n+1)
        dp[1] = 1
        
        for i in range(1, n+1):
            if dp[i] == 0:
                continue
            for j in range(i+delay, min(n, i+forget-1)+1):
                dp[j] = (dp[j] + dp[i]) % MOD
        
        # People who still remember on day n
        return sum(dp[max(1, n-forget+1): n+1]) % MOD