from bs4 import BeautifulSoup
from errors import default_error, dynamic_error, http_error, connection_error
from rich import print
from requests import HTTPError, ConnectionError
import requests

def search(term: str) -> dict:
    try:
        if " " in term:
            r_box = 'g'
        else:
            r_box = 'g'

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61"}
        req = requests.get(generate_url(term), headers=headers).text
        soup = BeautifulSoup(req, 'lxml')
        results = {
            'results': []
        }
        boxes = soup.find_all('div', class_=r_box)

        for item in boxes:
            title = item.find('h3')
            link = item.find('a')
            if title and link:
                result = {
                    'name': title.text,
                    'link': link['href']
                }
            else:
                result = {
                    'name': 'Desconhecido',
                    'link': 'Não foi possível encontrar o link'
                }

            results['results'].append(result)
        
        return results

    except HTTPError as e:
        return http_error(e)
    except ConnectionError as e:
        return connection_error(e)
    except Exception as e:
        return dynamic_error(e)
    except:
        return default_error()

def generate_url(search_term: str) -> str:
    if " " in search_term:
        used_search_term = search_term.replace(' ', '+')

        return f'https://www.google.com/search?q={used_search_term}&ie=UTF-8&oe=UTF-8'
    
    return f'https://www.google.com/search?q={search_term}&ie=UTF-8&oe=UTF-8'


if __name__ == '__main__':
    print(search('youtube'))