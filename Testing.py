daftar_list = [1, 2, 3, 4, 5]

daftar_list_baru = daftar_list[2::-2]

print('Daftar list awal')
for i in range(0, len(daftar_list)):
    print(daftar_list[i])

del daftar_list[:]

print('Nilai daftar list baru & Hapus daftar list')
for i in range(0, len(daftar_list_baru)):
    print(daftar_list_baru[i])

print(daftar_list)
