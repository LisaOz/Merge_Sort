'''
This is a Python script to demonstrate the sorting of an array
using the merge sort algorithm.
'''

def merge_sort(A):
    # Edge case when an array consists of 1 element or is empty
    if len(A) <= 1:
        return

    # Split array into two:
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    merge(A, L, R)


def merge(A, L, R):
    i = j = k = 0

    # copy data o temporal arrays
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Check if any element is left on L
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    # Check if any element is left in R
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    B = [5, 2, 6, 7, 3, 4, 9]
    merge_sort(B)
    print(*B)
