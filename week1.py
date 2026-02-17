#q1
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max =", max_val, ", Min =", min_val)

#q2
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even, ", Odd =", odd)

#q3
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:")
print(*arr)

#q4
n = int(input())
arr = list(map(int, input().split()))

is_sorted = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print(is_sorted)

#q5
n = int(input())
arr = list(map(int, input().split()))

sum_even_index = 0

for i in range(0, n, 2):
    sum_even_index += arr[i]

print(sum_even_index)

#q6
n = int(input())
arr = list(map(int, input().split()))
key = int(input())

count = 0
for num in arr:
    if num == key:
        count += 1

print(count)

#q7
n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]

for i in range(1, n):
    if arr[i] > max_val:
        print(arr[i])
        break

#q8
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] < 0:
        arr[i] = 0

print(*arr)

#q9
n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)

total = sum(arr)

avg = (total - max_val - min_val) / (n - 2)

print(avg)

#q10

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

if arr1 == arr2:
    print(True)
else:
    print(False)

