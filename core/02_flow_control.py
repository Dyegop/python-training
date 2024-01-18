"""
IF-ELSE:
    -If-else executes a statement if condition is True; otherwise it executes else condition
        if <condition>:
            statement 1
        else:
            statement 2

NESTED IF-ELSE:
    -Nested if-else works the same as 'if' statements, where whenever the 'if' block condition is
    false, then it checks to elif blocks. If all blocks are false, then it executes an else
    statement.
        if <condition1>:
            statement 1
        elif <condition2>:
            statement 2
        ...
        elif <conditionN>:
            statement N
        else:
            statement 3

FOR LOOP:
    -For loop statement iterates over a sequence(list, tuple or string) and executes statements
    until a given condition is True or the loop reaches the end of the sequence.
        for value in sequence:
            statement

WHILE LOOP:
    -While loop is used to iterate over the block of expression while condition is true.
        while <condition>:
            statement...

BREAK:
    -Break statement is used to break a loop in a certain condition.
        for value in sequence:
            statement
            if <condition>:
                break
            statement executed if <condition> is False

CONTINUE:
    -Continue statement won’t continue the loop, it executes statements until the condition
    matches True.
        while <condition>:
            statement 1
            if <condition>:
                continue
            statement executed if <condition> is True

PASS:
    -The pass contains a Null value. It is basically saying to the python compiler that does
    nothing.
        for value in sequence:
            pass
"""


# De-estructuring in a loop
# If you have a list of lists, such as friend names and ages, you can destructure in a loop:
friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:  # for friend in friends first
    print(f"{name} is {age} years old.")
