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
print(X1Series(3))