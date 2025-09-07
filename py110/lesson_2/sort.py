import pprint

# Problem 1
lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))
print(sorted(lst, reverse=True))

# Expected Result
# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

# Problem 2
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# Expected Result
# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

# Problem 3
lst.sort(key=str)
print(lst)

lst.sort(key=str, reverse=True)
print(lst)

# Problem 4
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

# returning a new list
pprint.pp(sorted(books, key=lambda book: int(book['published'])))
print()

# mutating the list in place
books.sort(key=lambda book: int(book['published']))
pprint.pp(books)