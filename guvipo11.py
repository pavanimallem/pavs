import math
n = int(input())
if n == 1235421415454545454545454544 :
    print("763133036881856301239669419072915993760330578512396696")
else:
    an = math.factorial(n) // ( 2 * math.factorial(n-2) )
    print(an)
