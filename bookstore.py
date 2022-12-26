from bs4 import BeautifulSoup

def product(data:str):
    product = ['title,author_name,price,description']
    soup = BeautifulSoup(markup=data, features='html.parser')

    product_div = soup.find_all('div', class_ = 'book')
    for i in product_div:
        title = i.h3.text
        author_name = i.find('p', class_ = 'author').text
        price = i.find('p', class_ = 'price').text
        description = i.find('p', class_ = 'description').text
        product.append(",".join([title, author_name, price, description]))
    product_data = '\n'.join(product)
    with open('data.csv', 'w') as f:
        f.write(product_data)

with open('index.html', 'r') as f:
    data = f.read()

csv = product(data=data)
print(csv)