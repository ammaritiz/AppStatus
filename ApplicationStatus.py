from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import winsound

#ASU
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login%3Fcallapp%3Dhttps%253A%252F%252Fwebapp4.asu.edu%252Fmyasu%252F%253Finit%253Dfalse")

inputElement = driver.find_element_by_name("username")
inputElement.send_keys("") #Yourusername
inputElement = driver.find_element_by_name("password")
inputElement.send_keys("") #Yourpassword
driver.find_element_by_class_name("submit").send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "tooltip-heading-app-status")))
print "ASU : "
try:
    driver.find_element_by_partial_link_text("In Review")
    print "Still In Review"
    driver.get("https://webapp4.asu.edu/myasu/Signout")
    driver.quit()
except:
    print "ASU status changed"
#ASU

#PSU
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://webaccess.psu.edu/?cosign-secure.gradsch.psu.edu&https://secure.gradsch.psu.edu/app/gradapp/")
inputElement = driver.find_element_by_name("login")
inputElement.send_keys("") #Yourusername
inputElement = driver.find_element_by_name("password")
inputElement.send_keys("") #Yourpassword
inputElement.send_keys(Keys.RETURN)
driver.get("https://secure.gradsch.psu.edu/app/status/ResponseGrad.cfm?appid=3904")
print("PSU : ")
try:
    driver.find_element_by_name("withdraw")
    print "Initial Phase"
    driver.get("https://secure.gradsch.psu.edu/app/status/index.cfm")
    driver.get("https://secure.gradsch.psu.edu/app/gradapp/includes/logout.cfm")
    driver.find_element_by_name("verify").click()
    driver.quit()
except:
    print "PSU status changed" 
#PSU

#UCLA
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://appstatus.grad.ucla.edu/account/login.aspx")
inputElement = driver.find_element_by_id("MainContent_LoginUser_UserName")
inputElement.send_keys("") #Yourusername
inputElement = driver.find_element_by_id("MainContent_LoginUser_Password")
inputElement.send_keys("") #Yourpassword
select = Select(driver.find_element_by_id("MainContent_LoginUser_ddlProgram"))
select.select_by_visible_text("UCLA")
driver.find_element_by_id("MainContent_LoginUser_LoginButton").click()
print "UCLA : "
flag = False
for element in driver.find_elements_by_tag_name("p"):
    if "no decision" in element.text:
        flag = True
        print "No Decision Yet"
        driver.quit()
        break
if flag == False:
    print "UCLA status changed"  
#UCLA

#NCSU
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantLogin.asp?id=ncsu-grad")
inputElement = driver.find_element_by_id("ay-login")
inputElement.send_keys("") #Yourusername
inputElement = driver.find_element_by_id("ay-password")
inputElement.send_keys("") #Yourpassword
driver.find_element_by_id("ay-loginSubmit").send_keys(Keys.RETURN)
print "NCSU : "
try:
    driver.find_element_by_partial_link_text("decision")
    print "Decision made"
except:
    driver.execute_script('logout()')
    print("No Decision Yet")
    driver.quit()
#NCSU

#SB
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantLogin.asp?id=sunysb-gs")
inputElement = driver.find_element_by_id("ay-login")
inputElement.send_keys("") #Yourusername
inputElement = driver.find_element_by_id("ay-password")
inputElement.send_keys("") #Yourpassword
driver.find_element_by_id("ay-loginSubmit").send_keys(Keys.RETURN)
print "SB : "
try:
    driver.find_element_by_partial_link_text("decision")
    print "Decision made"
except:
    driver.execute_script('logout()')
    print("No Decision Yet")
    driver.quit()
#SB

#UMN
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.applyyourself.com/AYApplicantLogin/fl_ApplicantConnectLogin.asp?id=UMN-GRAD")
inputElement = driver.find_element_by_id("ay-login")
inputElement.send_keys("") #Yourusername
inputElement = driver.find_element_by_id("ay-password")
inputElement.send_keys("") #Yourpassword
driver.find_element_by_id("ay-loginSubmit").send_keys(Keys.RETURN)
print "UMN : "
flag = False
for element in driver.find_elements_by_tag_name("h4"):
    if "AWAITING PROGRAM DECISION" in element.text:
        flag = True
        print "No Decision Yet"
        driver.execute_script('logout()')
        driver.quit()
        break
if flag == False:
    print "UMN status changed"
#UMN 

#RUTGERS
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admissionservices.rutgers.edu/graduate/programStatusLogon.app")
inputElement = driver.find_element_by_class_name("inputTxt")
inputElement.send_keys("") #RUID
select = Select(driver.find_element_by_id("dobMonth"))
select.select_by_visible_text("") #DOBMonth
select = Select(driver.find_element_by_id("dobDay"))
select.select_by_visible_text("") #DOBday
select = Select(driver.find_element_by_id("dobYear"))
select.select_by_visible_text("") #DOByear
driver.find_element_by_id("genderCode").click() #If you are a female, change id to gencode1
driver.find_element_by_id("submitBtn").send_keys(Keys.RETURN)
print("RUTGERS : ")
try:
    driver.find_element_by_partial_link_text("No decision")
    print "No Decision" 
    driver.find_element_by_id("logoutDiv")
    driver.quit()
except:
    print("RUTGERS status changed")
#RUTGERS

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
