
import requests
def shortner(link,name):
    api = '36639e6e9d2a832591704b32f7133f07f0925'
    base = 'https://cutt.ly/api/api.php'

    payload = {'key': api,'short': link,'name':name}
    request = requests.get(base,params=payload)
    data = request.json()
    print('')

    try:
        title = data['url']['title']
        short = data['url']['shortLink']

        print('Title:', title)
        print('Link:-', short)
    except:
        status=data['url']['status']
        print('Error Status:', status)

link = input("Enter The Link:- ")
name = input("Give your link a name:-")

shortner(link,name)

