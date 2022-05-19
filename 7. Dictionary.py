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