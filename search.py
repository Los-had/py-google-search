from bs4 import BeautifulSoup
from errors import default_error, dynamic_error, http_error, connection_error
from requests import HTTPError, ConnectionError
import requests

def search(term: str) -> dict:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61"}
    req = requests.get(generate_url(term), headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    results = {
        'results': []
    }
    boxes = soup.find_all('div', class_='g')

    for item in boxes:
        title = item.find('h3')
        link = item.find('a')
        result = {
            'name': title.text,
            'link': link['href']
        }

        results['results'].append(result)
    
    return results

def generate_url(search_term: str) -> str:
    used_search_term = search_term.replace(' ', '+')

    return f'https://www.google.com/search?q={used_search_term}&ie=UTF-8&oe=UTF-8'

if __name__ == '__main__':
    print(search('golang'))