from tkinter.ttk import *
from tkinter import *
window=Tk()
window.geometry('750x600')
admno=Label(text='Enter your admission no.',fg='white',bg='red')
admno.grid(column=0,row=0)
entry1=Entry(fg='white',bg='grey',width=20)
entry1.grid(column=0,row=1)
password=Label(text='Enter your password',fg='white',bg='red')
password.grid(column=0,row=2)
entry2=Entry(fg='white',bg='grey',width=20)
entry2.grid(column=0,row=3)
phonenumber=Label(text='Enter your phone no.',fg='white',bg='red')
phonenumber.grid(column=0,row=4)
entry3=Entry(fg='white',bg='grey',width=20)
entry3.grid(column=0,row=5)
branch= Listbox(window)
branch.insert(1,'AISG43')
branch.insert(2,'AISG46')
branch.insert(3,'AISSAKET')
branch.grid(column=0,row=6)
def func():
    from firebase import firebase
    import http 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    firebase = firebase.FirebaseApplication("https://python-interface-55bc7.firebaseio.com/", None)
    result = firebase.get("python-interface-55bc7/test", '')
    dict1 = {'Hi':1, "Hello":2}
    akshat = str(list(result.values())[1]["Number"])
    chrome_options = Options()  
#chrome_options.add_argument("--headless") 
    # url = "https://web.whatsapp.com/send?phone=+91"+akshat
    # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),  options =  chrome_options)  
    # driver.maximize_window()
    # driver.get(url)
    # username_textbox = driver.find_element_by_id("_3FRCZ copyable-text selectable-text")


bt=Button(text='submit',command=func())


    firebase = firebase.FirebaseApplication("https://python-interface-55bc7.firebaseio.com/", None)
    data = {    
    'Name':'Helldcibdibo',
    'Email' :'test@gmail.com',
    'Number': 9599499407
     }
    result = firebase.post("python-interface-55bc7/test", data)
    print(result)


bt=Button(text='submit',command=func)

bt.grid(column=0,row=7)
window.mainloop()
