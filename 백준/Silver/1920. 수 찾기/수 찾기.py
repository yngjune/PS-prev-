from sys import stdin

def binary_search(arr, target):
    left, right = 0, N - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

N = int(input())
arr = list(map(int, stdin.readline().split()))
arr.sort()
M = int(input())
search = list(map(int, stdin.readline().split()))

for i in range(M):
    print(binary_search(arr, search[i]))