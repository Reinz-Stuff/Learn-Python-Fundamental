# JSON wajib menggunakan petik dua
users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Brett",
    "email": "sincere@april.biz",  # email : key, tidak boleh angka harus string
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }

    }
}

print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]['street'])
print(users["address"]['geo'])
print(users["address"]['geo']['lat'])

print(users)
print(type(users))

# Diatas merupakan Dictonary dan bukan JSON meskipun tampilan sama, untuk merubah dictionary ke JSON maka harus
# menggunakan package bawaan python yg bernama "JSON" dan harus dipanggil dahulu menggunakan perintah import

print('Ubah Dict ke json')

# dumps = mengubah dictionary menjadi string JSON, dump = mengubah dictonary menjadi file JSON

import json
result = json.dumps(users)
print(result)
print(type(result))

with open('result.json', 'w') as file:
    json.dump(users, file)

# Code -> Reformat code, agar tampilan sama
