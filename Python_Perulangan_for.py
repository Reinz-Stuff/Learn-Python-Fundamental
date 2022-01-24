"""
Program perulangan membaca buku
"""

jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca = 6
print('Ibu berkata,"Baca semua bukumu."')
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

for jumlah_buku_yang_sudah_dibaca in range(jumlah_buku_yang_sudah_dibaca+1, jumlah_buku+1):
    print(f'Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')