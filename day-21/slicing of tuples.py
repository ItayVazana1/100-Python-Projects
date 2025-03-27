# Tuples in Python are immutable, ordered collections often used to store fixed sets of related values, such as coordinates (x, y), RGB color values (r, g, b),
# or grouped data from a database row or function return. Their immutability makes them more memory-efficient and safer for use as keys in dictionaries.

# Although tuples cannot be changed once created, Python allows you to retrieve parts of a tuple using slicing — a common and powerful feature.
# Slicing creates a new tuple containing a subset of the original elements, using the familiar syntax: tuple[start:stop:step].

# Here's a breakdown of how slicing works:
# - `start`: the index to begin from (inclusive)
# - `stop`: the index to stop at (exclusive)
# - `step`: optional, determines the stride or gap between elements

# Example 1: Basic slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])  # Output: (20, 30, 40) → includes index 1, 2, 3 but not 4

# Example 2: Omitting start/stop
print(t[:3])   # Output: (10, 20, 30) → from beginning to index 2
print(t[2:])   # Output: (30, 40, 50) → from index 2 to the end

# Example 3: Using step
print(t[::2])  # Output: (10, 30, 50) → every second item
print(t[::-1]) # Output: (50, 40, 30, 20, 10) → reversed tuple

# Slicing is especially useful when:
# - You want to copy a tuple or part of it without modifying the original.
# - You want to skip certain elements or reverse the order.
# - You're processing structured data and need only a portion of the fields.

# Example 4: Ignoring fields in data unpacking
data = ("John", "Doe", 30, "New York")
name = data[:2]          # ("John", "Doe")
location = data[3:]      # ("New York",)
print(name, location)

# Remember: slicing always returns a new tuple and does not affect the original.
# This fits perfectly with the immutable nature of tuples, and ensures safe manipulation without side effects.