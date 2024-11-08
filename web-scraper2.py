import httpx
from bs4 import BeautifulSoup


url = 'https://www.mobileshop.eu/ios-os/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
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