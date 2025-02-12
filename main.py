from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd



your_username = "example@gmail.com"
your_password = "pass@@@@@@@word"
# Set up the WebDriver dynamically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Open the login page
url = "https://aseemamatrimony.in/login.html"  # Replace with the actual login URL
driver.get(url)

time.sleep(10)

username_field = driver.find_element(By.ID, "name")  
username_field.send_keys(your_username)  
time.sleep(5)

password_field = driver.find_element(By.ID, "passwordInput") 
password_field.send_keys(your_password)  
time.sleep(5)




# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit' and @id='login']").click() 
time.sleep(5)

view_all = driver.find_element(By.XPATH, '//*[@id="nav"]/li[4]')
view_all.click()

time.sleep(5)

name_path = '//*[@id="home"]/form[1]/div/div[1]/table/tbody/tr[1]/td[2]'
DoB_path  = '//*[@id="home"]/form[1]/div/div[1]/table/tbody/tr[3]/td[2]'
mobile_no_path = '/html/body/div[1]/section/div/div/div/div/article/div/div/div/div[2]/div/div/div/form[1]/div/div[2]/table/tbody/tr[2]/td[2]'
telephone_no_path = '//*[@id="home"]/form[1]/div/div[2]/table/tbody/tr[3]/td[2]'
alternate_no_path = '//*[@id="home"]/form[1]/div/div[2]/table/tbody/tr[5]/td[2]'
alternate_mob_no_path = '//*[@id="home"]/form[1]/div/div[2]/table/tbody/tr[6]/td[2]'




data_list = []
for j in range(0,152) :

    url = f"https://aseemamatrimony.in/browseprofile/viewall.html?start={20*j}"  # Replace with the actual login URL
    driver.get(url)


    for i in range(1,21) :
        details_path= f'//*[@id="example"]/tbody/tr[{i}]/td/div/div[2]/div/div[2]/div'

        detail=  driver.find_element(By.XPATH, details_path)
        detail.click()

        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

        time.sleep(5)



        name=  driver.find_element(By.XPATH, name_path).text
        DoB=  driver.find_element(By.XPATH, DoB_path).text
        mob_no=  driver.find_element(By.XPATH, mobile_no_path).text
        telephon_no=  driver.find_element(By.XPATH, telephone_no_path).text
        alternate_no=  driver.find_element(By.XPATH, alternate_no_path).text
        alernate_mob_no=  driver.find_element(By.XPATH, alternate_mob_no_path).text
        time.sleep(1)
    
        data_list.append([name, DoB, mob_no, telephon_no, alternate_no, alernate_mob_no])

        print(f"done {i}")
        driver.close()  # Close the current tab
        driver.switch_to.window(window_handles[0])


        df = pd.DataFrame(data_list, columns=["name", "DoB", "mob_no", "telephon_no", "alternate_no", "alernate_mob_no"])
        df.to_excel("extracted_profiles_data.xlsx", index=False)

    page_path = "//a[text()='Next']"
    print(f"page {j} is completed")
    time.sleep(2)
    
    next_page = driver.find_element(By.XPATH, page_path)
    next_page.click()


time.sleep(10)
driver.quit()
