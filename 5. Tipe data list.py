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

daftar_anime = [86, 'Kimi no nawa', 3.54, -313]
print(type[daftar_anime])