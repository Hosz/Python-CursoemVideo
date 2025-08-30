import requests
try:
    r = requests.get('https://www.pudim.com.br')
    if r.status_code == 200:
        print(f'Consegui acessar o site Pudim com sucesso!')
except requests.exceptions.ConnectionError:
    print(f'O site Pudim não está acessivel no momento.')