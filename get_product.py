from bs4 import BeautifulSoup

def get_product(data:str):
    product = ['title,author name,price,description']
    soup = BeautifulSoup(markup=data, features='html.parser')

    product_divs = soup.find_all('div', class_ = 'book')
    for i in product_divs:
        title = i.h3.text
        author_name = i.find('p', class_ = 'author').text
        price = i.find('p', class_ = 'price').text
        description = i.find('p', class_ = 'description').text
        product.append(",".join([title, author_name, price, description]))
    product_save = '\n'.join(product)
    with open('data.csv', 'w') as f:
        f.write(product_save)
    return 'ok save'


with open('index.html', 'r') as f:
    data = f.read()

get_csv = get_product(data=data)
print(get_csv)