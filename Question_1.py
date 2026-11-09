# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Note: I completed this exercise with help from Claude,
# as I have yet to learn Python. I am signing up for the SCTP course to
# build these skills properly. The comments below explain each step so I
# can follow and learn from the code.


# Task 1:
# A function that converts a temperature between Celsius and Fahrenheit.
#   value: the temperature number to convert
#   unit:  "C" means value is in Celsius, "F" means value is in Fahrenheit

def convertTemp(value, unit):
    # If the unit is "C", convert Celsius to Fahrenheit
    if unit == "C":
        result = (value * 9 / 5) + 32

    # If the unit is "F", convert Fahrenheit to Celsius
    elif unit == "F":
        result = (value - 32) * 5 / 9

    # Any other unit is invalid, so return -1 straight away.
    # We check the unit first, so an invalid value like "invalid"
    # never reaches the maths (which would cause an error).
    else:
        return -1

    # Round to 2 decimal places before returning
    return round(result, 2)


# Task 2:
# Call the function with the test inputs and print each result.

print(convertTemp(100, "C"))        # Expected: 212.0
print(convertTemp(32, "F"))         # Expected: 0.0
print(convertTemp(37, "C"))         # Expected: 98.6
print(convertTemp("invalid", "X"))  # Expected: -1