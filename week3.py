#q1
n = int(input())

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#q2
n = int(input())
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n //= 10

print(sum_digits)

#q3
n = int(input())
original = n
reverse = 0

while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10

print(original == reverse)

#q4
n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

#q5
n = int(input())
original = n
sum_cubes = 0

while n > 0:
    digit = n % 10
    sum_cubes += digit ** 3
    n //= 10

print(original == sum_cubes)

#q6
a, b = map(int, input().split())

while b != 0:
    a, b = b, a % b

print(a)

#q7
a, b = map(int, input().split())

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print(lcm)

#q8
n = int(input())
count = 0

while n != 0:
    count += 1
    n //= 10

print(count)

#q9
n = int(input())
sum_div = 0

for i in range(1, n):
    if n % i == 0:
        sum_div += i

print(sum_div == n)

#q10
n = int(input())

for num in range(2, n + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
