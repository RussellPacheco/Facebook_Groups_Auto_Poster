from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import window

runapp = window.MainWindow()
runapp.mainloop()

driver = webdriver.Chrome(f"{runapp.filename2}")
driver.get(f"https://calendar.google.com/calendar/r/search?q=NCAD&start={runapp.from_date_entry}&end={runapp.to_date_entry}")

element1 = driver.find_element_by_name("identifier")
element1.send_keys(f"{runapp.email_entry}")
element1.send_keys(Keys.RETURN)

driver.implicitly_wait(8)

element2 = driver.find_element_by_name("password")
element2.send_keys(f"{runapp.password_entry}")
element2.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "yHbHub")))
    soup = bs(driver.page_source, "html.parser")
    events = soup.find_all("div", attrs={"class": "i06k6b NlL62b"})
    ncaddata = []

    for event in events:
        ncaddata.append(event.text)
finally:
    driver.quit()

ncaddatadf = pd.DataFrame(data=ncaddata)

append_df_to_excel(f"{runapp.filename1}", ncaddatadf, sheet_name="Pickup_Data", header=None, index=False, startrow=2)
