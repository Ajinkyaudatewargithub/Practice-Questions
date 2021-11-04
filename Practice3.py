'''
[21]

Given an array Arr of size N, swap the Kth element
from beginning with Kth element from end.

Example 1:

Input:
N = 8, K = 3
Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: Kth element from beginning is
3 and from end is 6.

Example 2:

Input:
N = 5, K = 2
Arr[] = {5, 3, 6, 1, 2}
Output: 5 1 6 3 2
Explanation: Kth element from beginning is
3 and from end is 1.
'''

def swapKth(arr, k):	
	arr[k-1], arr[-k] = arr[-k], arr[k-1]
	print(arr)
# swapKth([5, 3, 6, 1, 2], 2)

# --------------------------------------------------------------------------------------

'''
[22]
Given a number N. The task is to complete the function convertFive() which replace all zeros 
in the number with 5 and returns the number.

Input:
The first line of input contains an integer T, denoting the number of testcases. 
Then T testcases follow. Each testcase contains a single integer N denoting the number.

Output:
The function will return integer where all zero's are converted to 5.

User Task:
Since this is a functional problem you don't have to worry about 
input, you just have to complete the function convertFive().

Constraints:
1 <= T <= 103
1 <= N <= 104

Example:
Input
2
1004
121

Output
1554
121

Explanation:
Testcase 1:  At index 1 and 2 there
is 0 so we replace it with 5.Testcase 2: There is no ,0 so output will remain same.
'''

def convertFive(n):
    num = ''
    for i in str(n):
        if int(i) == 0:
            i = 5
        num = num + str(i)
    return int(num)
# print(convertFive(1004))

# ------------------------------------------------------------------------------------


'''
[23]
Given a single integer N, your task is to find the sum of the square of first N even natural Numbers.

Example 1:

Input: 2
Output: 20
Explanation: 22 + 42 = 20

Example 2: 

Input: 3
Outptut: 46
Explanation: 22 + 42 + 62 = 56

'''
# 1
n = 2
l1 = []
while 1:
    s = 0
    for i in range(n):
        s = s+2
        # print(s)
        l1.append(s)
    break

l2 = []
for i in l1:
    i = pow(i, 2)
    l2.append(i)
# print(sum(l2))


# 2 ---------------------------------------------------------------------------------------------------
l1 = []
while 1:
    s = 0
    for i in range(n):
        s = s+2
        # print(s)
        l1.append(s)
    break

for i in l1:
    i += i * i
# print(i)

# 3 ---------------------------------------------------------------------------------------------------
def sum_of_square_evenNumbers(n):
    s = 0
    sm = 0 
    for i in range(n):
        s = s+2
        sm += s*s
    return sm
# print(sum_of_square_evenNumbers(3))

# -----------------------------------------------------------------------------------------------------------


'''
[24]
A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term.

Example 1:

Input: n = 5, a = 1, d = 3
Output: 35
Explanation: Series upto 5th term is
1 4 7 10 13, so sum will be 35.

'''

def sum_of_ap( n, a, d):
	# Code here
	Sn = n / 2 * ( 2 * a + ( n - 1 ) * d )
	return int(Sn)

# --------------------------------------------------------------------------------------
'''
[25]
Given two positive integers num1 and num2, the task is to find the product of the 
two numbers on a 12 hour clock rather than a number line.
Note: Assume the Clock starts from 0 hour to 11 hours.

Example 1:

Input:
num1 = 2, num2 = 3
Output:
6
Explanation:
2*3 = 6. The time in a 12 hour clock is 6.

Example 2:

Input:
num1 = 3, num2 = 5
Output:
3
Explanation:
3*5 = 15. The time in a 12 hour clock is 3.
'''

def mulClock(num1, num2):
    hours = num1 * num2
    if hours >=0 and hours <=11:
        print(hours)
    else:
        print( hours % 12 )
# mulClock(3, 6)


'''
[26]
Given a string str, convert the first letter of each word in the string to uppercase. 

Example 1:

Input:
str = "i love programming"
Output: "I Love Programming"
Explanation:
'I', 'L', 'P' are the first letters of 
the three words.
'''
def transform(s):
    s2 = s.split()
    ans = ''
    for i in s2:
        ans = ans + i.capitalize() + ' '
    return ans
# print(transform("i love programming"))

# ----------------------------------------------------------------------------------------------------

'''
[27]
Factorial of nth number
'''
n = 7
count = 1
for i in range(1, n+1):
    count = count * i
# print(count)

# ----------------------------------------------------------------------------------------------------

'''
[28]
Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.

Example 1:

Input: n = 2, r = 1
Output: 2
Explaination: 2!/(2-1)! = 2!/1! = (2*1)/1 = 2.

Example 2:

Input: n = 3, r = 3
Output: 6
Explaination: 3!/(3-3)! = 3!/0! = 6/1 = 6.
'''

def nPr(n, r):
    sm1 = 1
    for i in range(1, n+1):
        sm1 = sm1 * i
        
    sm2 = 1
    rg = n - r 
    for i in range(1, rg + 1):
        sm2 = sm2 * i
        
    nPr = sm1 // sm2
    return nPr
# print(nPr(3, 3))

# -----------------------------------------------------------------------------------------------

'''
[29]
Given a string S which consists of alphabets , numbers and special characters. You need 
to write a program to split the strings in three different strings S1, S2 and S3 such that
the string S1 will contain all the alphabets present in S , the string S2 will contain all
the numbers present in S and S3 will contain all special characters present in S.  The 
strings S1, S2 and S3 should have characters in same order as they appear in input.


Example 1:

Input:
S = geeks01for02geeks03!!!
Output:
geeksforgeeks
010203
!!!
Explanation: The output shows S1, S2 and S3. 

Example 2:

Input:
S = **Docoding123456789everyday##
Output:
Docodingeveryday
123456789
**##

'''

def splitString(S): 
    alpha = ""
    num = ""
    special = ""
    for i in range(len(S)):
        if (S[i].isdigit()):
            num = num+ S[i]
        elif (S[i] >= 'A'):
            alpha += S[i]
        else:
            special += S[i]
     
    return alpha, num, special
# print(splitString('**Docoding123456789everyday##'))

# s = '**Docoding123456789everyday##'
# s1 = ''
# s2 = ''
# s3 = ''
# for i in range(len(s)):
#     if s[i].isdigit():
#         s2 = s2 + s[i]
#     elif s[i] >= 'A':
#         s1 = s1 + s[i]
#     else:
#         s3 = s3 + s[i]

# print('String', s1)
# print('Numbers', s2)
# print('Special Characters', s3)

# ----------------------------------------------------------------------------------------

'''
[30]
Given a non-empty sequence of characters str, return true if sequence is Binary, else return false

Example 1:

Input:
str = 101
Output:
1
Explanation:
Since string contains only 0 and 1, output is 1.

Example 2:

Input:
str = 75
Output:
0
Explanation:
Since string contains digits other than 0 and 1, output is 0.
'''

def isBinary(str):
    a = set(str)
    if str == '0':
        return 1
    elif str == '1':
        return 1
    elif a == {'1', '0'}:
      return 1
    else:
      return 0
# print(isBinary('101010'))