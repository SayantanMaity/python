# WAPP to find the largest element from a list
n = int(input('Enter the no. of elements to input: '))

x = []
for i in range(n):
    element = int(input(f'Enter element {i + 1}: '))
    x.append(element)

largest = x[0]
for i in x:
    if largest < i:
        largest = i

print("Largest element in the list:", largest)