from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.chrome.options import Options 
import os
import socket

number = int(input("Enter your phone number: "))

branch = input("Which branch? (G43, G46, Saket) : ")

username = input("Enter your admission number: ")
password = getpass("Enter password: ")

if(branch == "G43"):
    url = "https://aisg43.amizone.net"

elif (branch == "G46"):
    url = "https://aisg46.amizone.net"

elif (branch == "Saket"):
    url = "https://aissnew.amizone.net"

else:
    print("This branch is not supported yet :(")



chrome_options = Options()  
#chrome_options.add_argument("--headless")  



driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),  options =  chrome_options)  
driver.maximize_window()
driver.get(url)


username_textbox = driver.find_element_by_id("LoginName")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("LoginPassword")
password_textbox.send_keys(password)

driver.find_element_by_xpath( ".//*[contains(text(), 'Keep me logged in')]").click()

driver.find_element_by_xpath( ".//*[contains(text(), 'Sign In')]").click()

time.sleep(5)
driver.find_element_by_xpath( ".//*[contains(text(), 'Home Work')]").click()

time.sleep(5)
str1 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[5]/div[1]/div/div").text
str3 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[5]/div[3]/div/div").text
str5 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[5]/div[5]/div/div").text
str7 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[5]/div[7]/div/div").text
str9 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[5]/div[9]/div/div").text
str11 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div[5]/div[11]/div/div").text

print(str1)
print(str3)
print(str5)
print(str7)
print(str9)
print(str11)


#acting as host

#   s = socket.socket()
# print("Socket created")

# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)

# s.bind((ip_address, 9999))

# s.listen(3)
# print("Listening.....")

# while True:
#     c, addr = s.accept()
#     print("Connected to : " , addr)
    
#     c.send(bytes("Yay, you connected", "utf-8"))
    
#     c.close


