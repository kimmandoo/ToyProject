# Coded by Mingyu Kim
# referred https://signing.tistory.com/44
# crawling stars, reviews at playstore reviews

from selenium import webdriver
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException

url = "https://play.google.com/store/apps/details?id=com.truefriend.ministock&showAllReviews=true"
driverPath = "chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get(url)

spread_review = driver.find_elements_by_xpath("//button[@jsaction='click:TiglPc']")
for i in range(len(spread_review)):
    isTrue = spread_review[i].is_displayed()
    if isTrue:
        spread_review[i].click()
        time.sleep(2)

SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    for i in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height
    try:
        driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
    except NoSuchElementException:
        short_reviews = driver.find_elements_by_xpath("//span[@jsname='bN97Pc']")
        long_reviews = driver.find_elements_by_xpath("//span[@jsname='fbQN7e']")
        stars = driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']")
        break

res_dict = []
merged_review = [t.text if t.text != '' else long_reviews[i].text for i, t in enumerate(short_reviews)]

for i in range(len(short_reviews)):
    star_string = stars[i].get_attribute('aria-label')

    res_dict.append({
        'STAR': star_string[10],
        'REVIEW': merged_review[i]
    })

res_df = pd.DataFrame(res_dict)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(res_df)

res_df.to_csv("review.csv")