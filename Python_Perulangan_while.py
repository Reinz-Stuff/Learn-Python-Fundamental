"""
Program perulangan membaca buku - for
"""

jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca = 0
print('Ibu berkata,"Baca semua bukumu."')
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1

    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")