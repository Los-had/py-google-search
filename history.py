from datetime import datetime

def save_history(search_term: str) -> None:
    msg = f'{search_term} - {datetime.now()}\n'

    with open('history.txt', 'a', encoding='utf8') as file:
        file.write(msg)

def get_browser_history() -> str:
    with open('history.txt', 'r', encoding='utf8') as file:
        lines = file.readlines() 
        history = ''
        for line in lines:
            history += line
    
    return history