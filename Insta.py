from selenium import webdriver
import time
from bs4 import BeautifulSoup
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# import KEYS
from selenium.webdriver.common.keys import Keys



files = open('Pass.txt')
lines = files.readlines()
username = lines[4]
password = lines[5]

getdriver = ("https://www.instagram.com/accounts/login/")
insta = ("https://www.instagram.com")

driver = webdriver.Chrome("chromedriver.exe")
driver.get(getdriver)
driver.maximize_window()

time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
#driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]").click()


time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys('likeforlike')

time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
time.sleep(3)

actions = ActionChains(driver)
for _ in range(1,4):
    actions.send_keys(Keys.SPACE).perform()
    time.sleep(1)

time.sleep(4)

url = []
elems = driver.find_elements_by_tag_name('a')
for elem in elems:
    href = elem.get_attribute('href')
    if href is not None:
        url.append(href)
sub = "/p/"
url_post = [url for url in url if sub in url]
print(len(url_post))

for post in url_post:
    driver.get(post)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()


'''
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]").click()
time.sleep(5)
action = ActionChains(driver)
t = 10
while(t>0):
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
    time.sleep(2)
    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
    time.sleep(5)
    t = t-1
'''





