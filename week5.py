#q1
n = int(input())
arr = list(map(int, input().split()))
key = int(input())

for i in range(n):
    if arr[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")

#q2
n = int(input())
arr = list(map(int, input().split()))
key = int(input())

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Found")
else:
    print("Not Found")

#q3
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(*arr)

#q4
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(*arr)

#q5
n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(*arr)

#q6
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

arr.sort()
print(arr[k - 1])

#q7
n = int(input())
arr = list(map(int, input().split()))

swap_count = 0

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap_count += 1

print(swap_count)

#q8
n = int(input())
arr = list(map(int, input().split()))

if arr == sorted(arr):
    print(True)
else:
    print(False)

#q9
n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

merged = arr1 + arr2

print(*merged)

#q10
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if n % 2 == 1:
    print(arr[n // 2])
else:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
    print(median)
