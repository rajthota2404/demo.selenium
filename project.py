from selenium import webdriver
import time
browser = webdriver.Chrome('E:\python\chromedriver.exe')
browser.get('https://www.youtube.com/')
print(browser.title)
try:
    assert "youtube"==browser.title
except AssertionError:
    print(f"Page title not matched with expected title,Actual title{browser.title}but expected title is {'youtube'}")

browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.close()
