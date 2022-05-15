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

total_milk = 0
total_eggs = 8

print(f"jumlah botol susu {total_milk} botol")
print(f"jumlah telur {total_eggs} butir")

if total_milk == 0:
    if total_eggs == 0:
        print(f'Budi tidak jadi membeli botol susu dan telur')
    elif total_eggs <= 6:
        print(f'Budi hanya membeli {total_eggs} butir telur')
    else:
        print('Budi hanya membeli 6 butir telur')

elif total_milk > 0:
    print('Budi mengecek harganya,dan uangnya cukup')
    if total_eggs == 0:
        print("Budi hanya membeli 1 botol susu")
    elif total_eggs <= 6:
        print(f'Budi membeli 1 botol susu dan {total_eggs} butir telur')
    else:
        print('Budi membeli 1 botol susu dan 6 butir telur')

print('Budi pulang ke rumah')
print('Dan menyampaikan hasil belanja kepada ibu')