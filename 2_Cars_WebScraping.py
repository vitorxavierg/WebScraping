# Importing Libraries
import csv
from bs4 import BeautifulSoup
from selenium import webdriver


# Url function
def get_url(search_term):
    template = 'https://www.cars.com/shopping/results/?stock_type=new&makes%5B%5D={}&models%5B%5D=&list_price_max=&maximum_distance=all&zip='
    search_term = search_term.replace(' ', '_')
    url = template.format(search_term)
    url += '&page={}'
    return url



# Extracting Records
def extract_record(item):
       
    url_beta1 = item.find('a', {'class': 'vehicle-card-link js-gallery-click-link'})
    url_beta2 = url_beta1.get('href')
    url = 'https://cars.com' + url_beta2
    
    try:
        price = item.find('span', {'class': 'primary-price'}).text
    except AttributeError:
        price = 'null'
        
            
    try:
        car = item.find('h2', {'class': 'title'}).text
    except AttributeError:
        car = 'null'
        
    try:
        review = item.find('span', {'class': 'sds-rating__count'}).text 
    except AttributeError:
        review = 'null'
        
            
    result = (url, price, car, review)
    
    return result




# Main Function
def main(search_term):
    
    driver = webdriver.Chrome()
    
    records = []
    
    url = get_url(search_term)
        
        
    for page in range(1,3):
        driver = webdriver.Chrome()
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser') 
        results = soup.find_all('div', {'class': 'vehicle-card-main js-gallery-click-card' })
        
        
        
        for item in results:
            records.append(extract_record(item))
            
            
        driver.close()
            
            
            
            
            
        with open('Fiat.csv', 'w', newline='', encoding='utf-8') as f:
            
            
            writer = csv.writer(f)
            writer.writerow(['Url', 'Price', 'Car', 'Review'])
            writer.writerows(records)