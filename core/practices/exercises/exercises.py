import string
import math
import random
from collections import Counter

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for i in st.split():
    a = len(i)
    if i[0].lower() == 's' and a > 1:
        print(i)


# Use range() to print all the even numbers from 0 to 10.
for i in range(0, 11, 2):
    print(i)


# Use a List Comprehension to create a list of numbers between 1 and 50 that are divisible by 3.
lista1 = [i for i in range(1, 51) if i % 3 == 0]
print(lista1)


# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for i in st.split():
    if len(i) % 2 == 0:
        print(i + " is even")


# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five
# print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
mylist = [i[0] for i in st.split()]
print(mylist)


# If word starts with a vowel, add 'ay' to the end. If word does not start with a vowel,
# put first letter at the end, then add 'ay'.
while True:
    a = input("Please type a word: ")
    if a == "ESCAPE":
        break

    def pig_latin(word='NAME'):
        vowel = ("a", "e", "i", "o", "u")
        tail = "ay"
        if word[0] in vowel:
            pig_word = (word + tail)
        else:
            pig_word = (word[1:] + word[0] + tail)
        return pig_word.lower()

    print(pig_latin(a))


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both
# numbers are even, but returns the greater if one or both numbers are odd
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def lesser_of_two_evens(a, b):
    if is_even(a) and is_even(b) is True:
        return min(a, b)
    if is_even(a) or is_even(b) is False:
        return max(a, b)

x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))
print(lesser_of_two_evens(x, y))


# String exercise
def animal_crackers(text):
    my_list = text.split()
    for i in my_list:
        if my_list[i][0] == my_list[i + 1][0]:
            return True
        else:
            return False

typetype = input("Introduce un string: ")
print(animal_crackers(typetype))


# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of
# that letter
while True:
    def print_big(letter):
        my_dict = {
            1: "*****",
            2: "*",
            3: "    *",
            4: "****",
            5: "  **",
            6: "  *  ",
            7: "***",
            8: "   *",
            9: " *** "
        }
        if letter == 'd':
            print(my_dict[4])
            print(my_dict[2] + my_dict[3])
            print(my_dict[2] + my_dict[3])
            print(my_dict[2] + my_dict[3])
            print(my_dict[4])
        if letter == 'i':
            print(my_dict[9])
            print(my_dict[6])
            print(my_dict[6])
            print(my_dict[6])
            print(my_dict[9])
        if letter == 'e':
            print(my_dict[1])
            print(my_dict[2])
            print(my_dict[7])
            print(my_dict[2])
            print(my_dict[1])
        if letter == 'g':
            print(my_dict[1])
            print(my_dict[2])
            print(my_dict[2] + my_dict[5])
            print(my_dict[2] + my_dict[8])
            print(my_dict[1])
        if letter == 'o':
            print(my_dict[1])
            print(my_dict[2] + my_dict[8])
            print(my_dict[2] + my_dict[8])
            print(my_dict[2] + my_dict[8])
            print(my_dict[1])

    a = input("")
    print_big(a)
    if a == 'ESC':
        break


# PAPER DOLL: Given a string, return a string where for every character in the original there are
# three characters
def paper_doll(text):
    mylist1 = []
    for i in text:
        mylist1.append(i * 3)
    print(''.join(mylist1))


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST
def blackjack(a, b, c):
    mylist2 = [a, b, c]
    suma = sum(mylist2)
    if suma <= 21:
        return suma
    elif a == 11 or b == 11 or c == 11:
        dif = suma - 10
        if dif <= 21:
            return dif
        if dif > 21:
            return "BUST"
    else:
        return "BUST"

print(blackjack(9, 9, 11))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and
# including a given number
def count_primes(num):
    count = 0
    add = True
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                return add
            else:
                add = False
                return add
        if add:
            count += 1
    return count

print(count_primes(10))


# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    volume = (4 / 3) * math.pi * (rad ** 3)
    return volume

print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    return high > num > low

print(ran_check(5, 2, 7))


# Write a Python function that accepts a string and calculates the number of upper case letters
# and lower case letters.
def up_low(s):
    c = Counter(s)
    upper = 0
    lower = 0
    for i in c:
        if i.isupper():
            upper += c[i]
        if i.islower():
            lower += c[i]
    print("No. of Upper case characters ", upper)
    print("No. of Lower case characters ", lower)

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# Write a Python function that takes a list and returns a new list with unique elements of the
# first list.
def unique_list(lst):
    unique2 = list(set(lst))
    return unique2

print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    a = 1
    for i in range(0, len(numbers)):
        a *= numbers[i]
    return a

print(multiply([1, 2, 3, -4]))


# Write a Python function that checks whether a passed in string is palindrome or not. 
def palindrome(s):
    a = s[::-1]
    b = s[::]
    print(a, b)
    if a == b:
        return True
    else:
        return False

print(palindrome('madam or nurses run'))


# Write a Python function to check whether a string is pangram or not.
# Note: Pangrams are words or sentences containing every letter of the alphabet at least once.

def ispangram(str1, alphabet=string.ascii_lowercase):
    test = []
    for char in str1:
        if char in test:
            pass
        else:
            if char in alphabet:
                test.append(char)
    for char2 in alphabet:
        if char2 in test:
            return True
        else:
            return False

print(ispangram("The quick brown fox jumps over the lazy dog"))


# Write a Python function to check whether a string is pangram or no
def ispangram(str1, alphabet=string.ascii_lowercase):
    a = list(alphabet)
    for i in str1.lower():
        if i in a:
            a.remove(i)
    if len(a) == 0:
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))


# Create a generator that generates the squares of numbers up to some number N
def gensquares(n):
    for x in range(n):
        yield x ** 2

for i in gensquares(10):
    print(i)


# Create a generator that yields "n" random numbers between a low and high number (that are
# inputs).
def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

for i in rand_num(1, 10, 5):
    print(i)

# Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_iter = iter(s)


# Generator comprehension:
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
