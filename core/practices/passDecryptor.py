import random
import sys


# Figure out a password that will authenticate the program
#
#
#
def main():
    if len(sys.argv) != 2:
        print("Invalid args")
        return
    password = sys.argv[1]
    builder = 0
    for c in password:
        builder += ord(c)
    if builder == 1000 and len(password) == 10 and ord(password[1]) == 83:
        print("correct")
    else:
        print("incorrect")

if __name__ == "main":
    main()


# Key generator for main
def pass_decryptor():
    total = 1000 - 83
    while True:
        randomlist = random.sample(range(0, 127), 9)
        if sum(randomlist) == total:
            result = [chr(i) for i in randomlist]
            result.insert(1, chr(83))
            return ''.join(result)

for i in range(0, 10):
    print(pass_decryptor())





