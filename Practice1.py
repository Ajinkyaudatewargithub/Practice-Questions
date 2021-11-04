'''
[1]
Given two positive integers num1 and num2, the task is to find the remainder when num1 is divided by num2.

Example 1:

Input:
num1 = 5
num2 = 3

Output:
2

Explanation:
The remainder after dividing 5 by 3 is: 2
'''

def findRemainder(num1, num2):
    a = num1 % num2
    print(a)
# findRemainder(5, 10)

# -------------------------------------------------------------------------------------------------------- #
    
'''
[2]
You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.

Example 1:

Input:
N = 6
Output:
1
Explanation:
For dice facing number 6 opposite face
will have the number 1.
'''
def oppositeFaceOfDice(N):
    if N <= 6:
        dice = ( 6 - N ) + 1
        print(dice)
    else:
        print("please enter number in range from 1 to 6")

# oppositeFaceOfDice(6)

# -------------------------------------------------------------------------------------------------------- #

'''
[3]
Given a number, N. Find the sum of all the digits of N
 

Example 1:

Input:
N = 12
Output:
3
Explanation:
Sum of 12's digits:
1 + 2 = 3
'''

def sumOfDigits(N):
    sum = 0
    for i in N:
        sum = sum + int(i)
    return sum

# sumOfDigits('12')

# -------------------------------------------------------------------------------------------------------- #

'''
[4]
Given the marks of N students in an Array A, calculate the mean.

Note: If result is a Decimal Value, find it's floor Value.

Example 1:

Input:
N = 4 
A = { 56 , 67 , 30 , 79 }
Output:
58
Explanation:
56+67+30+79 = 232;  232/4 = 58.
So, the Output is 58.
'''
A = { 56 , 67 , 30 , 79 }
def mean(A, N):
    mean = 0
    for i in A:
        mean = mean + i
        avgMean = mean // N
    return avgMean

# mean({ 56 , 67 , 30 , 79 }, 4)

# -------------------------------------------------------------------------------------------------------- #

'''
[5]
Given an array of N integers. Your task is to print the sum of all of the integers.
 

Example 1:

Input:
4
1 2 3 4
Output:
10

 

Example 2:

Input:
6
5 8 3 10 22 45
Output:
93
'''

def getSum(arr):
    arrSum = 0 
    for i in arr:
        arrSum = arrSum + i
    return arrSum

array = [1, 2, 3, 4]    
# getSum(array)

# -------------------------------------------------------------------------------------------------------- #


'''
[6]
Print the multiplication table of a given number N. 


Example 1:

Input:
N = 9

Output:
9 18 27 36 45 54 63 72 81 90
'''

def getTable(N):
    M = range(1, 11)
    for i in M:
        i = i * N
        print(i, end=' ')
# getTable(9)

# -------------------------------------------------------------------------------------------------------- #

'''
[7]
Given a string. Count the number of Camel Case characters in it.

Example 1:

Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.
'''

def countCamelCase (s):
    count = 0
    for i in s:
        if i == i.upper():
            count = count + 1
    return count

# countCamelCase('hELLO')

# -------------------------------------------------------------------------------------------------------- #

'''
[8]
Given a number N, find the Nth term in the series 1, 3, 6, 10, 15, 21…

Example 1:

Input :
N = 4 
Output:
10
Explanation:
The 4th term of the Series is 10.
'''
# Program to print 'n' number of series
# a = 10
# i = 0
# for j in range(1, a):
#     i = i+j
#     print(i)

def findNthTerm(N):
    series = 0
    listNthTerm = []
    for i in range(1, N+1):
        series = series + i
        listNthTerm.append(series)
    print(listNthTerm[N-1])

# findNthTerm(4)  

# Formula for finding the nth term for this problem : n*(n+1)//2
# -------------------------------------------------------------------------------------------------------- #

'''
[9]
Given a string, remove spaces from it. 

Example 1:

Input:
S = "geeks  for geeks"
Output: geeksforgeeks
Explanation: All the spaces have been 
removed.

'''

def modify(s):
    check = s.split()
    sen = ''
    for i in check:
        sen = sen + i
    return sen
# print(modify('Sa na'))


'''
[10]
Given a list of names, display the longest name.

Example:

Input:
N = 5
names[] = { "Geek", "Geeks", "Geeksfor",
  "GeeksforGeek", "GeeksforGeeks" }

Output:
GeeksforGeeks
'''

names = { "Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks" }
a = []
for i in names:
    if len(i) > 0:
        a.append(i)
print(max(a))

print(max(names))

