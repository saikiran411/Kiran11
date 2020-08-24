from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver import ActionChains
#from pynput.mouse import Button,Controller

driver = webdriver.Chrome(executable_path="c:/Users/Dell/Desktop/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_css_selector("#txtUsername").send_keys("Admin")
driver.find_element_by_css_selector("#txtPassword").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

driver.implicitly_wait(10)
print("Login Sucessfull")

# Navigate to Admin
driver.find_element_by_id("menu_admin_viewAdminModule").click()
driver.find_element_by_xpath("//*[@id='btnAdd']").click()
user=driver.find_element_by_id("systemUser_userType")
drp=Select(user)
drp.select_by_visible_text('Admin')
driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Linda Anderson")
#driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Keys.ENTER").Perform()
sleep(2)
#element = driver.find_element_by_id("systemUser_employeeName_empName")
#drp=Select(element)
#drp.select_by_visible_text("Meddi NextGen")
#drp.select_by_index(1)

driver.find_element_by_id("systemUser_userName").send_keys("JohnCena4574134")
driver.find_element_by_xpath("//*[@id='systemUser_password']").send_keys("8019577117@sAi")
driver.find_element_by_xpath("//*[@id='systemUser_confirmPassword']").send_keys("8019577117@sAi")
sleep(3)
driver.find_element_by_id("btnSave").click()
sleep(2)
#PIM
PIM = driver.find_element_by_id("menu_pim_viewPimModule")
Add_Employee = driver.find_element_by_id("menu_pim_viewEmployeeList")
actions = ActionChains(driver)
actions.move_to_element(PIM).move_to_element(Add_Employee).click().perform()
#Adding employee

driver.find_element_by_xpath("//*[@id='menu_pim_addEmployee']").click()
driver.find_element_by_id("firstName").send_keys("Sachin")
driver.find_element_by_id("middleName").send_keys("")
driver.find_element_by_id("lastName").send_keys("Tendulkar")
driver.find_element_by_id("employeeId").send_keys("10")
driver.find_element_by_id("photofile").send_keys("C:/Users/Dell/Desktop/image.jpg")
driver.find_element_by_id("chkLogin").click()
driver.find_element_by_id("user_name").send_keys("Mango2555")
driver.find_element_by_id("user_password").send_keys("8019577117@sAi")
driver.find_element_by_id("re_password").send_keys("8019577117@sAi")
driver.implicitly_wait(10)
element = driver.find_element_by_id("status")
drp=Select(element)
drp.select_by_visible_text("Enabled")
driver.find_element_by_id("btnSave").click()
sleep(5)
#driver.find_element_by_id("btnSave").click()

driver.find_element_by_xpath("//*[@id='btnSave']").click()
# Personal details

driver.find_element_by_id("personal_txtLicenNo").send_keys("BDMD610J")
driver.find_element_by_id("personal_txtOtherID").send_keys("125698")

#Exp Date
driver.find_element_by_id("personal_txtLicExpDate").click()
Year = Select(driver.find_element_by_class_name("ui-datepicker-year"))
Year.select_by_value("2030")

sleep(2)

Month = Select(driver.find_element_by_class_name("ui-datepicker-month"))
Month.select_by_value("1")

sleep(2)

Date = driver.find_element_by_link_text("19")
actions = ActionChains(driver)
actions.move_to_element(Date).click().perform()

#edit
#driver.find_element_by_xpath("//input[contains(@value,'Edit') and @id ='btnSave']").click()

#gender

driver.find_element_by_id("personal_optGender_1").click()

#drop by Marital status

Marital=Select(driver.find_element_by_id("personal_cmbMarital"))
Marital.select_by_visible_text("Single")

#drop by Nationality

Nationality=Select(driver.find_element_by_id("personal_cmbNation"))
Nationality.select_by_visible_text("Indian")

#Date of birth
driver.find_element_by_id("personal_DOB").clear()
driver.find_element_by_id("personal_DOB").send_keys("1999-04-04")
#Year = Select(driver.find_element_by_class_name("ui-datepicker-year"))
#Year.select_by_value("1993")

#Month = Select(driver.find_element_by_class_name("ui-datepicker-month"))
#Month.select_by_value("3")

sleep(2)


#Date1 = driver.find_element_by_link_text("4")
#Actions = ActionChains(driver)
#actions.move_to_element(Date1).click().perform()

#mouse = Controller
#mouse.position(502,838)
#mouse.click(Button.left,1)

driver.find_element_by_xpath("//input[contains(@value,'Save') and @id ='btnSave']").click()