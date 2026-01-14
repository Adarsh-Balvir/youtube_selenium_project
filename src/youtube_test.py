from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.youtube.com")
time.sleep(3)

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Selenium tutorial")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.save_screenshot("screenshots/yotube-search.png")
print("Screenshot saved: screenshots/youtube_search.png")

first_video = driver.find_element(By.ID, "video-title")
first_video.click()
time.sleep(5)

driver.save_screenshot("screenshots/first-video_opened.png")
print("Screenshot saved: screenshots/first_video_opened.png")
driver.quit()
