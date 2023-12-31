# -*- coding: utf-8 -*-
"""assignment 9 prep

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BbHGkn1GL2Gd8ccpvXILgZcTMD3EfTBB
"""

#1 solution

import math

def is_power_of_two(n):
    if n <= 0:
        return False
    return math.log2(n).is_integer()

#2 solution

def sum_of_natural_numbers(n):
    sum = (n * (n + 1)) // 2
    return sum

print(sum_of_natural_numbers(3))  # 1 + 2 + 3 = 6
print(sum_of_natural_numbers(5))  # 1 + 2 + 3 + 4 + 5 = 15

#solution3

def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

print(factorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120
print(factorial(4))  # 4! = 4 * 3 * 2 * 1 = 24

#solution4

def exponent(N, P):
    result = N ** P
    return result

print(exponent(5, 2))  # 5^2 = 25
print(exponent(2, 5))  # 2^5 = 32

#solution 5

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], find_max(arr[1:]))

# Test the function with the given inputs
arr1 = [1, 4, 3, -5, -4, 8, 6]
print(find_max(arr1))  # Output: 8

arr2 = [1, 4, 45, 6, 10, -8]
print(find_max(arr2))  # Output: 45

#solution 6

def find_nth_term(a, d, N):
    nth_term = a + (N - 1) * d
    return nth_term

# Test the function with the given inputs
a1 = 2
d1 = 1
N1 = 5
print("The", N1, "term of the series is:", find_nth_term(a1, d1, N1))  # Output: 6

a2 = 5
d2 = 2
N2 = 10
print("The", N2, "term of the series is:", find_nth_term(a2, d2, N2))  # Output: 23

#solution 7

def permutations(string):
    if len(string) == 1:
        return [string]

    perms = []
    for i in range(len(string)):
        char = string[i]
        remaining = string[:i] + string[i+1:]
        for perm in permutations(remaining):
            perms.append(char + perm)

    return perms

# Test the function with the given inputs
S1 = "ABC"
print("Permutations of", S1, ":", permutations(S1))

S2 = "XY"
print("Permutations of", S2, ":", permutations(S2))

#8 solution

def permutations(string):
    if len(string) == 1:
        return [string]

    perms = []
    for i in range(len(string)):
        char = string[i]
        remaining = string[:i] + string[i+1:]
        for perm in permutations(remaining):
            perms.append(char + perm)

    return perms

# Test the function with the given inputs
S1 = "ABC"
print("Permutations of", S1, ":", permutations(S1))

S2 = "XY"
print("Permutations of", S2, ":", permutations(S2))

