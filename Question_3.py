# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Note: I completed this exercise with help from Claude,
# as I have yet to learn Python. I am signing up for the SCTP course to
# build these skills properly. The comments below explain each step so I
# can follow and learn from the code.


# Task 1:
# Return the name as "lastName, firstName".
# The test "bob", "lim" expects "Lim, Bob", so each name also needs
# its first letter capitalised.

def formatName(firstName, lastName):
    # capitalize() makes the first letter uppercase and the rest lowercase,
    # so "bob", "BOB" and "bOb" all become "Bob"
    first = firstName.capitalize()
    last = lastName.capitalize()

    # Join the two names with a comma and a space in between
    return last + ", " + first


# Task 2:
# Return the initials in uppercase, e.g. "J.S."

def formatInitials(firstName, lastName):
    # [0] picks the first character of a string ("john"[0] is "j")
    # upper() turns it into a capital letter, whatever case it started in
    firstInitial = firstName[0].upper()
    lastInitial = lastName[0].upper()

    # Put a full stop after each initial
    return firstInitial + "." + lastInitial + "."


# Task 3:
# Call both functions with the test inputs and print each result.

print(formatName("Alice", "Tan"))      # Expected: Tan, Alice
print(formatName("bob", "lim"))        # Expected: Lim, Bob
print(formatInitials("Alice", "Tan"))  # Expected: A.T.
print(formatInitials("bob", "lim"))    # Expected: B.L.