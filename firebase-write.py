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
url = "https://web.whatsapp.com/send?phone=+91"+akshat


driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),  options =  chrome_options)  
driver.maximize_window()
driver.get(url)
username_textbox = d river.find_element_by_id("_3FRCZ copyable-text selectable-text")






