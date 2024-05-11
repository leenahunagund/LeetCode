
memo={}
def dp(n, memo):
    if n in memo: return memo[n]
    if n<=2: return 1
    memo[n]=dp(n-1,memo)+dp(n-2,memo)
    return memo[n]


print(dp(2,memo))