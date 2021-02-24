# %%

with open("test.txt") as f:
    data = f.read()

# %%

try:
    file = open('test.txt')
except Exception:
    raise 
finally:
    file.close()

# %%

with open("out.txt", "w") as f:
    f.write("a line to write\n")

# %%

with open("test.txt") as f:
    data = f.readline()

print(data)

# %%

with open("test.txt") as f:
    data = f.readlines()

print(data)
# %%

with open("test.txt") as f:
    for line in f:
        print(line, end="")

# %%

with open("test.txt") as f:
    print(type(f))
    print(f.mode)
    
# %%

with open("missing.txt", "r") as f:
    pass

# %%

with open("test.txt") as f:
    while True:
        chunk = f.read(3)
        if not chunk:
            print("<end of file>")
            break
        print(chunk, end="*")

# %%


import json

s = '{"name": "red", "values": [255, 0, 0]}'
col = json.loads(s)

print(col["name"])


# %%

import json

col = dict(name="red", values=[255, 0, 0])
s = json.dumps(col)

print(s)

# %%

import json

with open("colours.json") as f:
    cold = json.load(f)

cols = json.dumps(cold, indent=4)
print(cols)

# %%

import json

col = dict(name="red", values=[255, 0, 0])

with open("red.json", "w") as f:
    json.dump(col, f)


# %%
