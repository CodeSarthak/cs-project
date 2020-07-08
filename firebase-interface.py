from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-interface-55bc7.firebaseio.com/", None)
data = {    
    'Name':'Helldcibdibo',
    'Email' :'test@gmail.com',
    'Number': 9599499407
}

result = firebase.post("python-interface-55bc7/test", data)
print(result)