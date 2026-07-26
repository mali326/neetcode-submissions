class Solution:
    def fib(self,n,memo):
        if n<=3: #first 3 are same as # steps
            return n

        if memo[n] != -1:
            return memo[n]

        memo[n] = self.fib(n-1,memo)+self.fib(n-2,memo)
        return memo[n]
        
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n+1)
        memo[1]=1
        return self.fib(n,memo)