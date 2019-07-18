for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

newsquares = [value**2 for value in range(1,11)]
print(newsquares)