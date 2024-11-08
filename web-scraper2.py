import httpx
from bs4 import BeautifulSoup


url = 'https://www.mobileshop.eu/ios-os/' #it can be any web site as it would need changes in some lines, I chose this website just for an example.
headers = {
    "User-Agent": "search [ my user agent ] in google and paste it here"
}

def extract_phones_data(phone):
    try:
        name = phone.find('div', class_="product-name").string
        price = phone.find('div', class_="price").text

        print(f'Name:{name}, Price:{price}')
        
    except Exception as e:
        print(e)


def main():
    response = httpx.get(url, headers=headers)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    phones = soup.find('div', class_="products-list")
    for phone in phones:
        extract_phones_data(phone)


if __name__ == '__main__':
    main()
