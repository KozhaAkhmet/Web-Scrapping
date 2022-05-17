
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

for i in range(3):
    link=("https://www.trendyol.com/sr?q=paten&qt=paten&st=paten&os=1&pi=" + str(i+1))
    driver.get(link)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find_all('div', class_="p-card-wrppr add-to-bs-card")
    for products in products:
        name = products.find("span", class_="prdct-desc-cntnr-name hasRatings" )
        strin = str(name).split('"')
        if "None" not in strin :
            print(strin[3])
