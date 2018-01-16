animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

print("cat")
print("dog")
print("frog")
print("Hello")

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
print(animals)
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print(animals) # Observe what prints after the insert operation


# FOR Loop
my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
    # Your code here
    print(2 * number)


start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print(square_list)


