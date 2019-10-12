from firebase import firebase

firebase = firebase.FirebaseApplication("https://stocktify.firebaseio.com/",None)

firebase.put("/produk/-LqzTgTwlOhacoRv--zN",'stok','458')
print('Update Succesfully')