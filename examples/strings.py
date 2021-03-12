# %%
"""string examples"""

s = "Hello, World!"

print(s.upper())
print(s.lower())
print(s.islower())
print(s.isupper())


# %%

s = "Hello, World!"

print("a" in s)
print("a" not in s)
print("llo" in s)

# %%

s = "Hello, World!"

print(s.split(","))

# %%

parts = ["one", "two", "three"]
print(", ".join(parts))

# %%

age = 42
txt = "Bob is {} years old"
print(txt.format(age))

# %%

age = 42
txt = "Bob is {0} years old, Alice is also {0}!"
print(txt.format(age))

# %%

alice = 24
bob = 42
txt = "Bob is {b} years old, Alice is really {a}!"
print(txt.format(a=alice, b=bob))

# %%

name = "Bob"
txt = f"{name} is {6 * 7} years old."
print(txt)

# %%

pad = 3
big = 2**24
dec = 123.123456789
txt = f"big: {big:,} floats: {dec:0.5f}, padding: {pad:04d}"
print(txt)

# %%

s = r"if I want to use\nanother line..."
print(s)

# %%

s = "if I want to \"quote\" Alice\'s work..."
print(s)

# %%
