"""
Lambdas are a concise way to define anonymous functions in Python. 
They are ideal for short, one-line expressions 
that you intend to use within your code without the need for a full-fledged named function.
"""
anoAtual = 2024
idade = lambda dataNascimento: anoAtual - int(dataNascimento.split('/')[2]) 

i = idade('15/11/2000')

print(f'Idade Aproximada: {i}')

#Lambdas are commonly used by being passed as key function for other method to execute, 
#determining how will this method work

#Example 1:
numbers = [3, 1, 4, 5, 2]
sorted_numbers = sorted(numbers, key=lambda x: x % 2)  # Sort by remainder when divided by 2
print(sorted_numbers)  # Output: [2, 4, 1, 3, 5]

#Example 2:
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 22}]
adults = list(filter(lambda person: person["age"] >= 21, data))  # Filter adults
print(adults)  # Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

#Example 3:
strings = ["hello", "world", "how", "are", "you"]
uppercased = (map(lambda word: word.upper(), strings))  # Convert to uppercase
print(list(uppercased))  # Output: ['HELLO', 'WORLD', 'HOW', 'ARE', 'YOU']