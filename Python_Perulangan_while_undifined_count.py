"""
Program perulangan membaca buku - while undifined count
"""

jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca = 0

print('Ibu berkata,"Bacalah semua bukumu sampai paham."')
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca_dan_dipahami} ")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f'Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami+1} belum paham')
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami +1
        print(f'Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dipahami')

print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")