import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time


# movieslist_url = f"https://in.bookmyshow.com/explore/movies-{city}"

movie_name = "Madame Web"
cinema_name = "amb-cinemas-gachibowli"
cinema_city = "cinema-hyd"
cinema_code = "AMBH-MT"
date = "20240217"
seats = 3
preference_time_start = 1700
preference_time_end = 1800

cinema_url = f"https://in.bookmyshow.com/buytickets/{cinema_name}/{cinema_city}-{cinema_code}/{date}"

driver = uc.Chrome()

driver.get(cinema_url)
time.sleep(7)
driver.find_element(By.XPATH, "//button[@id='wzrk-cancel']").click()

shows = driver.find_elements(By.XPATH, "//li[contains(., 'Madame')]//descendant::a[@class='showtime-pill data-enabled']//div[@class='__text']")

for show in shows: 
    show_time_text = show.text
    show_time = int(show_time_text[0:2]) * 100 + int(show_time_text[3:5])
    if (show_time_text[6:] == "PM"):
        show_time += 1200
    if show_time >= preference_time_start and show_time <= preference_time_end:
        show.click()


# clicks accept on popup
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='btnPopupAccept']").click()


time.sleep(5)
driver.find_element(By.XPATH, f"//li[contains(@id,'pop_{seats}')]").click()
driver.find_element(By.XPATH, "//div[@id='proceed-Qty']").click()

time.sleep(1)

available_seats = driver.find_elements(By.XPATH, "//div[a[contains(@class , '_available')]]")
available_seats[0].click()

# for seat in available_seats:
#     print(seat.get_attribute('id'))
#     seat.click()
#     seats -= 1
#     if not seats:
#         break

driver.execute_script('return fnBookNow();')
time.sleep(10)
driver.execute_script('fnPrePay();')
time.sleep(10)

payment_url = driver.current_url
print("payment_url-----------------------------")
print(payment_url)


time.sleep(10000)
driver.close()
