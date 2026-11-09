# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Note: I completed this exercise with help from Claude,
# as I have yet to learn Python. I am signing up for the SCTP course to
# build these skills properly. The comments below explain each step so I
# can follow and learn from the code.


# Task 1:
# Create an empty list to hold the item names.
# Square brackets [] with nothing inside means an empty list.

inventory = []


# Task 2:
# Add an item to the inventory, but only if it is not already there.

def addItem(itemName):
    # "in" checks whether the item is already somewhere in the list
    if itemName in inventory:
        # Item exists, so show a message and do not add it again
        print(itemName + " is already in inventory.")
    else:
        # Item is new, so append() adds it to the end of the list
        inventory.append(itemName)


# Task 3:
# Show everything in the inventory.

def listInventory():
    # len() gives the number of items in the list.
    # If it is 0, the list is empty.
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        # Print the whole list on one line, matching the expected output
        print("Inventory:", inventory)


# Task 4:
# Call the functions in this order and observe the output.

addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']