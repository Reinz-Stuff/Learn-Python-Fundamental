"""
Program perulangan membaca buku - while
"""

total_books = 10
readed_books = 1

print('Ibu berkata,"Bacalah semua bukumu."')
print(f"Jumlah buku yang sudah dibaca {readed_books} ")

while readed_books < total_books:
    readed_books += 1
    print(f'Buku ke {readed_books} sudah dibaca')

print(f"Jumlah buku yang sudah dibaca {readed_books}")