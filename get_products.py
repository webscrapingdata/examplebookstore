from bs4 import BeautifulSoup
import csv

# get products from html source as list
def get_products(source: str) -> list:
    # create BeautifulSoup obj
    soup = BeautifulSoup(markup=source, features='html.parser')
    # div book-list
    block_list = soup.find('div', class_='book-list')
    # all div books
    books = block_list.find_all('div', class_='book')
    # list for products
    products = [['title', 'author', 'price', 'description']]
    # iterate each book
    for book in books:
        # get product title
        title = book.find('h3', class_='title').text
        # get product author
        author = book.find('p', class_='author').text
        # get product price
        price = book.find('p', class_='price').text
        # get product description
        description = book.find('p', class_='description').text

        # append product to products
        products.append([title, author, price, description])

    return products


# write products in csv file
def write_products(products: list) -> None:
    # open csv file
    with open('products.csv', 'w') as f:
        # write products in file
        writer = csv.writer(f)
        writer.writerows(products)


# open html file
with open('index.html') as f:
    # get html source
    source = f.read()
    # get products as list
    products = get_products(source)
    # write products in csv file
    write_products(products)
