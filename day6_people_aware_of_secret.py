class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)   # dp[i] = number of people who learn the secret on day i
        dp[1] = 1            # On day 1, one person knows the secret

        for day in range(1, n + 1):
            for share_day in range(day + delay, min(day + forget, n + 1)):
                dp[share_day] = (dp[share_day] + dp[day]) % MOD

        # Count people who have not forgotten by day n
        return sum(dp[max(1, n - forget + 1): n + 1]) % MOD
