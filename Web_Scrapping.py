from selenium import webdriver      #Importing Libraries
from bs4 import BeautifulSoup

driver = webdriver.Firefox()        #Defining Webdriver

for i in range(3):                  #Page scrolling loop
    link=("https://www.trendyol.com/sr?q=paten&qt=paten&st=paten&os=1&pi=" + str(i+1))      #Doing string addition to turn pages
    driver.get(link)                          #Definding URL

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")                      #Definding site parser
    products = soup.find_all('div', class_="p-card-wrppr add-to-bs-card")             #In this row we search a class which include all products classes
    for products in products:                                                #Then doing loop for every product class
        name = products.find("span", class_="prdct-desc-cntnr-name hasRatings" )  #Searching for a name string in product class
        list = str(name).split('"')                                              #Then by converting name to string, we split it and assign to list
        if "None" not in list :                                                  #We do not print,if list include "None"
            print(list[3])
