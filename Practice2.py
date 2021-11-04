'''
[11]
Given the first 2 terms A1 and A2 of an Arithmetic Series.Find the Nth term of the series. 

Example 1:

Input:
A1=2
A2=3
N=4
Output:
5
Explanation:
The series is 2,3,4,5,6....
Thus,4th term is 5.

'''
# 1
def nthTermOfAP(A1,A2,N):
    difference = A2 - A1
    AP = A1 + (N-1) * difference
    return AP

# print(nthTermOfAP(2, 3, 4))

# 2
def nthTerm(a1, a2, n):
    AP = a1 + (a2-a1) * n-1
    return AP
# print(nthTerm(2, 3, 4))

# ------------------------------------------------------------------------------ #

'''
[2]
Calculate factorial of a given number N.
 
Example 1:

Input: 5
Output: 120
Explanation: 1 * 2 * 3 * 4 * 5 = 120.

'''
# def find_fact(n):
a = 5
fact = 1
for i in range(1, a+1):
    fact *= i
# print(fact)


# -------------------------------------------------------------------------------------------

'''
[13]
For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of
three digits is an integer such that the sum of the cubes of its digits is equal to the number 
itself. Return "Yes" if it is a armstrong number else return "No".
Note: 371 is an Armstrong number since 33 + 73 + 13 = 371

Example 1:

Input: N = 153
Output: "Yes"
Explanation: 153 is an Armstrong number
since 13 + 53 + 33 = 153.
Hence answer is "Yes".

'''
# 1
def armstrongNumber(ob):
    convert = str(ob)
    store = 0
    for i in convert:
        i = int(i) * int(i) * int(i) 
        store = store + i
    if ob == store:
        print('YES')
    else:
        print("NO")

# armstrongNumber(153)


# 2
def ArmstrongNumber(ob):
    convert = str(ob)
    store = 0
    for i in convert:
        i = int(i) ** 3
        store = store + i
    if ob == store:
        print('YES')
    else:
        print("NO")

# ArmstrongNumber(153)


# -------------------------------------------------------------------------------------------
'''
[14]
Given an integer, check whether it is a palindrome or not.

Example 1:

Input: n = 55555
Output: Yes


Example 2:

Input: n = 123
Output: No
'''

def is_palindrome(n):
	a = str(n)
	b = a[::-1]
	if a == b:
	    return "Yes"
	else:
		return "No"
# is_palindrome(121)

# ------------------------------------------------------------------------------------------

'''
[15]
Given a list of characters, merge all of them into a string.

Example 1:

Input:
N = 13
Char array = g e e k s f o r g e e k s
Output: geeksforgeeks 
Explanation: combined all the characters
to form a single string.
'''

def chartostr(arr):
    n = arr
    string = ''
    for i in n:
        string = string + i
    return string 
# chartostr(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'])

# -------------------------------------------------------------------------------------------

'''
[16]
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of
its index value ( Consider 1-based indexing ).

Example 1:

Input: 
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
'''

def valueEqualToIndex(arr, n):
	l1 = []
	for i in range(0, n):
		if arr[i] == i+1:
		    l1.append(arr[i])
	return l1
# valueEqualToIndex([15, 2, 45, 12, 7], 5)

# -------------------------------------------------------------------------------------------

'''
[17]
Given an array Arr[] of N integers.Find the sum of values of even and odd index positions separately.

Example 1:

Input:
N=5
Arr={1,2,3,4,5}
Output:
9 6
Explanation:
The sum of elements at odd places i.e
at 1st,3rd and 5th places are (1+3+5=9)
Similarly,the sum of elements at even 
places i.e. at 2nd and 4th places are
(2+4=6).
'''
# 1
def EvenOddSum(N,Arr):
    l1 = []
    sm1 = 0
    sm2 = 0
    for i in range(0, N):
        if i % 2 == 0:
            sm1 = sm1 + Arr[i]
        else:
            sm2 = sm2 + Arr[i]
    a,b = l1.append(sm1) ,l1.append(sm2)
    print(l1)

# EvenOddSum(5, [1,2,3,4,5])

# 2
def EvenOddSum2(N,Arr):
    l1 = []
    sm1 = 0
    sm2 = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            sm1 = sm1 + Arr[i]
        else:
            sm2 = sm2 + Arr[i]
    a,b = l1.append(sm1) ,l1.append(sm2)
    print(l1)

# EvenOddSum(5, [1,2,3,4,5])

# -------------------------------------------------------------------------------------------

'''
[18]
In a party of N people, each person is denoted by an integer. Couples are represented by the same number. 
Find out the only single person in the party of couples.

Example 1:

Input: N = 5
arr = {1, 2, 3, 2, 1}
Output: 3
Explaination: Only the number 3 is single
'''

# 1
def findSingle(N, arr):
    for i in range(0, N):
        c = 0
        for j in range(0, N):
            if arr[i] == arr[j]:
                c = c + 1

        if c % 2 != 0:
            print(arr[i])

# findSingle(5, [1, 2, 3, 2, 1])

# 2
def findSingle(arr):
    res = 0
    for i in arr:
        res = res ^ i
    print(res)

# findSingle([1, 2, 3, 2, 1])
# ---------------------------------------------------------------------------------------------


'''
[19]
Given two square matrices Grid1 and Grid2 with the same dimensions(NxN).Check whether they are identical or not.

Example 1:

Input:
N=2
Grid1=[[1,2],[3,4]]
Grid2=[[1,2],[3,4]]
Output:
1
Explanation:
Both the matrices are identical,
so the answer is 1.

Example 2:

Input:
N=2
Grid1=[[1,2][3,4]]
Grid2=[[1,2][3,2]]
Output:
0
Explanation:
Both the matrices are not identical,
So, answer is 0.
'''

Grid1=[[1,2],[3,4]]
Grid2=[[1,2],[3,4]]

def areMatricesidentical(Grid1,Grid2):
    if Grid1 == Grid2:
        print(1)
    else:
        print(0)
# areMatricesidentical([[1,2],[3,4]], [[1,2],[3,4]])

# --------------------------------------------------------------------------------------------

'''
[20]
Print numbers from 1 to N without the help of loops.

Example 1:
Input:
N = 10
Output: 1 2 3 4 5 6 7 8 9 10

Example 2:
Input:
N = 5
Output: 1 2 3 4 5
'''

# 1
def printNos(self,N):
    if(N>0):                   # The loop runs till N>1
        self.printNos(N-1)     # We keep on recursing till the end as we want to print from 1 to N
        print(N,end=" ")       # When recursion is done then print N


# 2
def printNos(N):
    if N > 0:
        printNos(N-1)
        print(N, end='')
# printNos(5)

# --------------------------------------------------------------------------------------------

