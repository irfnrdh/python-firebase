from firebase import firebase

firebase = firebase.FirebaseApplication("https://stocktify.firebaseio.com/",None)

result = firebase.get('/produk',None)
print(result)