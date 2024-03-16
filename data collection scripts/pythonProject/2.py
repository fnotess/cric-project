# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # Implement your solution here

    # Sort the input array
    A.sort()

    # get the maximum value of the array which is last since array is sorted
    max_value = A[-1]
    counter = [0] * (max_value + 1)

    for i in range(len(A)):
        position = A[i]
        counter[position] += 1

    for j in range(len(A), 0, -1):
        if counter[j] == j:
            return j


    return 0

print(solution([5,5,5,5,5]))
#print(solution([3,8,2,3,3,2]))