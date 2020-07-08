from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-interface-55bc7.firebaseio.com/", None)

firebase.put("python-interface-55bc7/users/-MACGVv25l8y1wQIYUU4", 'Name', 'Akshat')
print("done")
