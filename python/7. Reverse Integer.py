class Solution:
    def reverse(self, x: int) -> int:

        minus = False

        if x < 0:
            minus = True
            x = abs(x)

        res = ''

        while x != 0:
            b = x%10
            res += str(b)
            x = x//10

        try:    
            int_num = int(res)
            if minus == True:
                int_num *= -1


            if pow(-2, 31)<= int_num <= pow(2, 31) - 1:
                return int_num

        except Exception:
            return 0

        return 0



print(Solution().reverse(1534236469))


# x = 123

# res = ''

# while x != 0:
#     b = x%10
#     res += str(b)
#     x = x//10

# if pow(-2, 31)<= int(x) <= pow(2, 31) - 1:
#     print(int(x))

# else:
#     print(int(x))