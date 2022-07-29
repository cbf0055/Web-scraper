#Chandler Franklin
#3/5/21
#Web Scraper: Go to cnn.com and get 3 headers from each category: business, entertainment, and style
import requests
from bs4 import BeautifulSoup


url_b = 'https://www.cnn.com/business/'             #This section makes a request to visit the business tab in cnn.com
r_business = requests.get(url_b)                    #Then searches for h3, which on the business tab is the article titles
soup_b = BeautifulSoup(r_business.content, 'lxml')  #and saves the article titles into business_headers
business_headers = soup_b.select('h3')              

url_e = 'https://www.cnn.com/entertainment/'            #This section makes a request to visit the entertainment tab in cnn.com
r_entertainment = requests.get(url_e)                   #Then searches for h3, which is article titles in the entertainment tab
soup_e = BeautifulSoup(r_entertainment.content, 'lxml') #and saves the article titles into entertainment headers
entertainment_headers = soup_e.select('h3')             

url_s = 'https://www.cnn.com/style/'                    #This section makes a request to visit the style tab in cnn.com
r_style = requests.get(url_s)                           #Then searches for h1, which is article titles in the style tab
soup_s = BeautifulSoup(r_style.content, 'lxml')         #and saves the article titles into style_headers
style_headers = soup_s.select('h1')


print("\n")                                             #This section displays 3 article titles from the business tab to the user
print("Business headers: ")
for item in business_headers[:3]:
    print(item.getText())
    print("\n")

print("entertainment headers: ")                        #This section displays 3 entertainment article titles to the user
for item in entertainment_headers[:3]:
    print(item.getText())
    print("\n")

print("style headers: ")                              #This secion displays 3 style article titles to the screen.  
for item in style_headers[1:4]:                       #from 1-4 because there is a repeat in the first 2 indices
    print(item.getText())
    print("\n")


