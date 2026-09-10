class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        def fun(n):
            total = 0
            while n > 0:
                d = n % 10
                n = n // 10
                total += d * d
            return total

        slow = n
        fast = fun(n)

        while fast != 1:
            slow = fun(slow)
            fast = fun(fun(fast))

            if slow == fast:
                return False

        return True