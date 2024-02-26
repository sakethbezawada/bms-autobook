import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time


# movieslist_url = f"https://in.bookmyshow.com/explore/movies-{city}"

city = "hyderabad"
movie_name = "Madame Web"
cinema_city = "cinema-hyd"
cinema_name = "amb-cinemas-gachibowli"
cinema_code = "AMBH-MT"


date = "20240217"
seats = 3
preference_time_start = 1400
preference_time_end = 2300

cinema_url = f"https://in.bookmyshow.com/buytickets/{cinema_name}/{cinema_city}-{cinema_code}/{date}"
movieslist_url = f"https://in.bookmyshow.com/explore/movies-{city}"
cinemalist_url = "https://in.bookmyshow.com/explore/cinemas"

driver = uc.Chrome()

# driver.get(cinemalist_url)
# driver.find_element(By.XPATH, "//span[contains(@cursor,'pointer')]").click()
# city_list_elements = driver.find_elements(By.XPATH, "//li//child::div[not(*)]")
# for city in city_list_elements:
# print(city_list)
# time.sleep(30)

### GET CITY LIST
driver.get(cinemalist_url)
driver.find_element(By.XPATH, "//span[contains(@cursor,'pointer')]").click()
city_list_elements = driver.find_elements(By.XPATH, "//li//child::div[not(*)]")
city_list_elements_major = driver.find_elements(By.XPATH, "//li//child::div//child::span")
city_list = [city.get_attribute("innerHTML") for city in city_list_elements] + \
        [city.get_attribute("innerHTML") for city in city_list_elements_major]
print(len(city_list))
time.sleep(30)


### GET MOVIE LIST
# driver.get(movieslist_url)
# # driver.execute_script("window.scrollTo(0, 1000);")
# driver.execute_script("window.scrollTo(0, 2000);")
# # driver.execute_script("window.scrollTo(0, 3000);")
# time.sleep(4)
# movie_list_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-7o7nez-0')]//ancestor::a//descendant::h3")
# movie_list = [movie.get_attribute("innerHTML") for movie in movie_list_elements]
# print(movie_list)


#### RESERVE TICKETS
# driver.get(cinema_url)
# time.sleep(8)
# driver.find_element(By.XPATH, "//button[@id='wzrk-cancel']").click()

# shows = driver.find_elements(By.XPATH, f"//li[contains(., '{movie_name}')]//descendant::a[@class='showtime-pill data-enabled']//div[@class='__text']")

# for show in shows: 
#     show_time_text = show.text
#     show_time = int(show_time_text[0:2]) * 100 + int(show_time_text[3:5])
#     if (show_time_text[6:] == "PM"):
#         show_time += 1200
#     if show_time >= preference_time_start and show_time <= preference_time_end:
#         show.click()


# # clicks accept on popup
# time.sleep(3)
# driver.find_element(By.XPATH, "//div[@id='btnPopupAccept']").click()


# time.sleep(6)
# driver.find_element(By.XPATH, f"//li[contains(@id,'pop_{seats}')]").click()
# driver.find_element(By.XPATH, "//div[@id='proceed-Qty']").click()

# time.sleep(1)

# available_seats = driver.find_elements(By.XPATH, "//div[a[contains(@class , '_available')]]")
# available_seats[6].click()

# for seat in available_seats:
#     print(seat.get_attribute('id'))
#     # seat.click()
#     # seats -= 1
#     # if not seats:
#     #     break
# time.sleep(1000)
# driver.execute_script('fnBookTickets();')
# time.sleep(4)
# driver.execute_script('fnPrePay();')
# time.sleep(2)

# payment_url = driver.current_url
# print("payment_url-----------------------------")
# print(payment_url)

# time.sleep(10000)
driver.close()
