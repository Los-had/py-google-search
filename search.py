from bs4 import BeautifulSoup
from errors import default_error, dynamic_error, http_error, connection_error
from requests import HTTPError, ConnectionError
import requests

def generate_url(search_term: str) -> str:
    used_search_term = search_term.replace(' ', '+')

    return f'https://www.google.com/search?q={used_search_term}&ie=UTF-8&oe=UTF-8'