import pandas as pd
from bs4 import BeautifulSoup
import requests
import requests
import time

def xyzz(url, filename):
    max_retries = 20
    retry_count = 0
    
    while retry_count < max_retries:
        response = requests.get(url) 
        if response.status_code == 200:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)
            print("Webpage saved successfully as", filename)
            return ("yoyo")
        elif response.status_code == 503:
            print("Service Unavailable. Retrying in 2 seconds...")
            retry_count += 1
            time.sleep(.25) 
        else:
            return ("Failed to fetch webpage")
        
    return ("Maximum retries reached. Failed to fetch webpage.")


def scrape_amazon(search_term):
    import pandas as pd
    from bs4 import BeautifulSoup

    Index1 = []
    product_links=[]
    product_names1 = []
    product_prices1 = []
    c=0
    for page_num in range(0, 1):  
        url = "https://www.amazon.in/s?k="+search_term.replace(" ","+")#+"&page=" + str(page_num+1)
        print(url)
        bxo="test.html"

        if xyzz(url,bxo)=="yoyo":
            print("done dana done")
        elif xyzz(url,bxo)=="yoyo":
            print('done done done daa')
        else: break

        with open("./test.html", "r", encoding="utf8") as file:
            html_content = file.read()

        soup1 = BeautifulSoup(html_content, "html.parser")
        product_divs = soup1.find_all("div", class_="a-section a-spacing-small a-spacing-top-small")

        
        for div in product_divs:
            product_name_element = div.find("span", class_="a-size-medium a-color-base a-text-normal")
            product_price_element = div.find("span", class_="a-price-whole")
            #product_reviews_element = div.find("span", class_="a-size-base s-underline-text")
            link_element = div.find('a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
            if link_element:
                product_link = link_element['href']
                if not product_link.startswith('http'):
                    product_link = f"https://www.amazon.in{product_link}"
                    product_links.append(product_link)
                    c+=1
                    Index1.append(c)
            else: 
                product_links.append("")
                c+=1
                Index1.append(c)
            
            if product_name_element:
                product_name1 = product_name_element.text.strip()
                product_names1.append(product_name1.lower())
            else: product_names1.append("")

            if product_price_element:
                product_price1 = product_price_element.text.strip()
                product_prices1.append(product_price1)
            else: product_prices1.append("")

    print("Length of Index1:", len(Index1))
    print("Length of product_names1:", len(product_names1))
    print("Length of product_prices1:", len(product_prices1))
    print("Length of product_links:", len(product_links))
    print(Index1)
    print(product_names1)
    print(product_prices1)
    print(product_links)


    df1 = pd.DataFrame({" ": Index1,"product_name": product_names1, "product_price": product_prices1, "product_link":product_links})
    print(df1)

    df1.to_csv("amazon.csv", index=False)
    print("Data has been written to amazon.csv")

def scrape_flipkart(search_term):

    Index = []
    Product_name = []
    Prices = []
    Links = []
    Ram = []

    for page_num in range(1, 5):  
        url = "https://www.flipkart.com/search?q=" + search_term.replace(' ', '%20') + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(page_num)
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        names = soup.find_all("div", class_="KzDlHZ")
        prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")
        links = soup.find_all("a", class_="CGtC98")
        rams = soup.find_all("div", class_="_6NESgJ")
                
        for i, (name, price, link, ram) in enumerate(zip(names, prices, links, rams), start=1):
            Product_name.append(name.text.strip().lower())
            Prices.append(price.text.strip())
            Index.append(i)
            Links.append("https://www.flipkart.com" + link['href'])
            Ram.append(ram.text.strip().lower())

    df = pd.DataFrame({" ": Index, "product_name": Product_name, "product_price": Prices, "product_link": Links, "product_ram": Ram})
    print(df)

    df.to_csv("flipkart.csv", index=False)
    print("Data has been written to flipkart.csv")
