"""
Program perulangan membaca buku - while undifined count
"""

total_books = 10
understood_books = 0
total_read = 0

print('Ibu berkata,"Bacalah semua bukumu sampai paham."')
print(f"Jumlah buku yang sudah dibaca {understood_books} ")

while total_read < total_books * 2:
    total_read = total_read + 1
    if understood_books == 9:
        print(f'Buku ke {understood_books + 1} belum paham')
    else:
        understood_books = understood_books + 1
        print(f'Buku ke {understood_books} sudah dipahami')

print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_books}")

if understood_books == total_books:
    print('Budi  lapor pada ibu,"Bu semua buku sudah dibaca dan dipahami."')
else:
    print('Budi  lapor pada ibu,"Bu tidak semua buku bisa dipahami."')