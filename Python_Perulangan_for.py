"""
Program perulangan membaca buku - for
"""

total_books = 10
total_readed_books = 6
print('Ibu berkata,"Baca semua bukumu."')
print(f'jumlah buku yang sudah dibaca {total_readed_books}')

for total_readed_books in range(total_readed_books + 1, total_books + 1):
    print(f'Buku ke {total_readed_books} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {total_readed_books}')