# %%  Can't modify a tuple

fruits = ("apple", "banana", "cherry")
fruits[0] = "orange"

# %% can modify a list

fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"
print(fruits)

# %%

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[2:5])

# %%

letters = ["a", "b", "c"]
print(letters[:2])

# %%

letters = ["a", "b", "c"]
print(letters[3])

# %%

letters = ["a", "b", "c"]
print(letters[1:3])

# %%

letters = ["a", "b", "c"]
print(letters[1:])

# %%

letters = ["a", "b", "c"]
print(letters[::-1])


# %%

letters = ["a", "b", "c", "d", "e", "f", "g"]

for letter in letters:
    print(letter, end=" ")


# %%

letters = ["a", "b", "c", "d"]
fruits = ["apple", "banana", "cherry", "orange"]

for i, letter in enumerate(letters):
    print(letter, fruits[i], end=" ")


# %%

letters = ["a", "b", "c", "d"]
fruits = ["apple", "banana", "cherry", "orange"]

for letter, fruit in zip(letters, fruits):
    print(letter, fruit, end=" ")


# %%

squared = [x**2 for x in range(1, 5)]
print(squared)

# %%

squared_even = [x**2 for x in range(1, 9) if x % 2 == 0]
print(squared_even)

# %%

numbers = [1, 2]
letters = ["a", "b"]
nested = [(i, j) for i in numbers for j in letters]

print(nested)

# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# %%
