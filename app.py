from flask import Flask, render_template, request
import csv
from webscraping import scrape_flipkart, scrape_amazon

app = Flask(__name__)

# Function to read product prices from Amazon CSV
def read_amazon_prices_from_csv():
    amazon_prices = {}
    with open('amazon.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['product_name']!='' and row['product_price']!=''):
                amazon_prices[row['product_name']] = [row['product_price'],row['product_link']]
    return amazon_prices

# Function to read product prices from Flipkart CSV
def read_flipkart_prices_from_csv():
    flipkart_prices = {}
    with open('flipkart.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['product_name']!='' and row['product_price']!=''):
                if('ram' in row['product_ram']):
                    flipkart_prices[row['product_name']] = [row['product_price'].replace('â‚¹', ''),row['product_link'],row['product_ram'].split('ram')[0].strip()]
                else:
                    flipkart_prices[row['product_name']] = [row['product_price'].replace('â‚¹', ''),row['product_link'],'']
    return flipkart_prices

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for comparison page
@app.route('/compare')
def compare():
    product_name = request.args.get('product_name')
    product_storage = request.args.get('product_storage')
    product_ram = request.args.get('product_ram')
    product_price = request.args.get('product_price').split('-') #list

    search_term='mobile '+product_name+' '+product_storage+' '+product_ram
    scrape_flipkart(search_term)
    scrape_amazon(search_term)
    
    amazon_data = read_amazon_prices_from_csv()
    fk_data = read_flipkart_prices_from_csv()
    print(amazon_data)
    print(fk_data)

    matching_amazon_products = {name: price for name, price in amazon_data.items() 
                                if int(price[0].replace(',','')) in range(int(product_price[0]),int(product_price[1]))}

    matching_flipkart_products = {name: price for name, price in fk_data.items()
                                if int(price[0].replace(',','').replace('₹',''))in range(int(product_price[0]),int(product_price[1]))}

    listC={}
    listD={}
    for fk_key, fk_detail in matching_flipkart_products.items():
        #print(name)
        lst=fk_key.split("(")
        #print(list)
        flipkart_name=lst[0].strip()
        flipkart_color=''
        flipkart_storage=''
        if len(lst)==2:
            color=lst[1]
            #print(color)
            lst2=color.split(",")
            #print(list2)
            flipkart_color=lst2[0]
            if len(lst2)==2:
                flipkart_storage=lst2[1].replace(')','').strip().replace(' ','')
                #print(flipkart_s)
        for amazon_name, amazon_detail in matching_amazon_products.items():
            if flipkart_name in amazon_name and flipkart_color in amazon_name and flipkart_storage in amazon_name and (fk_detail[2].replace(' ', '')+' ram' in amazon_name or fk_detail[2]+' ram' in amazon_name):
                listC[fk_key]=amazon_detail
                listD[fk_key]=fk_detail
                break

    print()
    print()
    print(listC)
    print(listD)           
        
    return render_template('display.html', amazon_products=listC, flipkart_products=listD, search_term=product_name)

if __name__ == "__main__":
    app.run(debug=True)