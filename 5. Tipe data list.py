# Type data list
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']

print('1.Tampilkan semua variable daftar anime')
print(daftar_anime)

print('\n2.Proses dengan for in')
for i in daftar_anime:
    print(i)

print('\n3.Tamplikan isi dari daftar anime pada indeks tertentu')
print(daftar_anime[0])
print(daftar_anime[2])

print('\n4.Tamplikan isi dari daftar anime menggunakan in range')
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n5.Tamplikan isi dari daftar anime '
      'menggunakan in range dengan type data berbeda')
daftar_anime = [86, 'Kimi no nawa', 3.54, -313]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n6.Memambahkan data pada list')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
daftar_anime.append('Code Geass')
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n7.Menghapus data pada list dengan clear')
daftar_anime.clear()
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n8.Ganti Elemen Pertama')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
daftar_anime[0] = 'Naruto'
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n9.Mengambil Elemen')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
buku = daftar_anime.pop(1)
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n10.Elemen yang diambil tadi')
print(buku)
# Pop tanpa angka maka diambil dari ujung, jika angka negatif dihitung dari ujung

print('\n11.Pop')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
buku = daftar_anime.pop()
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\n12.Pop -1')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
buku = daftar_anime.pop(-2)
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

