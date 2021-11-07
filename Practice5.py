'''
[41]
Given a N X N binary Square Matrix where each row and column of the matrix is sorted in ascending order. Find the total number of zeros present in the matrix.

Example 1:

Input:
N = 3
A = {{0, 0, 0},
     {0, 0, 1},
     {0, 1, 1}}
Output: 6
Explanation: 
The first, second and third row contains 3, 2 and 1
zeroes respectively.

Example 2:

Input:
N = 2
A = {{1, 1},
     {1, 1}}
Output: 0
Explanation:
There are no zeroes in any of the rows.
'''

from typing import BinaryIO


def countZeroes(A):
    count = 0
    for i in A:
       for j in i:
            if j == 0:
                count += 1
    print(count)
# countZeroes([[0, 0, 0], [0, 0, 1], [0, 1, 1]])

# --------------------------------------------------------------------------

'''
[42]
Given N bits to an XOR - Gate find the output that will be produced. 
XOR - Gate Table:
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
 

Example 1:

Input:
N = 4
arr: 1 1 1 0
Output:
1
Explanation:
1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1
hence output is 1

Example 2:

Input:
N = 4
arr: 0 0 1 0
Output:
1
Explanation:
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
hence output is 1

HINT : If the number of 1s are even then the answer is 0, otherwise answer is 1.
'''


def xorGate (arr):
    c = 0
    for i in arr:
        if i == 1:
            c += 1
    if c % 2 == 0:
        return 0
    else:
        return 1
# print(xorGate([1, 1, 1, 0]))


# -----------------------------------------------------------------------------

'''
[43]
Given a series of numbers  3,10,21,36 …., and series starting from N = 1, find the pattern and output the N'th value of the above series.

Example 1:

Input:
N = 1
Output:
3
Explanation:
3 is the first term of the series.

Example 2:

Input:
N = 2
Output:
10
Explanation:
10 is the second term of the series.
'''
def differenceSeries(N):
    nth_term  = 2 * N**2 + N
    return nth_term
# print(differenceSeries(2))

# --------------------------------------------------------------------------

'''
[44]
Given a series 9, 33, 73, 129...  Find the n-th term of the series.

Example 1:

Input: n = 4
Output: 129
Explanation: 4th term of the 
series is 129.


Example 2:

Input: n = 5
Output: 201
Explanation: 5th term of the
series is 201.
'''

def nthOfSeries (n):
    nth_term = 8 * n**2 + 1
    return nth_term
# print(nthOfSeries(3))

# ----------------------------------------------------------------------------

'''
[45]
Given a series of numbers 2, 10, 30, 68, 130.., Identify the pattern in the series. You are given an integer X you need to find out the X'th number in the series.

Example 1:

Input:
X = 1
Output:
2
Explanation:
2 is the first number in the series.

Example 2:

Input:
X = 2
Output:
10
Explanation:
10 is the second number in the series.
'''

def X1Series(X):
	nth_term = X * (X**2 + 1)
	return nth_term 
# print(X1Series(3))

# ---------------------------------------------------------------------------------

'''
[46]
Given a number N, the task is to find XOR of count of 0s and count of 1s in binary representation of a given number.
 

Example 1:

Input: N = 5
Output: 3
Explanation: 
Binary representation: 101
Set_bit_count: 2
Unset_bit_count: 1
2 XOR 1 = 3

Example 2:

Input: N = 7
Output: 3
Expalanation:
Binary representation: 111
Set_bit_count: 3
Unset_bit_count: 0
3 XOR 0 = 3
'''

def find_xor(n):
    bn = bin(n)
    v1 = bn[2:]
    c0 = 0
    c1 = 0
    for i in v1:
        if i == '1':
            c1 += 1    
        else:
            c0 += 1
    return c1 ^ c0
# print(find_xor(5))

# -------------------------------------------------------------------------------

'''
[47]
Given a number N, find if it is Disarium or not. A number is called Disarium if sum of its digits powered with their respective positions is equal to the number itself. Output 1 if it's Disarium, and 0 if not.

Example 1:

Input:
N = 89
Output:
1
Explanation:
8^1+9^2 = 89 thus output is 1.

Example 2:

Input:
N = 81
Output:
0
Explanation:
8^1+1^2 = 9 thus output is 0. 
'''

def isDisarium(N):
    c = 0
    n = str(N)
    for i in range(1, len(n)+1):
        c += int(n[i-1]) ** i
    if c == N:
        return 1
    else:
        return 0
# print(isDisarium(89))

# -------------------------------------------------------------------------

'''
[48]
Given a string S, the task is to change the complete string to Uppercase or Lowercase depending upon the case for the first character.

Example 1:

Input:
S = "abCD"
Output: abcd
Explanation: The first letter (a) is 
lowercase. Hence, the complete string
is made lowercase.

â€‹Example 2:

Input: 
S = "Abcd"
Output: ABCD
Explanation: The first letter (A) is
uppercase. Hence, the complete string
is made uppercase.
'''

def modify(s):
    if s[0].isupper():
        return s.upper()
    else:
        return s.lower()
# print(modify('abCD'))

#  ---------------------------------------------------------------------------------

'''
[49]
Given a number N. The task is to generate and print all binary numbers with decimal values from 1 to N.

Example 1:

Input:
N = 2
Output: 
1 10
Explanation: 
Binary numbers from
1 to 2 are 1 and 10.

Example 2:

Input:
N = 5
Output: 
1 10 11 100 101
Explanation: 
Binary numbers from
1 to 5 are 1 , 10 , 11 , 100 and 101.
'''
def binary(N):
    l = ''
    for i in range(1, N+1):
        l += bin(i)[2:] + ' '
    return l
# print(binary(2))
# ------------------------------------------------------------------------------

'''
[50]
Pitsy needs help in the given task by her teacher. The task is to divide a array into two sub array (left and right) containing n/2 elements each and do the sum of the subarrays and then multiply both the subarrays.

Example 1:

â€‹Input : arr[ ] = {1, 2, 3, 4}
Output : 21
Explanation:
Sum up an array from index 0 to 1 = 3
Sum up an array from index 2 to 3 = 7
Their multiplication is 21.â€‹â€‹


â€‹Example 2:

Input : arr[ ] = {1, 2} 
Output :  2 
'''
def multiply (arr, n) : 
    s1 = sum(arr[:n//2])
    s2 = sum(arr[n//2:])
    return s1 * s2
# print(multiply([1, 2, 3, 4], 4))