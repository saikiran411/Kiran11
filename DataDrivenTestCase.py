import XLUtils
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="c:/Users/Dell/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

path = "C:/Users/Dell/Desktop/Orange_DDT.xlsx"

rows = XLUtils.getRowCount(path,'Login')

for r in range(2,rows+1):
    UserName = XLUtils.readData(path,"Login",r,1)
    Password = XLUtils.readData(path,"Login",r,2)

    #driver.find_element_by_id("txtUsername").clear()
    driver.find_element_by_id("txtUsername").send_keys(UserName)
    #driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys(Password)

    driver.find_element_by_xpath("//*[@id='btnLogin']").click()


    if driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
        print("test is passed")
        XLUtils.writeData(path,"Login",r,3,"Test Passed")
        driver.find_element_by_xpath("// a[@id='welcome']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[@href='/index.php/auth/logout']").click()
    else:
        print("Test failed")
        XLUtils.writeData(path,"Login",r,3,"Test failed")

driver.close()
#driver.quit()

    #driver.back()



