from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time

import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


print("Launching browser")

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)


os.system('cls')
print("Openning facebook")

driver.get("https://www.facebook.com/pokes")

os.system('cls')
driver.find_element_by_xpath('//*[@title="Accept All"]').click()

def logIn():
	lField = driver.find_element_by_name("email")
	pField = driver.find_element_by_name("pass")
	lButton = driver.find_element_by_id('loginbutton')

	email = input("Enter Email address or phone number\n--> ")
	os.system('cls')
	password = input("Enter Password\n--> ")
	os.system('cls')
	
	lField.clear()
	lField.send_keys(email)

	pField.clear()
	pField.send_keys(password)

	lButton.click()

	time.sleep(1)

logIn()

while driver.current_url != "https://www.facebook.com/pokes":
	print("Incorrect Login")
	logIn()

print("Logged in")

peopleCN = "ow4ym5g4 auili1gw rq0escxv j83agx80 buofh1pr g5gj957u i1fnvgqd oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 nnctdnn4 hpfvmrgz qt6c0cv9 jb3vyjys l9j0dhe7 du4w35lb bp9cbjyn btwxx1t3 dflh9lhu scb9dxdr"
namesCN = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"
rPeopleXP = '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div[2]'
rBannerXP = '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]'

rWait = WebDriverWait(driver, 30, poll_frequency=3)
rBanner = rWait.until(ec.visibility_of_element_located((By.XPATH, rBannerXP)))
rPeople = rWait.until(ec.visibility_of_element_located((By.XPATH, rPeopleXP)))

for element in [rPeople, rBanner]:
	driver.execute_script("""
	var element = arguments[0];
	element.parentNode.removeChild(element);
	""", element)


os.system('cls')
print("Waiting for incoming poke...")

pWait = WebDriverWait(driver, 10**10, poll_frequency=5)
pWait.until(ec.visibility_of_element_located((By.XPATH, '//div[@aria-label="Poke Back"]')))

os.system('cls')


while True:

	pWait.until(ec.visibility_of_element_located((By.XPATH, '//div[@aria-label="Poke Back"]')))

	people = driver.find_elements_by_xpath(f'//div[@class="{peopleCN}"]')
	for p in people:
		try:
			name = p.find_element_by_xpath(f'.//a[@class="{namesCN}"]').get_attribute("textContent")
			p.find_element_by_xpath('.//div[@aria-label="Poke Back"]').click()
			print(f"Poked {name}")
		except:
			continue
