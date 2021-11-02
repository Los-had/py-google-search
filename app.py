from history import save_history, get_browser_history
from search import search
from rich import print

def main():
    print("Seja bem-vindo ao py-google-search")
    while True:
        try:
            search_term = input("Pesquisa: ")
            save_history(search_term)
            if search_term == '--history':
                print(get_browser_history())
                continue

            s_result = search(search_term)

            for i in s_result['results']:
                name = i['name']
                link = i['link']
                print("========================================================================")
                print(f'Title: {name}')
                print(f'Link: {link}')
        except Exception as e:
            print(e)
            break

if __name__ == '__main__':
    main()