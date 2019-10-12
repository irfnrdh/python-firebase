from firebase import firebase

firebase = firebase.FirebaseApplication("https://stocktify.firebaseio.com/",None)


data = {
    'SKU': 'ENT124',
    'nama':'Tas Wanita',
    'stok': 98
}

result = firebase.post("/produk/1",data)

print(result)