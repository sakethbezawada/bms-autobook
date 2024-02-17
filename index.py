from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time


# movieslist_url = f"https://in.bookmyshow.com/explore/movies-{city}"

cinema_name = "amb-cinemas-gachibowli"
cinema_city = "cinema-hyd"
cinema_code = "AMBH-MT"
date = "20240217"
seats = 3

cinema_url = f"https://in.bookmyshow.com/buytickets/{cinema_name}/{cinema_city}-{cinema_code}/{date}"

driver = webdriver.Chrome()

driver.get(cinema_url)
name_elements = driver.find_elements(By.XPATH, "//span[@class='__name']")
movie_item  = [x for x in name_elements if re.search("^Madame", x.text)][0]

# selects first available show
movie_item.find_element(By.XPATH, "//ancestor::li").find_element(
    By.XPATH, "//a[@class='showtime-pill data-enabled']").click()

# clicks accept on popup
driver.find_element(By.XPATH, "//div[@id='btnPopupAccept']").click()



time.sleep(10000)


# abc = driver.find_elements(By.XPATH, "//li[contains(@id,'pop_1')]")
# print(abc)

# defs = driver.find_element(By.XPATH, "//ul[@id='popQty']")

# driver.find_element(By.XPATH, f"//li[@id='pop_{seats}']").click()
# driver.find_element(By.XPATH, "//div[@id=proceed-Qty]").click()


driver.close()

# https://in.bookmyshow.com/serv/getData?cmd=GETSHOWINFOJSON&vid=AMBH&ssid=66756&format=json
# https://in.bookmyshow.com/serv/getData?cmd=GETSHOWINFOJSON&vid=AMBH&ssid=66756&format=json


