"""
Semua sintaksis dasar bahasa pemograman terdiri dari :
1. Sekuensual : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial

print('Ibu berkata,"Pegi ke toko"')
print('Budi menjawab,"Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab,"Beli satu botol susu,jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Percabangan

jumlah_botol_susu = 173
jumlah_telur = 342
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print('Budi mengecek harganya,dan uangnya cukup')
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    elif jumlah_telur <= 6:
        print(f'Budi membeli 1 botol susu dan {jumlah_telur} butir telur')
    else :
        print('Budi membeli 1 botol susu dan 6 butir telur')

else:
    print('Budi tidak jadi membeli 1 botol susu')
print('Budi pulang ke rumah')
print('Dan menyampaikan hasil belanja kepada ibu')