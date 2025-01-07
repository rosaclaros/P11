# Default behavior
text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"

# Specified characters
text = "---Hello---"
print(text.strip("-"))  # Output: "Hello"
        

# String to list
#.split(separator, max)
text = "Hello World Python"
print(text.split())  # Output: ['Hello', 'World', 'Python']

# Specified separator
text = "apple,banana,cherry"
print(text.split(','))  # Output: ['apple', 'banana', 'cherry']

# Using maxsplit
text = "one:two:three:four"
print(text.split(':', 2))  # Output: ['one', 'two', 'three:four']

# Default behavior
text = "Hello World Python"
print(text.split())  # Output: ['Hello', 'World', 'Python']

# Specified separator
text = "apple,banana,cherry"
print(text.split(','))  # Output: ['apple', 'banana', 'cherry']

# Using maxsplit
text = "one:two:three:four"
print(text.split(':', 2))  # Output: ['one', 'two', 'three:four']