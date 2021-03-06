"""
Calculate the number of distinct values in an array A.
"""

def solution_pythonic(A):
	return len(set(A))

def solution(A):
    if not A:
	return 0
    A.sort()
    count = 1
    previous = A[0]
    for element in A:
        if element > previous:
            count += 1
        previous = element
    return count
