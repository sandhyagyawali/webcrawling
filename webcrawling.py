from selenium import webdriver

#Open up a browser and navigate to webpage
driver = webdriver.Chrome(r'C:\Users\Dell\Desktop\chromedriver_win32\chromedriver.exe')
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#Extract lists of "buyers" and "prices" based on xpath
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# Print out all the buyers and prices on current pages:
num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text + ":" + prices[i].text)

#Clean up [close browser once task is completed.]
driver.close()
