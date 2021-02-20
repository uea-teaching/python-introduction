"""Demonstrate user input"""

while True:
    value = input("Enter a value, or type 'q' to quit: ")
    if value == "q":
        print("Quitting...")
        break
    print("You entered: ", value)
