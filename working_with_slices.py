
list_of_books = [
    {'id': 1},
    {'id': 2},
    {'id': 3},
    {'id': 4},
    {'id': 5},
    {'id': 6},
    {'id': 7},
]

skip_elem = list_of_books[1:]
print(skip_elem)

limit = list_of_books[:5]
print(limit)

sliced = list_of_books[1:][:5]
print(sliced)