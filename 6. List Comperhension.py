print('\nPerintah del')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
del daftar_anime[0]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nPerintah del dengan list comprehension')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
del daftar_anime[:]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nPerintah del dengan list comprehension start')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
del daftar_anime[0:-2]  # [START:END]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nPerintah del dengan list comprehension step')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
del daftar_anime[0::2]  # [START:END:STEP]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nMembuat list baru')
daftar_anime = ['Overlord', 'Kingdom', 'Oregairu', 'One Puch Man']
daftar_anime_baru = daftar_anime[:]  # [START : END]
for i in range(0, len(daftar_anime)):
    print(daftar_anime[i])

print('\nMembuat list baru')
del daftar_anime[:]
for i in range(0, len(daftar_anime_baru)):
    print(daftar_anime_baru[i])

print('\nMembuat list baru dengan comperhension: Ganjil')
daftar_anime = ['1 Overlord', '2 Kingdom', '3 Oregairu', '4 One Puch Man']
daftar_anime_baru = daftar_anime[0::2]  # [START : END]
for i in range(0, len(daftar_anime_baru)):
    print(daftar_anime_baru[i])

print('\nMembuat list baru dengan comperhension: Genap')
daftar_anime = ['1 Overlord', '2 Kingdom', '3 Oregairu', '4 One Puch Man']
daftar_anime_baru = daftar_anime[1::2]  # [START : END]
for i in range(0, len(daftar_anime_baru)):
    print(daftar_anime_baru[i])

print('\nMembuat list baru dengan comperhension: Print')
daftar_anime = ['1 Overlord', '2 Kingdom', '3 Oregairu', '4 One Puch Man']
print(daftar_anime[0::2])
