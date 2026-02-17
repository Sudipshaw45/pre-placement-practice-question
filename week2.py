#q1
s = input().lower()

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels, ", Consonants =", consonants)

#q2
s = input()

if s == s[::-1]:
    print(True)
else:
    print(False)

#q3
s = input()
result = ""

for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)

#q4
s = input()
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key in freq:
    print(f"{key}:{freq[key]}", end=" ")


#q5
s = input()
result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)


#q6
s = input()
seen = set()

for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)

#q7
s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)


#q8
s = input()
result = ""

for ch in s:
    if ch.isdigit():
        result += "*"
    else:
        result += ch

print(result)


#q9
s = input()
words = s.split()
print(len(words))


#q10
s = input()
words = s.split()
reversed_words = words[::-1]

print(" ".join(reversed_words))

