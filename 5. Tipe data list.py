# Type data list
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']

print('Tampilkan semua variable daftar anime')
for i in daftar_anime:
    print(i)

print('\nProses dengan for in')
print(daftar_anime[0])
for i in daftar_anime:
    print(i)

print('\nTamplikan isi dari daftar anime pada indeks tertentu')
print(daftar_anime[2])

print('\nTamplikan isi dari daftar anime menggunakan in range')
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nTamplikan isi dari daftar anime '
      'menggunakan in range dengan type data berbeda')
daftar_anime = [86, 'Kimi no nawa', 3.54, -313]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nMemambahkan data pada list')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
daftar_anime.append('Code Geass')
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nMenghapus data pada list dengan clear')
daftar_anime.clear()
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nGanti Elemen Pertama')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
daftar_anime[0] = 'Naruto'
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nMengambil Elemen')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
buku = daftar_anime.pop(1)
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nElemen yang diambil tadi')
print(buku)
#Pop tanpa angka maka diambil dari ujung, jika angka negatif dihitung dari ujung

