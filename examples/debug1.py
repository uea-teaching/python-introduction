numbers = [500, 600, 700]
letters = ['x', 'y', 'z']


def nested_loop():
    for number in numbers:
        print(number)
        for letter in letters:
            print(letter)

if __name__ == '__main__':
    nested_loop()
