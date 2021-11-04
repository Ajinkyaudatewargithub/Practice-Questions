'''
[31]
Given two positive integers num1 and num2, the task is to find the sum of the two numbers on a 12 hour clock rather than a number line.

Example 1:

Input: num1 = 5, num2 = 7
Output: 0
Explaination: 5+7=12, which in 12 hour 
clock format is 0.

Example 2:

Input: num1 = 3, num2 = 5
Output: 8
Explaination: 3+5=8, which is 12 hour 
format is intact.
'''

def clockSum(num1, num2):
    hours = num1 + num2
    if hours <=11:
        return hours
        
    else:
        return hours % 12
clockSum(5, 5)

# -------------------------------------------------------------------------------------------

'''
[32]
Given a positive integer n. Find the sum of product of x and y such that floor(n/x) = y .
 

Example 1:

Input: n = 5
Output: 21
Explanation: Following are the possible 
pairs of (x, y):
(1, 5), (2, 2), (3, 1), (4, 1), (5, 1).
So, 1*5 + 2*2 + 3*1 + 4*1 + 5*1 
   = 5 + 4 + 3 + 4 + 5 
   = 21.

Example 2:

Input: n = 10
Output: 87
Explanation: Sum of product of all 
possible pairs of (x, y) is 87.

'''

def sumofproduct(n):
    sm = 0
    for i in range(1, n+1):
        y = n // i
        prod = y * i
        sm = sm + prod
    return sm
# print(sumofproduct(5))

# -------------------------------------------------------------------------------------------

'''
[33]
Given the value of n, we need to find the sum of the series where i-th term is sum of first i natural numbers.

Note: Sum of the series 1 + (1+2) + (1+2+3) + (1+2+3+4) + …… + (1+2+3+4+…+n)

Example 1:

Input: n = 5
Output: 35 
Explanation: 1 + (1+2) + (1+2+3).. = 35
Hence sum of the series is 35.

Example 2:

Input: n = 10
Output: 220
Explanation: 1 + (1+2) + (1+2+3) +
(1+2+3+4) + (1+2+3+4+5)... = 210.
Hence sum of the series is 210.
'''
def sumOfTheSeries(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            count = count + j
    return count
# print(sumOfTheSeries(5))

def sumOfTheSerie(n):
    print(int(( n * ( n + 1 ) * ( 2 * n + 4 ) ) / 12 ))
# sumOfTheSerie(10)

# ----------------------------------------------------------------------------------------

'''
[34]
Given a street of N houses (a row of houses), each house having K amount of money kept inside; now there is a thief who is going to steal this money but he has a constraint/rule that he cannot steal/rob two adjacent houses. Find the maximum money he can rob.

Example 1:

Input:
N = 5 , K = 10
Output:
30
Explanation:
The Robber can rob from the first, third
and fifth houses which will result in 30.

Example 2:

Input:
N = 2 , K = 12
Output:
12
Explanation:
The Robber can only rob from the first
or second which will result in 12.
'''
def maximizeMoney(N , K):
    if N % 2 == 0:
        N = N // 2
        K = K * N
        
    else:
        N = (N+1) // 2
        K = K * N
    print(K)
# maximizeMoney(5, 10)

# ---------------------------------------------------------------------------------------
'''
[35]
Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.

Example 1:

Input:
str = 1abc23
Output: 24
Explanation: 1 and 23 are numbers in the
string which is added to get the sum as
24.

Example 2:

Input:
str = geeks4geeks
Output: 4
Explanation: 4 is the only number, so the
sum is 4.
'''
def findSum(s):
    num = 0
    sm = 0
    for i in range(len(s)):
        if s[i]>= '0' and s[i] <= '9':
            num = num * 10 + (int(s[i])-0)
            print(num)
        else:
            sm = sm + num
            num = 0
    return sm + num
# print(findSum('1abc23'))

# -------------------------------------------------------------------------------------

'''
[36]
Given an N bit binary number, find the 1's complement of the number. The ones' complement of a binary number is defined as the value obtained by inverting all the bits in the binary representation of the number (swapping 0s for 1s and vice versa).
 
Example 1:

Input:
N = 3
S = 101
Output:
010
Explanation:
We get the output by converting 1's in S
to 0 and 0s to 1

Example 2:

Input:
N = 2
S = 10
Output:
01
Explanation:
We get the output by converting 1's in S
to 0 and 0s to 1

'''

def onesComplement(s,n):
    s = str(s)
    nw = ''
    for i in range(n):
        if s[i] == '0':
            nw += '1'
        else:
            nw += '0'
    return nw
# print(onesComplement(101, 3))
# -----------------------------------------------------------------------------------------------

'''
[37]
Given a string S, the task is to create a string with the first letter of every word in the string.

Example 1:

Input: 
S = "geeks for geeks"
Output: gfg

Example 2:

Input: 
S = "bad is good"
Output: big
'''

def firstAlphabet(S):
    ns = ''
    new = S.split(' ')
    for i in new:
	    ns += i[0]
    return ns
# print(firstAlphabet("geeks for geeks"))

# --------------------------------------------------------------------------------------------

'''
[38]
Given the value of n, we need to find the sum of the series where i-th term is sum of first i odd natural numbers.

NOTE: Sum of the series 1 + (1+3) + (1+3+5) + (1+3+5+7) + …… + (1+3+5+7+…+(2n-1))

Example 1:

Input: n = 2
Output: 5 
Explanation: 1 + (1+3) = 5
Hence sum of the series is 5.


Example 2:

Input: n = 5
Output: 55
Explanation: 1 + (1+3) + (1+3+5) +
(1+3+5+7) + (1+3+5+7+9) = 55.
Hence sum of the series is 55.
'''
def sumOfTheSpecialOddSeries(n):
    sm = 0
    for i in range(1, n+1):
        sm += i*i
    return sm
# sumOfTheSpecialOddSeries(5)

# ----------------------------------------------------------------------------------------------------

# n = 1
# while n<10:
#     print(n)
#     n = n +1
# print(n)

# ----------------------------------------------------------------------------------------------------

'''
[39]
Given a positive integer n, check if it is perfect square or not.

Example 1:

Input: n = 35
Output: 0 
Explanation: 35 is not perfect
square because sqrt(35) = 5 but
5*5 !=35.

Example 2:

Input: n = 49
Output: 1
Explanation: sqrt(49) = 7 and 
7*7 = 49, Hence 49 is perfect square. 
'''
def isPerfectSquare (n):
    fvar = n**0.5
    ivar = int(fvar)
    # print(fvar)
    # print(ivar)
    if ivar == fvar:
        return 1
    else:
        return 0
# print(isPerfectSquare(35))

# ----------------------------------------------------------------------------------

'''
Patterns
'''
# 1
# n = 4
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()

# 2
# n = 4
# for i in range(1, n+1):
#     for j in range(i, i+i):
#         print(j, end='')
#     print()

# -----------------------------------------------------------------------------------

'''
[40]
Given N bits to an OR - Gate find the output that will be produced. 
OR - Gate Table:
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0

Example 1:

Input:
N = 4
arr: 1 1 1 0
Output:
1
Explanation:
1 | 1 = 1
1 | 1 = 1
1 | 0 = 1
hence output is 1

Example 2:

Input:
N = 4
arr: 0 0 1 0
Output:
1
Explanation:
0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
hence output is 1
'''
def orGate (arr):
    if 1 in arr:
        return 1
    else:
        return 0
# print(orGate([0, 0, 1,0]))

# ------------------------------------------------------------------------------
