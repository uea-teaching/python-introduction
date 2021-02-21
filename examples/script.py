import sys

def main():
    """process cmd line args"""
    print("Printing Args:")
    for i, arg in enumerate(sys.argv):
        print(f"Arg {i} is: '{arg}'")

main()
