## This comes from a tutorial, link here: https://youtu.be/1pzoiIRdVas
import selenium
from selenium import webdriver


driver = webdriver.Firefox()
## Could use chrome by typing  webdriver.Chrome()

#Using a Best Buy laptop for this
url = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&id=pcat17071&iht=y&keys=keys&ks=960&list=n&sc=Global&st=laptop&type=page&usc=All%20Categories"

driver.get(url)

driver.maximize_window()

click = driver.find_element_by_xpath("/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[4]/div/div[6]/ol/li[3]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div")
## The xpath doesn't seem to work via Chrome

click.click()


