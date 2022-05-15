"""
Program perulangan membaca buku - while
"""

total_books = 10
total_readed_books = 6

print('Ibu berkata,"Bacalah semua bukumu."')
print(f"Jumlah buku yang sudah dibaca {total_readed_books} ")

while total_readed_books < total_books:
    total_readed_books = total_readed_books + 1
    print(f'Buku ke {total_readed_books} sudah dibaca')

print(f"Jumlah buku yang sudah dibaca {total_readed_books}")