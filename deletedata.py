from firebase import firebase

firebase = firebase.FirebaseApplication("https://stocktify.firebaseio.com/",None)

firebase.delete('/produk','-LqzTgTwlOhacoRv--zN')
print('Delete Succesfully')