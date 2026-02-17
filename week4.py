#q1
n = int(input())
arr = list(map(int, input().split()))

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)

#q2
n = int(input())
arr = list(map(int, input().split()))

result = [num for num in arr if num != 0]
zeros = [0] * arr.count(0)

print(*(result + zeros))

#q3
n = int(input())
arr = list(map(int, input().split()))

print(max(arr) - min(arr))

#q4
n = int(input())
arr = list(map(int, input().split()))

print(len(set(arr)))

#q5
n = int(input())
arr = list(map(int, input().split()))

seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(*duplicates)

#q6
n = int(input())
arr = list(map(int, input().split()))

arr = [arr[-1]] + arr[:-1]

print(*arr)

#q7
n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    print(arr[i] + arr[i + 1], end=" ")

#q8
n = int(input())
arr = list(map(int, input().split()))

if len(arr) != len(set(arr)):
    print(True)
else:
    print(False)

#q9
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] < 0:
        print(i)
        break

#q10
n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)

result = [total - num for num in arr]

print(*result)