# curl "https://in.bookmyshow.com/serv/getData?cmd=GETSHOWINFOJSON&vid=AMBH&ssid=66756&format=json" ^
#   -H "authority: in.bookmyshow.com" ^
#   -H "accept: */*" ^
#   -H "accept-language: en-US,en;q=0.9" ^
#   -H "cache-control: no-store" ^
#   -H "content-type: application/x-www-form-urlencoded" ^
#   -H "cookie: bmsId=1.0607296298.1708149533031; Rgn=^%^7CCode^%^3DHYD^%^7Ctext^%^3DHyderabad^%^7Cslug^%^3Dhyderabad^%^7C; __cf_bm=bA9VabAq_utOr8BdArGBVkZyM_bvcWnZqkOvHtY7n7E-1708149533-1.0-Ae7Lu/7+hiBwG916H2n8kr7fT3Do+H7jzafEoo32vRjn8/9CRefLlH4jUGy6khl/EfT1tEUwlKN8kT/+B59Mwiw=; _cfuvid=ZtezvSr4Sdi5JG3Ie30IXj3LmwxJ1sx8Lyy93QcJV6E-1708149533343-0.0-604800000; _gcl_au=1.1.1752243469.1708149533; __gads=ID=619b7f8a6adc35ce:T=1708149534:RT=1708149534:S=ALNI_MbEwYR_pF1u1ouZGFm59tzvRAYeQg; __gpi=UID=00000dcaa9cac295:T=1708149534:RT=1708149534:S=ALNI_MYd85rcbG6mGsBPN7Kyn3xswOr7VA; __eoi=ID=59d40e2dc8a5ef85:T=1708149534:RT=1708149534:S=AA-AfjZ7BKAGoLC6BsUxct2fegzx; APPDETAILS_ALL=^%^7B^%^22FB^%^22^%^3A^%^22^%^7CFB_APPID^%^3D165665113451029^%^7CFB_PRIVILEGES^%^3Demail^%^2Cpublic_profile^%^2Cuser_birthday^%^2Cuser_gender^%^7CAPPID_LIST^%^3D165665113451029^%^7CCHECKLIST^%^3DY^%^7CFB_URL^%^3Dhttps^%^3A^%^2F^%^2Fgraph.facebook.com^%^2Fv3.2^%^7C^%^22^%^2C^%^22PLUS^%^22^%^3A^%^22^%^7CGOOGLELOGIN_ACTION^%^3Dhttp^%^3A^%^2F^%^2Fschemas.google.com^%^2FAddActivity^%^7CGOOGLELOGIN_CLIENTID^%^3D990572338172-iibth2em4l86htv30eg1v44jia37fuo5.apps.googleusercontent.com^%^7CGOOGLELOGIN_PRIVILEGES^%^3Dprofile^%^26nbsp^%^3B^%^20openid^%^26nbsp^%^3Bemail^%^7C^%^22^%^7D; cf_clearance=nzBEgMrfPPttyu.UE0N3hX3HXoWuDUEd8iPrsOKIbQ0-1708149535-1.0-AQvwZm0ScRBkTDxxIp4jHIk2nI50p9qFtFi9n8fYhYw0ikMF34/+uucq8I0oIhjVFyrwOEAnvuWX/fToX/fnxzA=; _ga=GA1.1.2091971314.1708149533; WZRK_G=ecaaa66707964cb7afe312e84c934487; _uetsid=a1685960cd5911ee9a5781c9cc5dec07; _uetvid=a1686900cd5911ee87f92d853a888536; _fbp=fb.1.1708149533894.509820243; WZRK_S_RK4-47R-98KZ=^%^7B^%^22p^%^22^%^3A1^%^2C^%^22s^%^22^%^3A1708149535^%^2C^%^22t^%^22^%^3A1708149534^%^7D; cto_bundle=ANCZd183dmlJMHhsREZ5byUyQlJ6cE9oRVRia2JYYXlvcXA1NmpPVSUyQnJjeDJSRVBSVnZWTUwzYmVzYkZCTGxuTGo2VldTVE8xSjRBYTA5VlJmZ3BPSmJZTTA5R2lSY1lJJTJGOGdnTnBMTG9kUmRQUzBQa1ZxTyUyRkVSNnAxYklCQVN0blBQSGNoZHBtU2c3WE5VbDNtQ3pFRHdUZmFXZyUzRCUzRA; tvc_vid=91708149534387; AMP_TOKEN=^%^24NOT_FOUND; tvc_bmscookie=GA1.2.2091971314.1708149533; tvc_bmscookie_gid=GA1.2.3934109.1708149535; _dc_gtm_UA-27207583-8=1; _ga_84T5GTD0PC=GS1.1.1708149533.1.0.1708149534.59.0.0; userCine=^%^7Cmrs^%^3DAMBH^%^3B^%^7C" ^
#   -H "referer: https://in.bookmyshow.com/buytickets/amb-cinemas-gachibowli/cinema-hyd-AMBH-MT/20240217" ^
#   -H "sec-ch-ua: ^\^"Not A(Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"121^\^", ^\^"Chromium^\^";v=^\^"121^\^"" ^
#   -H "sec-ch-ua-mobile: ?0" ^
#   -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
#   -H "sec-fetch-dest: empty" ^
#   -H "sec-fetch-mode: cors" ^
#   -H "sec-fetch-site: same-origin" ^
#   -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36" ^
#   -H "x-requested-with: XMLHttpRequest" ^
#   --compressed

