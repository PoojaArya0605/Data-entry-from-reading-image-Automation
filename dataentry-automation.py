from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytesseract       
from PIL import Image     
import pyttsx3            
from googletrans import Translator
import urllib
import requests
import io
import time


START =int(input("Enter start number: "))
END = int(input("Enter end number: "))

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}

web=webdriver.Chrome()
web.get('Site link')
username=web.find_element_by_id('useremail')
username.send_keys('ID name')
password=web.find_element_by_id('userpassword')
password.send_keys('Password')
python_button = web.find_elements_by_xpath("//*[@id='userLoginform']/div[3]/button")[0]
python_button.click()
start_button = web.find_elements_by_xpath("//*[@id='side-menu']/li[1]/a")[0]
start_button.click()

    
val=[]
for i in range(START, END + 1):
    select_image_button = web.find_element_by_id('dataId')
    select_option = Select(select_image_button)
    select_option.select_by_visible_text(f'Record-{i}')
    WebDriverWait(web, 60).until(EC.invisibility_of_element_located(web.find_element_by_id("loading")))
    imgsrc= web.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div/div[2]/span/img")
    img=imgsrc.get_attribute('src')
    #print(img)
    response = requests.get(img, headers = header)
    #print(response.content)
    img = Image.open(io.BytesIO(response.content))      
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
# converts the image to result and saves it into result variable 
    result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path    
    with open('abc.txt',mode ='w') as file:      
        file.write(result)
    print(len(result))
    val=result.split('*')
    print(val)
    
    try:
        username=web.find_element_by_id('tbc_no')
        username.send_keys(val[0])
        username=web.find_element_by_id('user_name')
        username.send_keys(val[1])
        username=web.find_element_by_id('contact_no')
        username.send_keys(val[2])
        username=web.find_element_by_id('license_no')
        username.send_keys(val[3])
        username=web.find_element_by_id('address')
        username.send_keys(val[4])
        username=web.find_element_by_id('gir_no')
        username.send_keys(val[5])
        username=web.find_element_by_id('mrn_no')
        username.send_keys(val[6])
        username=web.find_element_by_id('loan_amount')
        username.send_keys(val[7])
    except IndexError:
        username=web.find_element_by_id('tbc_no')
        username.send_keys('000')
        username=web.find_element_by_id('user_name')
        username.send_keys('000')
        username=web.find_element_by_id('contact_no')
        username.send_keys('000')
        username=web.find_element_by_id('license_no')
        username.send_keys('000')
        username=web.find_element_by_id('address')
        username.send_keys('000')
        username=web.find_element_by_id('gir_no')
        username.send_keys('000')
        username=web.find_element_by_id('mrn_no')
        username.send_keys('000')
        username=web.find_element_by_id('loan_amount')
        username.send_keys('000')
    except:
        print("list index out of range")
    save= web.find_elements_by_xpath("//*[@id='userForm']/div[2]/button[1]")[0]
    save.click()
    time.sleep(2)

    
    
