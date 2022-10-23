"""
Program perulangan membaca buku - for
"""

total_books = 10
readed_books = 2
print('Ibu berkata,"Baca semua bukumu."')
print(f'jumlah buku yang sudah dibaca {readed_books}')

for readed_books in range(readed_books + 1, total_books + 1):
    print(f'Buku ke {readed_books} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {readed_books}')