# curl "https://in.bookmyshow.com/serv/getData?cmd=GETSHOWINFOJSON&vid=AMBH&ssid=66756&format=json" ^
#   -H "authority: in.bookmyshow.com" ^
#   -H "accept: */*" ^
#   -H "accept-language: en-US,en;q=0.9" ^
#   -H "cache-control: no-store" ^
#   -H "content-type: application/x-www-form-urlencoded" ^
#   -H "cookie: bmsId=1.430989244.1705639580871; preferences=^%^7B^%^22ticketType^%^22^%^3A^%^22M-TICKET^%^22^%^7D; _gcl_au=1.1.725939402.1705639581; _ga=GA1.1.287491890.1705639581; tvc_bmscookie=GA1.2.287491890.1705639581; WZRK_G=a244b76e02e64fb685dc437b78a9aa4f; geoHash=^%^22^%^22; geolocation=^%^7B^%^22x-location-shared^%^22^%^3Afalse^%^2C^%^22x-location-selection^%^22^%^3A^%^22manual^%^22^%^2C^%^22timestamp^%^22^%^3A1705639584763^%^7D; tvc_vid=81705639607475; Rgn=^%^7CCode^%^3DHYD^%^7Cslug^%^3Dhyderabad^%^7Ctext^%^3DHyderabad^%^7C; _cfuvid=gRl_Jd7wNcn6jHHGKBlkJUiosVf54jOAIwIBdaf_xJE-1708090977769-0.0-604800000; tvc_bmscookie_gid=GA1.2.1442607397.1708090979; userCine=^%^7Cmrs^%^3DAMBH^%^3B^%^7C; cf_clearance=ULPQjPl0.wXTvYx7Bm2FQqBmN8inbji2CsXczBxYxPQ-1708145674-1.0-ASjzyRooNP7rkk8XawFdmWBwCeq7xDHQMvexWn7dLp1VoJaQAWxicP9Kt/T321TG5PUWSIHYR7e6YyqfN/ZFQo8=; __cf_bm=7fwi6AMk3V5ctAOf2vvo9ThRfJx18ENbNv4KgSCIuWg-1708148980-1.0-ASaIiYYB74dMVkMU/zyyM5IoNeIS7SO7CrauN2NbnTaKEB08kvbb5YbiQ8zRwyII8PUeXZFJJ9AWD4m8uaOriI0=; APPDETAILS_ALL=^%^7B^%^22FB^%^22^%^3A^%^22^%^7CFB_APPID^%^3D165665113451029^%^7CFB_PRIVILEGES^%^3Demail^%^2Cpublic_profile^%^2Cuser_birthday^%^2Cuser_gender^%^7CAPPID_LIST^%^3D165665113451029^%^7CCHECKLIST^%^3DY^%^7CFB_URL^%^3Dhttps^%^3A^%^2F^%^2Fgraph.facebook.com^%^2Fv3.2^%^7C^%^22^%^2C^%^22PLUS^%^22^%^3A^%^22^%^7CGOOGLELOGIN_ACTION^%^3Dhttp^%^3A^%^2F^%^2Fschemas.google.com^%^2FAddActivity^%^7CGOOGLELOGIN_CLIENTID^%^3D990572338172-iibth2em4l86htv30eg1v44jia37fuo5.apps.googleusercontent.com^%^7CGOOGLELOGIN_PRIVILEGES^%^3Dprofile^%^26nbsp^%^3B^%^20openid^%^26nbsp^%^3Bemail^%^7C^%^22^%^7D; AMP_TOKEN=^%^24NOT_FOUND; _uetsid=4b1e4fa0ccd111eea2a845b08bdbadb2; _uetvid=bfdc5f80b68511ee93d929967fed0191; cto_bundle=ix1ik19MYWJPZk0xZTd6NTN0a0V3REF0Y3VYOEx5NGNxeUpvTmYlMkZuMGNrMUF0V2hzYXE0YVAwVjRuWUpBMWVyV3hJam51YzJJalElMkJmYnZTSjFUdFM3ZVhZMkQ1UzdwWjFLTW1pVWt2T1E3MGZpNjdBU2FJYjFQSlIzdVNMVFpDb3M3YVpHbGx3MHpZOVdWRUtlZTMwV2hzcyUyQkc1Wk1JVVBvWGNTeEp5S2dHJTJCNlV2cTBpWWxaM1ZwTlQ4JTJGJTJCeUlTR293VG9pOGRCY0UyTFA1YUxESDcxaHdHZ3EwbE1VYTNpS1F6ZzJSQ1pwaHN1bGYyM2ZSV25ZS205V0JtaTk5ZWk2R3ViMllQMVQlMkJRN3hGVlBGYlFWeGVPeVZwRjU4UHkwMSUyRmgybnlYdSUyQk0lMkJOYzRwNmREbUxLYjgwOHhqVms5Z2IlMkZpSUo; _ga_84T5GTD0PC=GS1.1.1708145671.5.1.1708149382.60.0.0; WZRK_S_RK4-47R-98KZ=^%^7B^%^22p^%^22^%^3A14^%^2C^%^22s^%^22^%^3A1708145674^%^2C^%^22t^%^22^%^3A1708149383^%^7D" ^
#   -H "referer: https://in.bookmyshow.com/buytickets/amb-cinemas-gachibowli/cinema-hyd-AMBH-MT/20240217" ^
#   -H "sec-ch-ua: ^\^"Not A(Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"121^\^", ^\^"Chromium^\^";v=^\^"121^\^"" ^
#   -H "sec-ch-ua-mobile: ?0" ^
#   -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
#   -H "sec-fetch-dest: empty" ^
#   -H "sec-fetch-mode: cors" ^
#   -H "sec-fetch-site: same-origin" ^
#   -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36" ^
#   -H "x-requested-with: XMLHttpRequest" ^
#   --compressed

